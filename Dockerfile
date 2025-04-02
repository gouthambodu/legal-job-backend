FROM python:3.11-slim

# Required for Playwright
RUN apt-get update && apt-get install -y wget gnupg curl unzip fonts-liberation libgtk-3-0 libnss3 libxss1 libasound2 libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxtst6

# Install pip dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m playwright install

# Copy app files
COPY . .

# Expose FastAPI port
EXPOSE 10000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
