
# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /workspace

# Copy the current directory contents into the container
COPY . /workspace

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install additional tools if needed (e.g., git)
RUN apt-get update && apt-get install -y git

# Expose port if needed
EXPOSE 8000

# Set default command
CMD [ "python", "main.py" ]
