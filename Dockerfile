FROM python:3.11.11-bookworm

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r ./requirements.txt

RUN echo "Done installing requirements"

CMD ["python3", "src/main.py"]