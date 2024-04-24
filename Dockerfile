# app/Dockerfile

FROM python:3.12-slim

COPY app /app

WORKDIR /app

RUN mv ./.streamlit/config.prod.toml ./.streamlit/config.toml

RUN pip3 install --no-cache-dir -r requirements.txt

RUN groupadd -r streamlit && useradd --no-log-init -r -g streamlit streamlit

USER streamlit

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]