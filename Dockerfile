FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (fonts and tzdata)
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-dejavu-core \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Set Kyiv timezone
ENV TZ=Europe/Kyiv

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Run bot
CMD ["python", "bot.py"]
