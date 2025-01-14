FROM python:3.11.11-bookworm

WORKDIR /usr/src/app

RUN pip3 install discord
RUN pip3 install requests
RUN pip3 install python-dotenv

COPY . .

CMD ["python3", "src/main.py"]