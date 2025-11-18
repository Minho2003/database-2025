FROM python:3.12-slim

ENV TZ=Asia/Seoul
RUN apt-get update && apt-get install -y \
    tzdata \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 의존성 파일 먼저 복사 (캐시 활용)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 파일 복사
COPY . /app

EXPOSE 5001

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["python", "app.py"]