# Slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Create non-root user (required for marks!)
RUN adduser --disabled-password --gecos "" appuser

# Copy and install dependencies FIRST (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]