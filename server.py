from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔥 ЗАМЕНИТЕ ЭТУ СТРОЧКУ НА ВАШ НАСТОЯЩИЙ КЛЮЧ DEEPSEEK!
DEEPSEEK_API_KEY = "sk-2ad10b19bfe54a949f309da598726f14"
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route('/v1/chat/completions', methods=['POST'])
def proxy():
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        response = requests.post(DEEPSEEK_URL, headers=headers, json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
