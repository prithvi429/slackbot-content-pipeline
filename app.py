from flask import Flask, request, jsonify
from slack_sdk.web import WebClient
from slack_sdk.errors import SlackApiError
import os

from config import SLACK_BOT_TOKEN, FLASK_PORT
import slack_commands

app = Flask(__name__)
client = WebClient(token=SLACK_BOT_TOKEN)


@app.route("/", methods=["GET"])
def index():
    return "Slackbot Content Pipeline - healthy\n"


@app.route("/slack/commands", methods=["POST"])
def slack_commands_endpoint():
    # Slack sends application/x-www-form-urlencoded payloads for slash commands
    form = request.form
    command = form.get("command")
    text = form.get("text")
    user_id = form.get("user_id")

    # Handle the command (returns a dict that will be sent as JSON)
    response = slack_commands.handle_command(command, text, user_id)

    # If the handler returns a `channel` and `text`, post as bot (optional)
    if isinstance(response, dict) and response.get("channel") and response.get("text"):
        try:
            client.chat_postMessage(channel=response["channel"], text=response["text"])
        except SlackApiError as e:
            app.logger.error("Failed to post message: %s", e)

    # For slash commands we typically respond with a JSON body
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=FLASK_PORT)
