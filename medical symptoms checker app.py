from flask import Flask, render_template, request

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

if __name__ == "__main__":
    app.run(debug=True)
