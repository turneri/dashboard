from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)


def send_push_notification(message):
    pushover_data = {
        "token": os.environ["PUSHOVER_APP_TOKEN"],
        "user": os.environ["PUSHOVER_KEY"],
        "message": message
    }
    requests.post("https://api.pushover.net/1/messages.json", data=pushover_data)


@app.route('/receive', methods=['POST'])
def receive_webhook():
    try:
        data = request.get_json()
        value = data.get("value", "").strip()
        usage = float(value)  
        rounded_usage =usage - 2.5
        formatted_usage = "{:.2f}".format(rounded_usage)
        
        print(f"CPU Usage at {float(formatted_usage) * 10}%") 
        send_push_notification(f"**ALERT** server CPU usage at {float(formatted_usage) * 10}%")
        return jsonify({"status": "ok", "got_usage": usage})

    except Exception as e:
        return jsonify({"error": str(e)}), 500