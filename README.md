# OSutilis – Operating System Utilities

OSutilis is a Flask-based system monitoring application that provides real-time insights into operating system resources such as CPU, memory, disk usage, running processes, network activity, and logged-in users. It also exposes RESTful APIs for retrieving system information programmatically.

---

## 📁 Project Structure

```
project/
│
├── app.py               # Main Flask application
│
├── templates/           # HTML templates directory
│   └── index.html       # Main UI template
│
└── static/              # (Optional) CSS / JS files
```

---

## 🚀 Features

- System Resource Monitoring (CPU, Memory, Disk usage)
- Process Management (List running processes with pagination)
- Network Monitoring (Active connections, interface details)
- User Session Tracking (List logged-in users)
- Disk and Sensor Information Retrieval
- RESTful APIs for system insights
- Lightweight and easy-to-use Flask backend

---

## 🛠️ Technologies Used

- Python
- Flask
- psutil
- HTML (Jinja2 Templates)

---

## 📦 Requirements

- Python 3.9 or higher
- Flask
- psutil

---

## ⚙️ Installation

```
pip install flask psutil
```

---

## ▶️ Running the Application

```
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 📌 Notes

- This project uses Flask’s development server.
- Intended for learning, academic projects, and experimentation.
- Not recommended for production deployment without a proper WSGI server (e.g., Gunicorn).

---

## 📄 License

This project is licensed under the BSD 3-Clause License.
