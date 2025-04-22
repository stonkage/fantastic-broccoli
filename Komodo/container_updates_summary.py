from flask import Flask, jsonify
import requests

app = Flask(__name__)

KOMODO_URL = "http://KOMODO CORE/read"
API_KEY = "YOUR KOMODO KEY"
API_SECRET = "YOUR KOMODO SECRET"

HEADERS = {
    "Content-Type": "application/json",
    "X-Api-Key": API_KEY,
    "X-Api-Secret": API_SECRET
}

@app.route("/")
def container_update_summary():
    try:
        # Get all containers
        containers_resp = requests.post(KOMODO_URL, headers=HEADERS, json={
            "type": "ListDockerContainers",
            "params": { "server": "KOMODO HOST" }
        })
        containers = containers_resp.json()

        # Get updates
        updates_resp = requests.post(KOMODO_URL, headers=HEADERS, json={
            "type": "ListUpdates",
            "params": {}
        })
        updates = updates_resp.json()

        # Extract image names
        update_images = {u["image"] for u in updates if "image" in u}

        # Count matches
        total = len(containers)
        updatable = sum(1 for c in containers if c.get("image") in update_images)

        return jsonify({
            "total": total,
            "updates": updatable
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5070)
