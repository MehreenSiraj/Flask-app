from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bra_size(underbust, bust):
    """
    Calculate bra size using standard sizing logic.
    Measurements are in inches.
    """
    # Band size: nearest even number
    band = int(round(underbust / 2) * 2)

    diff = bust - band

    if diff < 1:
        cup = "AA"
    elif diff < 2:
        cup = "A"
    elif diff < 3:
        cup = "B"
    elif diff < 4:
        cup = "C"
    elif diff < 5:
        cup = "D"
    elif diff < 6:
        cup = "DD"
    elif diff < 7:
        cup = "DDD"
    else:
        cup = "G+"

    return f"{band}{cup}"

@app.route("/", methods=["GET", "POST"])
def index():
    bra_size = None

    if request.method == "POST":
        try:
            underbust = float(request.form["underbust"])
            bust = float(request.form["bust"])
            bra_size = calculate_bra_size(underbust, bust)
        except ValueError:
            bra_size = "Invalid input"

    return render_template("index.html", bra_size=bra_size)

# 🔴 THIS BLOCK IS REQUIRED — DO NOT REMOVE
if __name__ == "__main__":
    app.run(debug=True)
