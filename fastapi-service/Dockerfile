FROM python:3.9

# set a directory for the app
WORKDIR /usr/src/server

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

RUN python -m spacy download en_core_web_sm

# run the command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]