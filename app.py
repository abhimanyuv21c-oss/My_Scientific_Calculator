from flask import Flask, request, render_template,jsonify,session
import math

app = Flask(__name__)
app.secret_key = "calculator123"

@app.route("/calculator", methods=["GET","POST"])
def calculator():
    result = None

    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        try:
            a=float(request.form.get("a",0))
            b_raw=request.form.get("b","")
            b=float(b_raw) if b_raw.strip() != "" else None
            operation = request.form["operation"]

            if operation in ["add", "sub", "mul", "div", "pow", "mod"]:
                if b is None:
                    raise ValueError("Second number is required for this operation")
                
                if operation == "add":
                    result = a + b
                    op_str = f"{a} + {b} = {result}"

                elif operation == "sub":
                    result = a - b
                    op_str = f"{a} - {b} = {result}"

                elif operation == "mul":
                    result = a * b
                    op_str = f"{a} * {b} = {result}"

                elif operation == "div":
                    result = a / b if b!=0 else "Error(Divide by Zero)"
                    op_str = f"{a} / {b} = {result}"

                elif operation == "pow":
                    result = a ** b
                    op_str = f"{a} ^ {b} = {result}"

                elif operation == "mod":
                    result = a % b
                    op_str = f"{a} mod {b} = {result}"

            if operation in ["sqrt", "sin", "cos", "tan", "log","exp","ln","abs","fact", "pi","e","reciprocal"]:
                if operation == "sqrt":
                    result = math.sqrt(a)
                    op_str = f"sqrt({a}) = {result}"

                elif operation == "sin":
                    result = math.sin(math.radians(a))
                    op_str = f"sin({a}°) = {result}"

                elif operation == "cos":
                    result = math.cos(math.radians(a))
                    op_str = f"cos({a}°) = {result}"

                elif operation == "tan":
                    result = "Undefined" if a % 180 == 90 else math.tan(math.radians(a))
                    op_str = f"tan({a}°) = {result}"

                elif operation == "log":
                    result = "Error (<=0)" if a <= 0 else math.log(a)
                    op_str = f"log({a}) = {result}"

                elif operation == "exp":
                    result = math.exp(a)
                    op_str = f"exp({a}) = {result}"

                elif operation == "ln":
                    result = "Error (<=0)" if a <= 0 else math.log(a)
                    op_str = f"ln({a}) = {result}"

                elif operation == "abs":
                    result = abs(a)
                    op_str = f"|{a}| = {result}"

                elif operation == "fact":
                    result = "Error (non-integer or <0)" if a < 0 or not float(a).is_integer() else math.factorial(int(a))
                    op_str = f"{int(a)}! = {result}"

                elif operation == "pi":
                    result = math.pi
                    op_str = f"π = {result}"

                elif operation == "e":
                    result = math.e
                    op_str = f"e = {result}"

                elif operation == "reciprocal":
                    result = "Error (÷0)" if a == 0 else 1 / a
                    op_str = f"1/({a}) = {result}"

            if isinstance(result,(float,int)) or "Error" in str(result) or result=="Undefined":
                history = session["history"]
                history.insert(0, op_str)
                session["history"]= history[:10]

        except ValueError:
            return jsonify({"error":"invalid input, please provide numbers"}), 400
        
    return render_template("calculator.html", result=result, history=session["history"])
    
    

if __name__ == "__main__":
    app.run(debug=True)