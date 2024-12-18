## Market Data Simulator - Kafka Producer
## Overview
This project provides a microservices architecture where you simulate market data, consume it via Kafka, and store it in Redis. Additionally, a Flask API is provided to control the start and stop of these microservices.

In this project, you will find three different types of microservices.

1. MarketDataSimulator
2. DataConsumer
3. DataReader

## Installation
``````````````````````````````````````````````````````````````````````````````````
Install Dependencies:


pip install redis flask
pip install confluent-kafka


Run the Producer:
step 1: python data_reader.py
step2: python api.py



```````````````````````````````````````````````````````````````````````````````````
## Start All Microservices:
Once the API is running, open Postman and send a POST request to the /start endpoint to start all microservices:

POST request: http://127.0.0.1:5000/start

## Stop All Microservices:
To stop all microservices, send a POST request to the /stop endpoint:

POST request: http://127.0.0.1:5000/stop

## License
This project is licensed under the MIT License.

