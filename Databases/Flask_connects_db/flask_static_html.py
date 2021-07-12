from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='/')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('./', path)
  
if __name__ == '__main__':
    app.run(port=5000)
