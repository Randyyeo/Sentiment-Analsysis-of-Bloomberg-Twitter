from flask import Flask, send_file, make_response
import word_cloud_bloomberg_twitter

app = Flask(__name__)

@app.route("/")
def cloud():
    bytes_obj = word_cloud_bloomberg_twitter.word_cloud()
    return send_file(bytes_obj,
                     attachment_filename='cloud.png',
                     mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)