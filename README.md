# Anime Recommendation

A recommender system for animes.

## Docker Hub
Please, check image at https://hub.docker.com/r/soutogustavo/recommendation-anime-streamlit

## Build Docker Image

The image can be built by running the following command:

```console
docker build -t recommendation-anime-streamlit .
```

If you use Docker **Desktop**, you should see the built image as follows:
![image](https://github.com/soutogustavo/Recommendation-Anime-Streamlit/assets/9319823/bdb9e816-71fc-4580-84d5-eb07df1e73e6)

If not, you still can see it by running the following command in the (Linux) terminal:
```console
docker images
```
![image](https://github.com/soutogustavo/Recommendation-Anime-Streamlit/assets/9319823/5c0a89b9-033d-4d3a-b8ec-7c748bf47e8e)

## Run Docker Image

Please run the following command to run the recommender system anime image:
```console
docker run -d -p 8501:8501 recommendation-anime-streamlit
```
**Parameters**
 - **-d**: this runs the Docker image as a background process.
 - **-p**: it maps the port 8581 from the container to port 8051 on the host.

## Dashboard

You can also check the recommendation for each user at the Streamlit Dashboard:

> [!CAUTION]
> Unfortunately, the section **Anime Search** is not working because the dataset is too large and GitHub does not allow large files. 

![image](https://github.com/soutogustavo/Recommendation-Anime-Streamlit/assets/9319823/bf08dea7-d592-4457-b6ba-cf32c0ee820a)


