from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Define the URL of your FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000"  

# Function to fetch random anime from the FastAPI endpoint
def fetch_random_anime():
    response = requests.get(f"{FASTAPI_URL}/anime")
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random_anime')
def random_anime():
    anime_data = fetch_random_anime()
    return jsonify(anime_data)

if __name__ == "__main__":
    app.run(debug=True)


