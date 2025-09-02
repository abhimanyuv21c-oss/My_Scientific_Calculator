# 🧮 Scientific Calculator (Flask + HTML/JS/CSS)

A **Scientific Calculator Web App** built with **Flask (Python)** for the backend and **HTML, CSS, JavaScript, Bootstrap** for the frontend.  
Supports both basic and advanced mathematical operations with a clean UI and keypad.

---

## 🚀 Features
- Number keypad with **C (clear)** and **⌫ (backspace)**  
- Input target selection (**A or B**)  
- Supports operations:
  - ➕ Addition
  - ➖ Subtraction
  - ✖ Multiplication
  - ➗ Division
  - xʸ Power
  - √ Square Root
  - Logarithm (log, ln)
  - Trigonometry (sin, cos, tan)
  - Factorial, absolute, inverse, exp
- History of calculations  
- Dark/Light theme toggle  

---

## 📂 Project Structure
calc/
│── app.py # Flask backend
│── pyvenv.cfg # Virtual environment config
│── templates/
│ └── calculator.html # Main HTML (Jinja template)
│── static/
│ ├── css/
│ │ └── calculator.css # Styles
│ └── js/
│ └── calculator.js # Logic
│── .gitignore
│── README.md

## 💻 Run Locally

1. Clone the repo:

   git clone https://github.com/<your-username>/scientific-calculator.git
   cd scientific-calculator

2.Create virtual environment (optional but recommended)

    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows

3.Install dependencies
    pip install flask

4.Run Flask app
    python app.py

5.Open in browser:
    http://127.0.0.1:5000/calculator