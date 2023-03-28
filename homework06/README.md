# HW 06: Containerized Flask Application for HGNC Human Genome Data Using Redis Database
## Purpose
Currently the non-profit Humand Genome Organization (HUGO) which oversees the HUGO Gene Nomenclature Commmittee (HGNC) has approved almost 43,000 symbols (genes). It is important that there are standardize names for genes to minimize confusion and make it much easier to work with genes. Due to the work of the HGNC we always know that we are talking about the same gene! 

As mentioned there are nearly 43,0000 symbols so it can be difficult to search through the data and get the information you need. This project contianerizes a flask application which is deisgned to make it much eaiser to find the needed gene and information. It also creates a base for developers to build upon the application and create interesting projects.   
## Data
The public [data](https://www.genenames.org/download/archive/) used is provided and maintained by HUGO. At the bottom you will find all of the different formats. The one used for this is 'Current JSON format hgnc_complete_set file'. Furthemore, within the /genes/<hgnc_id> route you will find much more detailed information about what the dataset contains.

## Important Files
gene_api.py: Flask app containing all of the routes allowing user to make a request and get a response. It also contains the code regarding redis, a noSQL database, which allows us to store the data. This is important so that all the data is stored in the case that the flask application stops.

Dockerfile: Containerizes the gene_api.py application. Containerization is important as it allows the script to function the same despite the host device. It will install the necessary libraries used such as Flask, Redis, JSON, and Python. It also makes it easy to share the application once it has been pushed to Docker Hub.

docker-compose.yaml: Makes it much easier to run and stop the entire application. Brlow is the command to launch the application along with redis.  
```
$ docker-compose up -d
```
Closing the application:
```
$ docker-compose down
```
## Pull and use image from Docker Hub
Some users may want something that works out of the box. If so you can simply use a prebuilt image from Docker Hub. 
1. Clone this repository onto your machine. 
2. make a data directory within the cloned repo.
```
$mkdir data
```
3. Pull the image from dockerhub.
```
$dockerpull antjim19037/gene_api:hw06
```
4. Use docker-compose
```
$ docker-compose up -d
```
5. Curl commands to the flask application.

## Build new image from Docker file
If you wish to edit or tailor the code to your needs you can also build your own image. Note that 
1. Clone repository onto your machine.
2. make a data directory within the cloned repo.
```
$mkdir data
```
3. Create docker image
```
$docker build -t <dockerhubusername>/<script name without the .py>:<version> .
```
Running the image:
```
$docker run -it --rm -p <dockerhubusername>/<script name without the .py>:<version>
```   
### Pushing the image to DockerHub
If you wish to push the image to DockerHub:
```
$docker push <dockerhubusername>/<script name without the .py>:<version>
```
4. Use docker-compose
```
$ docker-compose up -d
```
5. Curl commands to the flask application.

## Usage

| Route | Method | Description |
| --- | --- | --- |
| `/data` | POST | Store data into redis |
| | GET | Return all data from redis |
| | DELETE | Delete all data in redis |
| `/genes` | GET | Return json-formatted list of all the hgnc_ids |
| `/genes/<hgnc_id>` | GET | Return all data associated with <hgnc_id> |

### /data route
There are three methods associated with this route.
1. POST - pulls most recent data from internet and stores it into redis. You will see a message saying that the data was loaded in. 
```
$ curl -X POST localhost:5000/data
Data was loaded in.
```
2. GET - returns all the data from redis.
```
$ curl -X GET localhost:5000/data
...
{
    "_version_": 1761599377614307329,
    "agr": "HGNC:13703",
    "alias_symbol": [
      "MAK16L"
    ],
    "ccds_id": [
      "CCDS6089"
    ],
    "date_approved_reserved": "2000-10-19",
    "date_modified": "2023-01-20",
    "date_name_changed": "2015-07-03",
    "date_symbol_changed": "2008-06-04",
    "ena": [
      "AF251062"
    ],
    "ensembl_gene_id": "ENSG00000198042",
    "entrez_id": "84549",
    "gene_group": [
      "RNA binding motif containing"
    ],
    "gene_group_id": [
      725
    ],
    "hgnc_id": "HGNC:13703",
    "location": "8p12",
    "location_sortable": "08p12",
    "locus_group": "protein-coding gene",
    "locus_type": "gene with protein product",
    "mane_select": [
      "ENST00000360128.11",
      "NM_032509.4"
    ],
    "mgd_id": [
      "MGI:1915170"
    ],
    "name": "MAK16 homolog",
    "orphanet": 470626,
    "prev_name": [
      "RNA binding motif protein 13",
      "MAK16 homolog (S. cerevisiae)"
    ],
    "prev_symbol": [
      "RBM13"
    ],
    "pubmed_id": [
      29245012,
      29557065
    ],
    "refseq_accession": [
      "NM_032509"
    ],
    "rgd_id": [
      "RGD:1311297"
    ],
    "status": "Approved",
    "symbol": "MAK16",
    "ucsc_id": "uc003xjj.4",
    "uniprot_ids": [
      "Q9BXY0"
    ],
    "uuid": "e4a49609-b7dd-4be6-ba75-0cac2eda85ad",
    "vega_id": "OTTHUMG00000163957"
  }
]
```
3. DELETE - Deletes data in redis.
```
$ curl -X DELETE localhost:5000/data
data deleted, there are [] keys in the db
```
### /genes route
Returns a list of all of the hgnc_id which the user can then use to get more information using the next route. Here is how to use it:
```
$ curl localhost:5000/genes
...
  "HGNC:50660",
  "HGNC:12209",
  "HGNC:51973",
  "HGNC:56364",
  "HGNC:38352",
  "HGNC:11723",
  "HGNC:11726",
  "HGNC:37230",
  "HGNC:30249",
  "HGNC:47814",
  "HGNC:18854",
  "HGNC:46971",
  "HGNC:15107",
  "HGNC:13703"
]
```
### /genes/<hgnc_id>
Returns all of the data as associated with that hgnc_id in a dictionary. Below we see keys such as alias_symbol, when it was approved, modified, gene group, and much more information that scientist might need for their own projects.
```
$ curl localhost:5000/genes/HGNC:13703
{
  "_version_": 1761599377614307329,
  "agr": "HGNC:13703",
  "alias_symbol": [
    "MAK16L"
  ],
  "ccds_id": [
    "CCDS6089"
  ],
  "date_approved_reserved": "2000-10-19",
  "date_modified": "2023-01-20",
  "date_name_changed": "2015-07-03",
  "date_symbol_changed": "2008-06-04",
  "ena": [
    "AF251062"
  ],
  "ensembl_gene_id": "ENSG00000198042",
  "entrez_id": "84549",
  "gene_group": [
    "RNA binding motif containing"
  ],
  "gene_group_id": [
    725
  ],
  "hgnc_id": "HGNC:13703",
  "location": "8p12",
  "location_sortable": "08p12",
  "locus_group": "protein-coding gene",
  "locus_type": "gene with protein product",
  "mane_select": [
    "ENST00000360128.11",
    "NM_032509.4"
  ],
  "mgd_id": [
    "MGI:1915170"
  ],
  "name": "MAK16 homolog",
  "orphanet": 470626,
  "prev_name": [
    "RNA binding motif protein 13",
    "MAK16 homolog (S. cerevisiae)"
  ],
  "prev_symbol": [
    "RBM13"
  ],
  "pubmed_id": [
    29245012,
    29557065
  ],
  "refseq_accession": [
    "NM_032509"
  ],
  "rgd_id": [
    "RGD:1311297"
  ],
  "status": "Approved",
  "symbol": "MAK16",
  "ucsc_id": "uc003xjj.4",
  "uniprot_ids": [
    "Q9BXY0"
  ],
  "uuid": "e4a49609-b7dd-4be6-ba75-0cac2eda85ad",
  "vega_id": "OTTHUMG00000163957"
}
```
