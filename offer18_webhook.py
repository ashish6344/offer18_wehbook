from flask import Flask, request
import requests

app = Flask(Vision11)

TELEGRAM_BOT_TOKEN = "7800645235:AAHMjePhblo2PYByKjFa3J5qvGbBfaMkdIo"
TELEGRAM_CHANNEL = "@conversionalert"

@app.route("/offer18-webhook", methods=["GET"])
def handle_postback():
    offer_id = request.args.get("offerid")
    sub_id = request.args.get("aff_sub1")
    payout = request.args.get("payout")
    event = request.args.get("event_token")
    ip = request.args.get("ip")

    message = f"""
🟢 New Conversion Recorded!

🎯 Offer ID: {offer_id}
👤 User (Sub ID): {sub_id}
💰 Cashback: ₹{payout}
⚙️ Event Type: {event}
🌐 IP Address: {ip}

⚡️ Powered by @conversionalert
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHANNEL,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

    return "OK", 200

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
