import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

OLLAMA_URL = "http://ollama:11434/api/generate"
OLLAMA_MODEL = "mistral"

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        data = {
            "model": OLLAMA_MODEL,
            "prompt": prompt
        }
        try:
            r = requests.post(OLLAMA_URL, json=data, timeout=60, stream=True)
            r.raise_for_status()
            result = ""
            for line in r.iter_lines():
                if line:
                    part = json.loads(line.decode('utf-8'))
                    result += part.get("response", "")
            response = result or "No response from Ollama."
        except Exception as e:
            response = f"Error: {e}"
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)