# Base image - Python 3.9
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install any additional dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install curl

# Install pip, if not already installed
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py

# Set the working directory in the container
WORKDIR /workspaces/epidemic-research-ai

# Install Python dependencies
COPY requirements.txt /workspaces/epidemic-research-ai/
RUN pip install -r requirements.txt

# Expose default Jupyter port
EXPOSE 8888
