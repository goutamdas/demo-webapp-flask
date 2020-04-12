import os
from flask import Flask
app = Flask(__name__)

@app.route('/corona')
def hello():
    return 'Maintain social distancing to beat Corona!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
