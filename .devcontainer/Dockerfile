# start by pulling the python image
FROM python:3.10.6-buster

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# expose with port the application will run
#EXPOSE 5000

# switch working directory
WORKDIR /app

# upgrade pip
RUN pip install --upgrade pip

# install latest sentry dependency
RUN pip install --upgrade 'sentry-sdk[flask]' --no-cache

# update python buster
RUN apt-get update && apt-get upgrade -y

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt --no-cache

# copy every content from the local file to the image
COPY . /app

# configure the container to no stop in devcontainer
ENTRYPOINT ["tail", "-f", "/dev/null"]