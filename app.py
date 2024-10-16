from flask import Flask, render_template, request

app = Flask(__name__)

# Calculator route
@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            # Get form values
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            # Perform calculation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2
        except (ValueError, ZeroDivisionError):
            result = "Invalid input or division by zero"

    return render_template("index.html", result=result)
@app.route("/lavda1111")
def lavda():
    return render_template("love/lovda.html")

if __name__ == "__main__":
    app.run(debug=True)
