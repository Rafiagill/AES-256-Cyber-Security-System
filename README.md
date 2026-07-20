# 🔐 AES-256 Cyber Security System

A professional desktop application developed in Python that provides secure file encryption and decryption using the Advanced Encryption Standard (AES-256). The project was developed as a Final Year Project (FYP) for Cyber Security and demonstrates practical implementation of modern cryptographic techniques with an interactive graphical interface.

---

## 📌 Project Overview

The AES-256 Cyber Security System is designed to provide secure file protection through password-based encryption while offering a professional desktop interface for users. Besides encryption and decryption, the system includes multiple security analysis tools such as entropy analysis, avalanche effect analysis, activity logging, and encryption performance benchmarking.

The application is built using Python and CustomTkinter and is packaged as a standalone Windows executable using PyInstaller.

---

# ✨ Features

- 🔐 AES-256 File Encryption
- 🔓 AES-256 File Decryption
- 🔑 SHA-256 Password-Based Key Generation
- 👤 User Authentication System
- 📁 Multiple File Encryption Support
- 📊 Encryption Performance Benchmarking
- ⚡ Encryption Speed Calculation
- 📈 AES Performance Comparison
- 🌊 Avalanche Effect Analysis
- 🧠 Entropy Analysis
- 📜 Activity Logging
- 📂 Organized Reports, Logs, and Results
- 🌙 Dark/Light Theme Switching
- 📉 Progress Bar
- 📋 Live Results Panel
- 💻 Modern CustomTkinter GUI
- 📦 Standalone Windows Executable

---

# 🛠 Technologies Used

- Python 3.10
- CustomTkinter
- Cryptography Library
- SHA-256
- AES-256 (CBC Mode)
- Pandas
- Matplotlib
- PyInstaller

---

# 📂 Project Structure

```
AES_Project/
│
├── modern_aes_gui.py
├── aes_gui.py
├── aes_logo.ico
│
├── Logs/
│   └── activity_log.txt
│
├── Reports/
│   └── encryption_report.pdf
│
├── Results/
│   ├── aes_comparison_results.csv
│   ├── entropy_results.csv
│   ├── performance_results.csv
│   └── avalanche_results.csv
│
├── test_files/
│
├── build/
├── dist/
│
└── README.md
```

---

# 🔐 Encryption Workflow

1. User Login
2. Select Files
3. Enter Password
4. SHA-256 generates 256-bit key
5. AES-256 encrypts selected files
6. Encrypted files are saved
7. Activity is logged
8. Performance metrics are displayed

---

# 🔓 Decryption Workflow

1. Select encrypted files
2. Enter password
3. SHA-256 regenerates encryption key
4. AES decrypts the file
5. Original file is restored
6. Logs are updated

---

# 📊 Security Features

## AES-256 Encryption

The application uses the Advanced Encryption Standard (AES-256) operating in CBC mode for secure encryption.

## SHA-256 Key Generation

Passwords entered by users are converted into secure 256-bit encryption keys using SHA-256 hashing.

## Activity Logging

Every important action is recorded with timestamps, including:

- User Login
- File Selection
- Encryption
- Decryption
- Performance Analysis
- Entropy Analysis

---

# 📈 Performance Analysis

The application measures

- Encryption Time
- Decryption Time
- Encryption Speed (MB/s)
- AES Performance Comparison

Graphs are automatically generated using Matplotlib.

---

# 📊 Security Analysis

The project includes

- Entropy Analysis
- Avalanche Effect Analysis
- AES Performance Comparison

These analyses demonstrate the effectiveness and randomness of the encryption process.

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AES-256-Cyber-Security-System.git
```

Go to project folder

```bash
cd AES-256-Cyber-Security-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python modern_aes_gui.py
```

---

# 📦 Create EXE

```bash
pyinstaller --onefile --windowed --icon=aes_logo.ico AES_Security_Suite.py
```

---

# 📸 Screenshots

## Login Window

![image alt](https://github.com/Rafiagill/AES-256-Cyber-Security-System/blob/6609bbe1a51d71770d2b3c14be08667e050b999c/Screenshot%202026-07-21%20001946.png)

---

## Dashboard

![image alt](https://github.com/Rafiagill/AES-256-Cyber-Security-System/blob/14cbc9bf0c485d22cf168859cb034e5f9b878fea/Screenshot_21-7-2026_02017_.jpeg)

---

## AES Performance

![image alt](https://github.com/Rafiagill/AES-256-Cyber-Security-System/blob/098d12fc4b05f549cce9d1d72230794b3ca097ac/Screenshot_21-7-2026_02049_.jpeg)

---

## Entropy Analysis

![image alt](https://github.com/Rafiagill/AES-256-Cyber-Security-System/blob/098d12fc4b05f549cce9d1d72230794b3ca097ac/Screenshot_21-7-2026_02049_.jpeg)

---

## Avalanche Analysis

![image alt](https://github.com/Rafiagill/AES-256-Cyber-Security-System/blob/098d12fc4b05f549cce9d1d72230794b3ca097ac/Screenshot_21-7-2026_02049_.jpeg)

---

## Activity Logs

![image alt](https://github.com/Rafiagill/AES-256-Cyber-Security-System/blob/309919c1bf0e501b106da7ca7a78de7e136edbb8/Screenshot_21-7-2026_02120_.jpeg)

---

# 📚 Learning Outcomes

- Applied AES-256 encryption for secure file protection.
- Implemented password hashing using SHA-256.
- Developed a professional desktop GUI with CustomTkinter.
- Implemented real-time encryption monitoring.
- Performed cryptographic performance evaluation.
- Created a deployable Windows application using PyInstaller.

---

# 🚀 Future Enhancements

- AES-GCM Authentication
- RSA Hybrid Encryption
- Digital Signatures
- Cloud Storage Integration
- Database Authentication
- Two-Factor Authentication (2FA)
- Secure File Sharing
- Drag-and-Drop File Encryption
- Automatic Backup and Recovery
- Cross-Platform Support

---

# 👨‍💻 Author

**Rafia Rehman**

Bachelor of Science in Cyber Security

Final Year Project

The Islamia University of Bahawalpur

---

# 📄 License

This project is developed for educational and research purposes.
