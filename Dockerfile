# Base image
FROM python:3.12-slim  

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install GDAL and system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# ✅ Set GDAL environment variables
ENV GDAL_VERSION=3.6.2
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt /app/
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

# Copy rest of the project
COPY . /app/

# ✅ Use gunicorn from the virtual environment
RUN . /opt/venv/bin/activate && python manage.py collectstatic --noinput
CMD ["/opt/venv/bin/gunicorn", "shegar.wsgi:application", "--bind", "0.0.0.0:8000"]