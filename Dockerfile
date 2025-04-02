FROM python:3.11-slim

# Install dependencies for Playwright (Chromium)
RUN apt-get update && apt-get install -y \
    wget gnupg curl unzip \
    fonts-liberation libgtk-3-0 libnss3 libxss1 libasound2 \
    libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 \
    libxfixes3 libxi6 libxrandr2 libxtst6

# Set working directory
WORKDIR /app

# Copy only requirements.txt first (better Docker cache)
COPY requirements.txt .

# Install pip dependencies (including playwright itself)
RUN pip install --upgrade pip
RUN pip install playwright

# Install browser binaries
RUN python -m playwright install

# Now copy the rest of the app
COPY . .

# Expose port
EXPOSE 10000

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
