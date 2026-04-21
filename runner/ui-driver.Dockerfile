FROM mcr.microsoft.com/playwright/python:v1.54.0-noble
WORKDIR /app
RUN python -m pip install --no-cache-dir playwright==1.54.0
COPY runner/ui_driver.py /app/ui_driver.py
