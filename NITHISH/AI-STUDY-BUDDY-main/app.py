from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/api/assistant")
def assistant():
    data = request.get_json(silent=True) or {}
    question = str(data.get("question", "")).strip().lower()

    if "html" in question:
        answer = "HTML creates the structure of a webpage using elements such as headings, paragraphs, links and forms."
    elif "css" in question:
        answer = "CSS controls the appearance, layout, spacing, colors and responsive design of a webpage."
    elif "javascript" in question:
        answer = "JavaScript adds logic and interactivity to webpages. Practice variables, functions, arrays and DOM manipulation."
    elif "python" in question:
        answer = "Python is a high-level programming language widely used for software development, automation, data science and AI."
    elif "plan" in question:
        answer = "Try a simple plan: 25 minutes JavaScript, 5 minutes break, 25 minutes Python, then 10 minutes quiz revision."
    else:
        answer = "Break the topic into small concepts, learn one concept at a time, and practice with an example."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
