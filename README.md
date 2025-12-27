🧮 Bra Size Calculator – Flask Web App

A simple, accurate, and SEO-friendly **Bra Size Calculator** built with **Flask (Python)**.
This app allows users to calculate their bra size using **underbust and bust measurements**, with no signup, no data storage, and full privacy.

The project is designed as a **tool-based web app**, suitable for learning Flask fundamentals and building SEO-friendly utility tools.

---

## 🚀 Features

* ✅ Accurate bra size calculation (band + cup)
* ✅ Server-side calculation (SEO-friendly)
* ✅ Clean Flask architecture
* ✅ Beginner-friendly codebase
* ✅ Privacy-first (no user data stored)
* ✅ Ready for SEO & AdSense-style monetization
* ✅ Built with Python 3.11 + Flask 3+

---

## 🛠️ Tech Stack

* **Backend:** Python 3.11, Flask
* **Frontend:** HTML (Jinja2 templates)
* **Styling:** Basic CSS (optional)
* **Environment:** Conda
* **Editor:** Visual Studio Code
* **Server:** Flask development server

---

## 📂 Project Structure

```
bra_size_calculator/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
│
├── templates/
│   └── index.html      # Main calculator page
│
├── static/             # (Optional) CSS / JS files
│
└── frontend/           # (Optional) future UI work
```

---

## ⚙️ Installation & Setup (Step-by-Step)

### 1️⃣ Create & Activate Conda Environment

```bash
conda create -n flask.env python=3.11
conda activate flask.env
```

### 2️⃣ Install Dependencies

```bash
pip install flask
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

You should see output like:

```
Running on http://127.0.0.1:5000
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 How the Bra Size Calculation Works

### Inputs

* **Underbust (inches):** Measurement taken snugly under the bust
* **Bust (inches):** Measurement taken around the fullest part of the bust

### Logic

* Band size is calculated by rounding the underbust to the nearest even number
* Cup size is calculated based on the difference between bust and band size

### Example

```
Underbust: 31 inches
Bust: 35 inches

Band → 32
Difference → 3 inches
Cup → C

Result: 32C
```

This logic follows commonly used industry sizing guidelines.

---

## 🧩 Core File Explanation

### `app.py`

* Initializes Flask app
* Contains bra size calculation logic
* Handles GET & POST requests
* Renders results using Jinja templates
* Starts the Flask server

### `templates/index.html`

* Displays the calculator form
* Shows calculated result
* Structured for SEO (H1, descriptive text)

---

## 🔍 SEO Considerations

This app is intentionally built as a **server-rendered tool**, not a JavaScript-only calculator.

SEO-friendly choices:

* Server-side rendering (Flask + Jinja)
* Clean URL (`/`)
* Semantic HTML structure
* Tool-focused content (not blog fluff)
* Fast load time
* No forced user interaction

This makes it suitable for:

* Google indexing
* Tool-based keyword ranking
* AdSense approval (with proper policies)

---

## 🔐 Privacy & Data Policy

* ❌ No user data stored
* ❌ No cookies or tracking
* ❌ No database
* ✅ Calculations happen only in memory

This makes the tool safe, private, and compliant with basic privacy expectations.

---

## 🧪 Common Issues & Fixes

### Flask does not start

Ensure `app.py` contains:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

### Browser shows nothing

* Confirm Flask server is running
* Check `http://127.0.0.1:5000`
* Ensure `index.html` exists in `templates/`

---

## 🛣️ Future Improvements (Roadmap)

* ⏳ CM ↔ Inches unit toggle
* ⏳ UK / EU / US size conversion
* ⏳ Improved UI styling
* ⏳ JSON-LD SEO schema (SoftwareApplication)
* ⏳ Deployment to Render / Railway
* ⏳ Multi-tool SEO hub integration

---

## 📚 Learning Purpose

This project is ideal for:

* Flask beginners
* Python learners
* SEO tool builders
* Utility-based SaaS experiments
* Portfolio projects

---

## 📄 License

This project is open-source and free to use for learning and experimentation.

