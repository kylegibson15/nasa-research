FROM python:3.13-slim

RUN apt-get update && apt-get install -y cron

COPY scripts/collector_cron.py /app/collector_cron.py

# At 23:00 on Thursday in every month.
RUN echo "0 23 * */1 4 python /app/collector_cron.py" > /etc/crontab

CMD ["cron", "-f"]