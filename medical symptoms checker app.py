from flask import Flask, render_template, request
import webbrowser
import threading

app = Flask(__name__)

condition_map = {
    "fever": ["Flu", "COVID-19", "Common Cold"],
    "cough": ["Bronchitis", "COVID-19", "Flu"],
    "headache": ["Migraine", "Tension Headache", "Dehydration"],
    "nausea": ["Food Poisoning", "Stomach Flu", "Pregnancy"],
    "rash": ["Allergic Reaction", "Eczema", "Measles"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        symptoms_input = request.form.get("symptoms", "").lower()
        symptoms = [s.strip() for s in symptoms_input.split(",")]

        for symptom in symptoms:
            if symptom in condition_map:
                result.extend(condition_map[symptom])

        result = sorted(set(result))

    return render_template("index.html", conditions=result)

def open_browser():
    print("Opening browser...")
    webbrowser.open_new_tab("http://127.0.0.1:5000/")

if __name__ == "__main__":
    print("Starting app...")
    threading.Timer(1.25, open_browser).start()
    print("If browser didn't open, click here: http://127.0.0.1:5000/")
    app.run(debug=True)


