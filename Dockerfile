FROM python:3.14-slim
LABEL maintainer=sriram1918@xyz.com

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN useradd -m -s /bin/bash sriram && \
    chown -R sriram:sriram /app
USER sriram

EXPOSE 5000
CMD ['python', 'app.py']