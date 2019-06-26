# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir -p /live_chat
WORKDIR /live_chat

# Install dependencies
RUN pip install --upgrade pip
COPY live_chat/requirements/base.txt .
RUN pip install --no-cache-dir -r base.txt

# Copy project
COPY . /live_chat/

# Server
STOPSIGNAL SIGINT
