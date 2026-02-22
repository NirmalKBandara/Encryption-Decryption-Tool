# Use a lightweight Python
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user
RUN useradd --create-home appuser

# Set the working directory
WORKDIR /home/appuser/app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python scripts
COPY aes_handle.py .
COPY app.py .

# Switch to the non-root user
USER appuser

# Set the default executable 
ENTRYPOINT ["python", "app.py"]