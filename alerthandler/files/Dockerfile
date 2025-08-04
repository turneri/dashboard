FROM python:3.11-slim

# Set working directory
WORKDIR /alerthandler

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY ./app ./app

# Set environment variables
ENV FLASK_APP=app.app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8010
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/sender/app

CMD ["gunicorn", "--bind", "0.0.0.0:8010", "app.app:app"]
