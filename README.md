# Enersense hiring challenge
Solution to the Enersense challenge - Backend Developer

## Overview
This application simulates the whole lifecycle of reading data from an EV charging station via MQTT, stores the received data in a database and serves it via a REST API. It is formed of three main components:

- Publisher: simulates the EV charger itself. Connects to MQTT and publishes a new session every minute to a prespecified topic.
- Listener: listens to the same mqtt topic, logs the data received and stores it into a MongoDB database.
- API: connects to the MongoDB database and serves the data to the user.

Tech stack: Python, FastAPI, Docker/Docker compose, HiveMQ MQTT broker, MongoDb/MongoDb Atlas.

## Running instructions
The solution has been written and tested with Python version 3.10.6. It has also been linted by `black`, `isort` and `mypy`.

If you want to setup the virtual environment first, please make sure python3.10-venv is installed or install it by running:

`sudo apt install python3.10-venv`

then run:

`python3 -m venv .venv`

and activate the virtual env:

`source .venv/bin/activate`

Also the project uses `python-dotenv`, so it loads environment variables into a Python session by using a .env file. A sample can be found in .env.example, please create a new .env file and copy the values into it. 

Understandably, some of these values are secrets and should be managed seperately. They are only placed directly in .env.example for the purpose of running this assignment.

This project uses MongoDb Cloud to set the database remotely and the free public MQTT broker HiveMQ.

### Run locally

You can find the commands to run each component seperately (from the root directory). It is recommended to run these commands inside a virtual environment to avoid conflicts. To run all three components, you will need to run each of the following sections in a separate terminal.

#### API

`cd api/` <br />
`python -m pip install -r requirements.txt` <br />
`chmod +x start_api.sh` <br />
`./start_api.sh`


#### Publisher

`cd publisher/` <br />
`python -m pip install -r requirements.txt` <br />
`export PYTHONPATH=. && python app/publish.py`

#### Listener

`cd listener/` <br />
`python -m pip install -r requirements.txt` <br />
`export PYTHONPATH=. && python app/listen.py`


### Run containers

This project uses Docker compose, so everything is set up. You can run the following commands directly from the root directory to run all three containers.

`docker compose build` <br />
`docker compose up`

This will run all three containers in your terminal. You can add `-d` to the second command to run in detached mode.

The API will be reachable on port 8008 and the Swagger UI can be reached at `http://127.0.0.1:8008/docs`.

## Notes

- A QOS level of 1 has been used for both the publisher and the subscriber. Given the sample data, we can assume that the publisher is an EV charging station which posts the cost per charging session. Hence, ensuring the data always arrives is crucial, hence the QOS level is set to AT LEAST ONCE.

- The publisher does not disconnect/reconnect every publishing session. I did a bit of reading regarding whether to keep the connection alive or not and I believe keeping the connection is okay since the sessions are posted every minute. Changing that in the future should not be problematic if need arises.

- Passwords written as plain text inside the repository are just for demonstration purposes, but would not be the case in a real application.

- The publisher and the listener both connect to the broker without TLS, which is also for the sake of the assignment. Normally certs would have to be created and connection should be done over TLS.

- The database contains one dummy item, which is used only for testing. Normally, a seperate testing database/collection should be set up.
