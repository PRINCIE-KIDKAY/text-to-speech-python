# Use Python base image (CPU version)
FROM python:3.10-slim

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    espeak \
    libespeak1 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your code and requirements
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "test.py"]
