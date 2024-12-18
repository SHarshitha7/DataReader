from app import initialize_app

app = initialize_app()
if __name__=='__main__':
    app.run(debug=True)

'''
import redis
import json
import time
import config

# Connect to Redis
r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)

def read_market_data():
    while True:
        keys = r.keys()
        for key in keys:
            value = r.get(key)
            print(f"Raw value from Redis: {value}")
            if value:
                try:
                    data = json.loads(value)
                    print(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
        time.sleep(1)

if __name__ == "__main__":
    read_market_data()

'''