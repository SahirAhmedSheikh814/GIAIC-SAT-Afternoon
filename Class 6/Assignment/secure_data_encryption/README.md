
# 🛡️ Secure Data Encryption

**A secure web application built with Streamlit to encrypt and store sensitive data using PBKDF2 hashing, Fernet encryption, and JSON storage. The app supports multi-user login, ensuring each user’s data is isolated and securely encrypted.**

## ✨ Features

* **🔒 Data Encryption**: Encrypt sensitive text using Fernet (symmetric encryption) with a secure passkey.

* **🛡️ Secure Hashing**: Derive encryption keys using PBKDF2HMAC with SHA256 for enhanced security.

* **👥 Multi-User Support**: Each user has separate encrypted data, stored securely in data.json.

* **🔑 User Authentication**: Register and login with username and password (hashed using SHA256).

* **⏱️ Lockout Mechanism**: Prevents brute-force attacks by locking out users after 3 failed decryption attempts.

* **📁 JSON Storage**: All encrypted data and user credentials are stored in data.json and users.json.

* **🎨 Custom UI**: Styled with CSS for a modern, user-friendly interface.

## 📂 Project Structure

SECURE_DATA_ENCYPTION/

├── venv/ # Virtual environment

├── data.json # Stores encrypted user data

├── users.json # Stores user credentials (username, hashed password, salt)

├── main.py # Main Streamlit application

├── README.md # Project documentation

└── requirements.txt # Project dependencies  

## 🚀 Installation

#### Prerequisites

* Python 3.8 or higher
* pip package manager

  

#### Steps

  

1. **Clone the Repository (if applicable)**:

git clone <[Repository](https://github.com/SahirAhmedSheikh814/GIAIC-SAT-Afternoon/tree/main/Class%206/Assignment/secure_data_encryption)>

cd SECURE_DATA_ENCYPTION

  
  

2. **Set Up a Virtual Environment**:

python -m venv venv

  

  Activate the virtual environment: 

* On Windows:

venv\Scripts\activate

  
  

* On Mac/Linux:

source venv/bin/activate

  
  
  
  

3. **Install Dependencies**:

pip install -r requirements.txt

  

The requirements.txt file includes:

streamlit==1.38.0

cryptography==43.0.1

  
  

4. **Run the Application**:

streamlit run main.py

  

Open your browser and go to http://localhost:8501 to access the app.

  
  

## 🖥️ Usage

  

1. **Home Page**:

  

* View the app’s features and overview.

* Navigate to other sections using the sidebar.

  
  

2. **Login/Register**:

  

* Enter a username and password to login or register.

* If the username doesn’t exist, it will be registered automatically.

  
  

3. **Store Data**:

  

* Log in first.

* Enter the text you want to encrypt and a secure passkey.

* Click "Encrypt & Save" to store the encrypted text in data.json.

  
  

4. **Retrieve Data**:

  

* Log in first.

* Select an encrypted entry from your stored data.

* Enter the passkey used during encryption.

* Click "Decrypt" to view the original text.

* Note: After 3 failed decryption attempts, you’ll be locked out for 60 seconds.

  
  

5. **Logout**:

  

* Log out to end your session and protect your data.

  
  
  

## 🔧 How It Works

  

* **Encryption**: The app uses the cryptography library’s Fernet class for symmetric encryption. The encryption key is derived from a user-provided passkey using PBKDF2HMAC with a unique salt per user.

* **User Management**: User credentials are stored in users.json, with passwords hashed using SHA256 for security.

* **Data Storage**: Encrypted data is stored in data.json, with each user having their own list of encrypted entries.

* **Security Features**:

 Passwords are never stored in plaintext; they are hashed using SHA256.

A lockout mechanism prevents brute-force attacks by limiting failed decryption attempts.

Each user’s data is isolated, ensuring privacy.

  
  
  

## 📦 Dependencies

  

* streamlit: For building the web application.

* cryptography: For secure encryption and key derivation.

* Standard Python libraries: hashlib, json, time, base64, os.

  

## ⚠️ Security Notes

  

* **Passkey Security**: Choose a strong passkey for encryption, as it’s used to derive the encryption key. If you lose the passkey, you cannot decrypt your data.

* **Data Storage**: The app stores data in data.json and users.json on the local filesystem. For production use, consider using a secure database instead.

* **Local Deployment**: This app is designed for local use (localhost:8501). If deploying publicly, ensure proper security measures like HTTPS and secure user authentication.

  

## 🤝 Contributing

  

1. Fork the repository.

2. Create a new branch (git checkout -b feature-name).

3. Make your changes and commit (git commit -m "Add feature").

4. Push to the branch (git push origin feature-name).

5. Create a pull request.

  

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact

For questions or feedback, feel free to reach out at sahirahmedsheikh5@gmail.com.

  ___

**Built with ❤️ using Streamlit**