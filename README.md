# MMDS Final Project
## Completed by: Denys Botuk, Yurii Roziaiev and Tetiana Monchak

![Task](images/task.jpg)

# Repo overview
1. `fetch_data.ipynb` - notebook with code for downloading the stream of recent changes from wikipedia, with sampling
2. `/data` - folder that contains 40k raw and normalized json files of wikipedia edits
3. `main.ipynb` - main notebook with classifier model implementation, its evaluation and bloom filter preparation
4. `/images` - folder with all images and visualizations found within the project
5. `/model` - folder with best saved classifier model files
6. `bloom_filter.pkl` - pickle of trained bloom filter's bitarray and its hashing functions
7. `demo.py` - PySpark Streaming job that acts as a main script during demo that is running within the docker image
8. `Dockerfile`, `entrypoint.sh` and `requirements.txt` - files that are needed to build the docker image for demo

# Docker demo startup
1. From inside the /mmds folder run `docker build -t mmds .`
2. Run using `docker run --rm -p 9999:9999 mmds`

# Demo preview
![demo1 preview](images/demo1.jpg)
![demo2 preview](images/demo2.png)
