import logging
from contextlib import contextmanager

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker, joinedload, Session
from sqlalchemy.exc import IntegrityError
from db import connector

Base = declarative_base()


@contextmanager
def session_scope() -> None:
    """Provide a transactional scope around a series of operations."""
    session = scoped_session(sessionmaker(bind=connector.engine))
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Flat(Base):
    __tablename__ = 'flats'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)

    # Relationship to enable flat.images to return all associated images
    images = relationship("Image", backref="flat")

    def __init__(self, title: str, images: list[str]) -> None:
        self.title = title
        self.images = [Image(url=image) for image in images]

    def insert(self) -> None:
        with session_scope() as session:
            session.add(self)
            Image.insert_multiple(self.images)
            session.commit()

    @staticmethod
    def insert_flats_with_images(flats: list["Flat"]) -> None:
        try:
            with session_scope() as session:
                flat_data = [{'title': flat.title} for flat in flats]
                stmt = insert(Flat).values(flat_data)
                stmt = stmt.on_conflict_do_nothing(index_elements=['title'])
                session.execute(stmt)

                flat_ids = {title: id for (title, id) in session.query(Flat.title, Flat.id)}

                image_data = []
                for flat in flats:
                    flat_id = flat_ids.get(flat.title)
                    for image in flat.images:
                        image_data.append({'url': image.url, 'flat_id': flat_id})

                if image_data:
                    stmt = insert(Image).values(image_data)
                    stmt = stmt.on_conflict_do_nothing()
                    session.execute(stmt)

                session.commit()
        except IntegrityError as e:
            logging.debug("Integrity error: ", e)
            pass

    @staticmethod
    def load_all_flats(session: Session) -> list["Flat"]:
        return session.query(Flat).options(joinedload(Flat.images)).all()


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    flat_id = Column(Integer, ForeignKey('flats.id'))
    url = Column(String, unique=True)

    def insert(self) -> None:
        with session_scope() as session:
            session.add(self)
            session.commit()

    @staticmethod
    def insert_multiple(images: list["Image"]) -> None:
        with session_scope() as session:
            for image in images:
                session.add(image)
            session.commit()

