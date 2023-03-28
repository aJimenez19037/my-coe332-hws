# HW 06: HUGO Gene No
## Purpose
Currently the non-profit Humand Genome Organization (HUGO) which oversees the HUGO Gene Nomenclature Commmittee (HGNC) has approved almost 43,000 symbols (genes). It is important that there are standardize names for genes to minimize confusion and make it much easier to work with genes. Due to the work of the HGNC we always know that we are talking about the same gene! 

As mentioned there are nearly 43,0000 symbols so it can be difficult to search through the data and get the information you need. This project contianerizes a flask application which is deisgned to make it much eaiser to find the needed gene and information. It also creates a base for developers to build upon the application and create interesting projects.    
## Important Files
## Pull and use image from Docker Hub
## Build new image from Docker file

## Usage

| Route | Method | Description |
| --- | --- | --- |
| `/data` | POST | Store data into redis |
| | GET | Return all data from redis |
| | DELETE | Delete all data in redis |
| `/genes` | GET | Return json-formatted list of all the hgnc_ids |
| `/genes/<hgnc_id>` | GET | Return all data associated with <hgnc_id> |

### /data route
### /genes route
### /genes/<hgnc_id>
