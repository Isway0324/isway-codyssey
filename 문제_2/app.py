from flask import Flask

app = Flask(__name__)

@app.route("/")                             # 데코레이터 사용
def hello_world():
    return "Hello, DevOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
