# Search-Engine
This repository contains a Flask web application that utilizes Google's generative AI model to provide answers to user questions. The application processes HTML responses to return plain text answers.

# Project Structure
app.py: Main Flask application.
templates/: Directory containing HTML templates.
index.html: Main HTML file for user interaction.
requirements.txt: Python dependencies for the project.
# Requirements
Python 3.x
Flask
BeautifulSoup4
google-generativeai
Setup

# Clone the repository:
cd generative-ai-flask-app

# Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required packages:
pip install -r requirements.txt
Set up Google Generative AI:

Ensure you have an API key for Google Generative AI and configure it in the app:
genai.configure(api_key='YOUR_API_KEY')
# Run the Flask app:
python app.py
# Access the application:

Open your web browser and navigate to http://127.0.0.1:5000/.

# Usage
Ask a Question:

On the main page, enter a question in the input field and submit it.

Get an Answer:

The application will call Google's generative AI model to get a response and display the plain text answer on the page.

End the Session:

Type end to end the API session.

Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
