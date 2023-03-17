from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response")
def get_response():
    prompt = request.args.get("prompt")
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

if __name__ == "__main__":
    app.run(debug=True)
