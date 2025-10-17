# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl wget && \
    rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8008

# Default environment
ENV ENV=development

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8008"]
