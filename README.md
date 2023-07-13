# Enersense hiring challenge
Solution to the Enersense challenge - Backend Developer

## Overview
The solution has been written and tested with Python version 3.10.6. It has also been linted by `black`, `isort` and `mypy`.

If you want to setup the virtual environment first, please make sure python3.10-venv is installed or install it by running:

`sudo apt install python3.10-venv`

then run:

`python3 -m venv .venv`

and activate the virtual env:

`source .venv/bin/activate`

Also the project uses python-dotenv, so it loads environment variables into a Python session by using a .env file. A sample can be found in .env.example, please create a new .env file and copy the values into it. 

Understandably, some of these values are secrets and should be managed seperately. They are only placed directly in .env.example for the purpose of running this assignment.

## Run locally

You can find the commands to run each component seperately (from the root directory). It is recommended to run these commands inside a virtual environment to avoid conflicts. To run all three components, you will need to run each of the following sections in a separate terminal.

### API

`cd api/` <br />
`python -m pip install -r requirements.txt` <br />
`chmod +x start_api.sh` <br />
`./start_api.sh`


### Publisher

`cd publisher/` <br />
`python -m pip install -r requirements.txt` <br />
`python app/publish.py`

### Listener

`cd listener/` <br />
`python -m pip install -r requirements.txt` <br />
`python app/listen.py` 


## Run containers

This project uses Docker compose, so everything is set up. You can run the following commands directly to run all three containers.

`docker compose build` <br />
`docker compose up`

## Notes

- A QOS level of 1 has been used for both the publisher and the subscriber. Given the sample data, we can assume that the publisher is an EV charging station which posts the cost per charging session. Hence, ensuring the data always arrives is crucial, hence the QOS level is set to AT LEAST ONCE.

- The publisher does not disconnect/reconnect every publishing session. I did a bit of reading regarding whether to keep the connection alive or not and I believe keeping the connection is okay since the sessions are posted every minute. Changing that in the future should not be problematic if need arises.

- Passwords written as plain text inside the repository are just for demonstration purposes, but would not be the case in a real application.

- The publisher and the listener both connect to the broker without TLS, which is also for the sake of the assignment. Normally certs would have to be created and connection should be done over TLS.
