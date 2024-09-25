# Use the official Python image from Docker Hub
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .
