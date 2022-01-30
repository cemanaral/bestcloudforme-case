# How to build?
Inside the root folder of this repo (where the Dockerfile resides) please run
```
sudo docker build --tag bestcloudforme-case-cem .
```

# How to run?
```
sudo docker run bestcloudforme-case-cem
```

# Notes
Deployed to Heroku using GitHub actions (https://bestcloudformecase.herokuapp.com/)
I have implemented this case using Python & Flask therefore I have used ```python:3.8-slim-buster``` image as a starting point.
