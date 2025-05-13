from flask import Flask, render_template, request
import random

app = Flask(__name__)

# State-specific area codes
us_states = {
    "California": "213",
    "New York": "212",
    "Texas": "214",
    "Florida": "305",
    "Illinois": "312",
    "Georgia": "404",
    "Pennsylvania": "215",
    "Ohio": "614",
    "Michigan": "313",
    "Arizona": "602",
    # Add more as needed
}

# Toll-free area codes
toll_free_codes = ["800", "888", "877", "866", "855", "844", "833"]

@app.route("/", methods=["GET", "POST"])
def home():
    numbers = []
    selected_state = None
    selected_type = None
    count = 0

    if request.method == "POST":
        selected_state = request.form.get("state")
        selected_type = request.form.get("number_type")
        count = int(request.form.get("count", 0))

        for _ in range(count):
            if selected_type == "tollfree":
                area_code = random.choice(toll_free_codes)
            else:
                area_code = us_states.get(selected_state, "000")

            local_number = random.randint(1000000, 9999999)
            formatted = f"({area_code})-{str(local_number)[:3]}-{str(local_number)[3:]}"
            numbers.append(formatted)

    return render_template(
        "index.html",
        states=us_states.keys(),
        numbers=numbers,
        selected_state=selected_state,
        selected_type=selected_type,
        count=count
    )

if __name__ == "__main__":
    app.run(debug=True)