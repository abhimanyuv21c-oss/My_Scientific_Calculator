let activeInput = "inputA"; // Default target

// Switch input focus when target radio changes
function setActiveInput(inputId) {
  activeInput = inputId;
  document.getElementById(inputId).focus();
}

// Handle target radio clicks
document
  .getElementById("targetA")
  .addEventListener("change", () => setActiveInput("inputA"));
document
  .getElementById("targetB")
  .addEventListener("change", () => setActiveInput("inputB"));

// Number pad clicks
document.querySelectorAll(".keypad button").forEach((btn) => {
  btn.addEventListener("click", () => {
    if (btn.classList.contains("clear")) {
      clearInput();
    } else if (btn.classList.contains("backspace")) {
      backspace();
    } else {
      appendValue(btn.dataset.value);
    }
  });
});

// Append value to active input
function appendValue(value) {
  const input = document.getElementById(activeInput);
  input.value += value;
}

// Clear active input
function clearInput() {
  document.getElementById(activeInput).value = "";
}

// Backspace on active input
function backspace() {
  const input = document.getElementById(activeInput);
  input.value = input.value.slice(0, -1);
}

// Handle operations
document.querySelectorAll(".operations button").forEach((btn) => {
  btn.addEventListener("click", () => {
    operate(btn.dataset.op);
  });
});

function operate(op) {
  const a = parseFloat(document.getElementById("inputA").value);
  const b = parseFloat(document.getElementById("inputB").value);

  let result;
  switch (op) {
    case "add":
      result = a + b;
      break;
    case "subtract":
      result = a - b;
      break;
    case "multiply":
      result = a * b;
      break;
    case "divide":
      result = a / b;
      break;
    case "power":
      result = Math.pow(a, b);
      break;
    case "modulo":
      result = a % b;
      break;
    case "sqrt":
      result = Math.sqrt(a);
      break;
    case "log":
      result = Math.log10(a);
      break;
    case "sin":
      result = Math.sin(a);
      break;
    case "cos":
      result = Math.cos(a);
      break;
    case "tan":
      result = Math.tan(a);
      break;
    case "exp":
      result = Math.exp(a);
      break;
    case "ln":
      result = Math.log(a);
      break;
    case "abs":
      result = Math.abs(a);
      break;
    case "fact":
      result = factorial(a);
      break;
    case "inverse":
      result = 1 / a;
      break;
    default:
      result = "Invalid";
  }

  document.getElementById("result").textContent = `Result: ${result}`;
  const operationString = `${op}(${a},${b})`;
  addToHistory(operationString,result);
}

function factorial(n) {
  if (n < 0) return NaN;
  if (n === 0) return 1;
  return n * factorial(n - 1);
}

// History tracking
function addToHistory(operation, result) {
    const historyList = document.getElementById("historyList");

    const li = document.createElement("li");
    li.innerHTML = `<strong>${operation}</strong> = <span>${result}</span>`;
    
    historyList.prepend(li);
}

// Theme toggle
document.getElementById("themeToggle").addEventListener("click", toggleTheme);

function toggleTheme() {
  document.body.classList.toggle("dark-theme");
}
