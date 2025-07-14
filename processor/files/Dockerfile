FROM python:3.11-slim

# Set working directory
WORKDIR /processor

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY ./app ./app

# Set environment variables
ENV FLASK_APP=app.main
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000
ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.app:app"]
