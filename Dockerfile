FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
ENV PYTHONPATH=/app/unilime
RUN chmod +x /app/entrypoint.sh
CMD ["./entrypoint.sh"]
