# Use slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary folders
RUN mkdir -p artifacts models prediction_logs

# Expose FastAPI port
EXPOSE 8000

# Run API
CMD ["uvicorn", "src.platform.api.app:app", "--host", "0.0.0.0", "--port", "8000"]