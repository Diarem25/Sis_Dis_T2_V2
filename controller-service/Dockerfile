# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run when the container starts
CMD ["python", "./main.py"]

