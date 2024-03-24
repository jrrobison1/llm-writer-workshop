from flask import Flask, request, jsonify
from multi_model_writer_workshop import arthur_chatter, luis_chatter, heidi_chatter

app = Flask(__name__)


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    text = data["text"]
    # Process the text and generate feedbacks using your existing Python code
    # feedbacks = generate_feedbacks(text)
    feedbacks = arthur_chatter.chat(text)
    return jsonify({"feedbacks": feedbacks})


if __name__ == "__main__":
    app.run()
