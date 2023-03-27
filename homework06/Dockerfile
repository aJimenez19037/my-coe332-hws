From python:3.8.10

RUN pip install Flask==2.2.2
RUN pip3 install json==0.13.0
RUN pip3 install requests==2.22.0
RUN pip3 install requests==4.5.1

COPY genes_api.py /genes_api.py

CMD ["python", "genes_api.py"]