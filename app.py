from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Jenkins CI/CD! Working!"

if __name__ == '__main__':
    print("Starting server on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)