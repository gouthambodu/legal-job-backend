FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget gnupg curl unzip \
    libgbm1 \
    fonts-liberation libgtk-3-0 libnss3 libxss1 libasound2 \
    libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 \
    libxfixes3 libxi6 libxrandr2 libxtst6 \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install pip deps
RUN pip install --upgrade pip
RUN pip install playwright
RUN python -m playwright install
RUN python -m playwright install-deps

# Copy rest of the code
COPY . .

# Expose the port Render expects
EXPOSE 10000

# Run the FastAPI server with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000

