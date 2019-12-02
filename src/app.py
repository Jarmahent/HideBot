from flask import Flask, jsonify
import slack
import os

slack_token = os.environ["SLACK_API_TOKEN"]

client = slack.WebClient(
    token=slack_token,
    run_async=True
    )
app = Flask(__name__)


@app.route("/hide_message", methods=["POST"])
def hide_message():
  client.chat_postMessage(channel='#random',ext="Hook hit!!")
  return jsonify({"status":"Message hidden"})



if __name__ == "__main__":
  app.run(port="8080")