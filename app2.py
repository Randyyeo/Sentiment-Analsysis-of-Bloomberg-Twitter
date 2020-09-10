from flask import Flask, send_file, make_response
import sentiment_graph_bloomberg

app = Flask(__name__)

@app.route("/")
def graph():
    bytes_obj_2 = sentiment_graph_bloomberg.sentiment_graph()
    return send_file(bytes_obj_2,
                     attachment_filename='graph.png',
                     mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)