FROM python:3.6

RUN pip3 install aiohttp
RUN pip3 list

COPY web.py .
COPY senha.py .

EXPOSE 8080

CMD ["python3", "-u", "web.py"]
