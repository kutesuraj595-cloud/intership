from flask import Flask, request
import random

app = Flask(__name__)

projects = [
    {"title": "Python Expense Tracker", "desc": "Tracks daily expenses with charts."},
    {"title": "Smart Plant Watering (IoT)", "desc": "Automates watering using soil sensors."},
    {"title": "Snake Game", "desc": "Classic game built with Python."}
]

def recommend_project(skill):
    if "python" in skill.lower():
        return random.choice([p for p in projects if "Python" in p["title"]])
    else:
        return random.choice(projects)

@app.route("/ai", methods=["GET", "POST"])
def ai_helper():
    if request.method == "POST":
        skill = request.form["skill"]
        suggestion = recommend_project(skill)
        return f"<h2>AI Suggestion</h2><p>Based on your skill in {skill}, try: {suggestion['title']} - {suggestion['desc']}</p>"
    return """
    <h2>AI Project Recommender</h2>
    <form method='POST'>
        Enter your skill: <input name='skill'>
        <input type='submit'>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
