# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY server.py .

# Install dependencies
RUN pip install --no-cache-dir flask prometheus_client

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "server.py"]
