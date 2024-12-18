from flask import Flask, request
import subprocess

app = Flask(__name__)

processes = []

@app.route('/start', methods=['POST'])
def start_services():
    global processes
    processes.append(subprocess.Popen(["python", "../MarketDataSimulator/market_data_simulator.py"]))
    processes.append(subprocess.Popen(["python", "../DataConsumer/data_consumer.py"]))
    processes.append(subprocess.Popen(["python", "data_reader.py"]))
    return {"message": "All microservices started successfully"}, 200

@app.route('/stop', methods=['POST'])
def stop_services():
    global processes
    for process in processes:
        process.terminate()
    processes = []
    return {"message": "All microservices stopped successfully"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)