FROM python:3.11.9

WORKDIR /usr/src/app

COPY src/requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./src/main.py" ]