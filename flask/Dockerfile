FROM python:3.10
WORKDIR "/app"

# Production server dependency
RUN pip install gunicorn
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
