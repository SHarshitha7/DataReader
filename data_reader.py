import redis
import time
import json

# Redis Configuration
REDIS_HOST = "redis.finvedic.in"
REDIS_PORT = 6379

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def read_data():
    print("Reading data from Redis...")
    while True:
        keys = redis_client.keys("*")
        for key in keys:
            data = redis_client.get(key)
            print(f"Ticker: {key}, Data: {data}")
        time.sleep(3)

if __name__ == "__main__":
    read_data()
