FROM python:3.9-slim

RUN apt update
RUN pip3 install Flask

WORKDIR /app

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
