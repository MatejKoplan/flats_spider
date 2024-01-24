from contextlib import contextmanager

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker, joinedload

from flats_project.db import connector

Base = declarative_base()


@contextmanager
def session_scope():
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
    title = Column(String)

    # Relationship to enable flat.images to return all associated images
    images = relationship("Image", backref="flat")

    def __init__(self, title: str, images: list[str]):
        self.title = title
        self.images = [Image(url=image) for image in images]

    def insert(self):
        with session_scope() as session:
            session.add(self)
            Image.insert_multiple(self.images)
            session.commit()

    # def __dict__(self):
    #     return {"title": self.title, "images": [dict(image) for image in self.images]}


    @staticmethod
    def insert_flats_with_images(flats: list["Flat"]):
        with session_scope() as session:
            session.bulk_save_objects(flats)

            images = []
            for flat in flats:
                for image in flat.images:
                    image.flat_id = flat.id
                    images.append(image)

            # Bulk insert images
            if images:
                session.bulk_save_objects(images)
            session.commit()

    @staticmethod
    def load_all_flats():
        with session_scope() as session:
            # Use joinedload for eager loading of the images relationship
            flats = session.query(Flat).options(joinedload(Flat.images)).all()
            return flats


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    flat_id = Column(Integer, ForeignKey('flats.id'))
    url = Column(String)

    # def __dict__(self):
    #     return {"url": self.url}

    def insert(self):
        with session_scope() as session:
            session.add(self)
            session.commit()

    @staticmethod
    def insert_multiple(images: list["Image"]):
        with session_scope() as session:
            for image in images:
                session.add(image)
            session.commit()
