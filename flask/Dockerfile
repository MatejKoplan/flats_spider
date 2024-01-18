# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR "/app"

RUN pip install gunicorn

# Copy the Flask app's requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the Flask application
COPY . .

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
