# Use a slim Python 3.11 image for a minimal attack surface
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Prevent Python from generating .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=UTC

# Install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy source code
COPY . .

# Run the entrypoint script
CMD ["python", "main.py"]