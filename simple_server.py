from flask import Flask, Response, request
import os, pickle

app = Flask(__name__)

@app.route('/', methods=["POST"])
def base():
    print(list(request.form)[0])
    return Response(status=200)

@app.route('/upload', methods=["POST"])
def upload():
    print(pickle.loads(request.files['afile'].read()))
    return Response(status=200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)