import os
import socket

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    html = """
    Hello {name}
    Hostname: {hostname}
    """
    return html.format(name=os.getenv("NAME","py-user"),hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)