from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask running in a container - ECS CI / CD test - V1"

@app.route('/flask')
def hello_eks():
    return "Hello from Flask running in EKS"

@app.route('/health-check')
def healthy():
    return "Service is healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)