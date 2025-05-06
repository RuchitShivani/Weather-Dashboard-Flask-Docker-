# Use official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages directly
RUN pip install flask requests

# Expose the port the app runs on
EXPOSE 3017

# Define environment variable for Flask to run in production
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=3017"]
