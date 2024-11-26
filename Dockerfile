# use slim python image
FROM python:3.13-slim

# install pipenv in docker
RUN pip install pipenv

# set working directory
WORKDIR /app

# copy model, script for flask deployment and dependencies
COPY ./models ./models
COPY ./scripts ./scripts
COPY ./Pipfile .
COPY ./Pipfile.lock .

# install dependencies
RUN pipenv install --system --deploy

# expose port
EXPOSE 9696

# run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:9696", "scripts.predict:app"]