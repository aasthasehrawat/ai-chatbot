from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    ai_response = f"Echo: {user_input}"
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
