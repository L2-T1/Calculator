from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        expr = request.form.get("expression", "")
        try:
            value = eval(expr)
            if isinstance(value, float):
                value = round(value, 2)
            result = str(value)
        except Exception:
            result = "Error"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

#assistance from github copilot
