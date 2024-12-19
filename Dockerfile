# Replace with your compatible version
FROM python:3.12-slim  

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Create working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project files
COPY . /app/

# Command to run the application
CMD ["gunicorn", "project_name.wsgi:application", "--bind", "0.0.0.0:8000"]