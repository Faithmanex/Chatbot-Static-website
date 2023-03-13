import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Set up OpenAI API
openai.api_key = "YOUR_API_KEY"

# Define the chatbot function
def ask_openai(question):
    response = openai.Completion.create(
        engine="davinci", prompt=question, max_tokens=60, n=1, stop=None, temperature=0.5
    )
    answer = response.choices[0].text.strip()
    return answer

# Define the home page
@app.route("/")
def home():
    return render_template("index.html")

# Define the chat page
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["user_message"]
    bot_message = ask_openai(user_message)
    return {"bot_message": bot_message}

if __name__ == "__main__":
    app.run(debug=True)
