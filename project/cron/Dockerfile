FROM python:3
RUN mkdir -p /usr/src/pycron/
WORKDIR /usr/src/pycron
COPY . .
RUN pip install -r requirements.txt

CMD ["python3","pycron.py"]