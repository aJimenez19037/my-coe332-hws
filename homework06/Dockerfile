From python:3.8.10

RUN pip install Flask==2.2.2
RUN pip3 install requests==2.22.0
RUN pip3 install redis==4.5.1

COPY gene_api.py /gene_api.py

CMD ["python", "gene_api.py"]