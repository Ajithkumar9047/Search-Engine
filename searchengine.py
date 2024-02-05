from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key='AIzaSyBW2k1uJvP_rZyFj1WJkfvmQlwnjT_C5-A')
model = genai.GenerativeModel('gemini-pro')

def to_plain_text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    plain_text = soup.get_text(separator='\n', strip=True)
    return plain_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_answer', methods=['GET'])
def generate_answer():
    try:
        user_question = request.args.get('question', '')

        if user_question.lower() == 'end':
            return jsonify({"message": "API session ended"}), 200

        response = model.generate_content(user_question)
        plain_text_result = to_plain_text(response.text)
        
        return jsonify({"answer": plain_text_result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
