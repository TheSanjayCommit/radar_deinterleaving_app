Radar Emitter De-Interleaving System
Offline Streamlit Application (Air-Gapped Deployment)
📌 Overview

This project is a fully offline, air-gapped Streamlit application developed for Radar Emitter De-Interleaving and Analysis.
The system is designed to operate without any internet connectivity, making it suitable for defence laboratories, secure environments, and restricted networks.

All dependencies are pre-downloaded as Python wheel (.whl) files and installed locally.

🎯 Key Features

Fully offline execution (no internet required)

Streamlit-based interactive dashboard

Radar PDW (Pulse Descriptor Word) analysis

Density-based clustering (DBSCAN / HDBSCAN)

Machine Learning models (scikit-learn)

Local authentication (username & hashed password)

SQLite database (local storage)

Defence-safe, auditable deployment structure

🛠️ Technology Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
ML / AI	scikit-learn, SciPy
Database	SQLite (local .db file)
Deployment	Local system (air-gapped)
📂 Project Structure
radar_deinterleaving_app/
│
├── app.py                      # Main Streamlit application
├── README.md                   # Offline setup documentation
│
├── offline_packages/           # Pre-downloaded Python wheels
│   ├── streamlit-*.whl
│   ├── numpy-*.whl
│   ├── pandas-*.whl
│   ├── scikit_learn-*.whl
│   ├── scipy-*.whl
│   ├── matplotlib-*.whl
│   └── other_dependency.whl
│
├── data/
│   └── pdw_sample.csv
│
├── database/
│   └── users.db                # SQLite database
│
├── models/
│   └── trained_model.pkl
│
├── utils/
│   ├── auth.py                 # Password hashing logic
│   ├── db.py                   # SQLite helper
│   └── preprocessing.py

🔒 Offline & Security Compliance

✔ No cloud services
✔ No APIs
✔ No external network calls
✔ No OTP / Email authentication
✔ No telemetry or analytics

This system complies with air-gapped deployment requirements commonly followed in defence and research organizations.

🧪 System Requirements

Operating System: Windows 10 / 11

Python Version: Python 3.13.x (Mandatory)

Internet: Not required after setup

Verify Python version:

python --version

📦 Offline Dependency Installation

All required Python packages are stored locally in the offline_packages/ directory.

Step 1: Open terminal in project folder
cd D:\radar_deinterleaving_app

Step 2: Install dependencies (offline)
pip install --no-index --find-links=offline_packages streamlit numpy pandas scikit-learn scipy matplotlib


📌 This command does not access the internet.

▶️ Running the Application (Offline)

After successful installation:

streamlit run app.py


The application will start on:

http://localhost:8501

🗄️ Database (Offline)

Uses SQLite

Database file: database/users.db

Automatically created if not present

Stores:

User credentials (hashed)

Session data

Analysis metadata

🔐 Authentication Mechanism

Local username & password login

Passwords are hashed (SHA-256 / bcrypt)

No OTP, email, or third-party login

Fully offline and secure

🧠 Machine Learning (Offline)

Models trained locally

Algorithms:

DBSCAN / HDBSCAN

Isolation Forest (Anomaly Detection)

Models stored in models/ folder

Loaded using joblib

🚫 Known Limitations

No online maps or APIs

No cloud synchronization

Single-system deployment (unless LAN is used)

📄 Deployment Note (For Review Committees)

“The application is deployed in an air-gapped environment with all software dependencies pre-installed using offline Python wheels.
The system operates independently without internet access, ensuring data security and compliance with defence deployment standards.”



✅ Status

✔ Offline Ready
✔ Defence-Safe
✔ Production Deployable

If you want next, I can:

✅ Generate requirements_offline.txt

✅ Give app.py offline starter template

✅ Provide defence-style deployment diagram

✅ Help convert this into a single .exe