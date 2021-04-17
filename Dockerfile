FROM mcr.microsoft.com/playwright:bionic

WORKDIR /app
ADD . .
RUN pip3 install -r requirements.txt && python3 -m playwright install && chmod +x /app/main.py

CMD "/app/main.py"
