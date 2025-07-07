# Base image
FROM python:3.12-slim  

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

ENV GDAL_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgdal.so
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV PORT=8000

WORKDIR /app

COPY requirements.txt /app/

RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

# ✅ Collect static files
RUN . /opt/venv/bin/activate && python manage.py collectstatic --noinput

CMD ["gunicorn", "shegar.wsgi:application", "--bind", "0.0.0.0:$PORT"]