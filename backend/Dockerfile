FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk del build-deps && \
    apk --no-cache add musl-dev linux-headers g++
WORKDIR /backend
COPY requirements.txt /backend/
RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt
COPY . .
# run entrypoint.sh
ENTRYPOINT ["/backend/entrypoint.sh"]