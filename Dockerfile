FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PORT=8080
RUN mkdir -p ~/.streamlit && \
    printf "[server]\nheadless=true\nenableCORS=false\nenableXsrfProtection=false\nport=8080\n" > ~/.streamlit/config.toml

EXPOSE 8080
CMD ["streamlit", "run", "ivey_synthetic_data_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
