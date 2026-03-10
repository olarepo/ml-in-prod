# Base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure models directory exists
RUN mkdir -p models

# Default command
CMD ["uvicorn", "src.platform.api.app:app", "--host", "0.0.0.0", "--port", "8000"]