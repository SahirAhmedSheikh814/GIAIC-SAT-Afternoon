import streamlit as st
import hashlib
import json
import time
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os

st.set_page_config(page_title="Secure Data Encryption", page_icon="🛡️")

# ------------------- CSS for UI -------------------
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .title {
        font-size: 36px;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        color: #34495e;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #2c3e50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 0.6em 1.2em;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- Utility Functions -------------------
def generate_key(passkey: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(passkey.encode()))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------- File Management -------------------
DATA_FILE = "data.json"
USERS_FILE = "users.json"
LOCKOUT_DURATION = 60  # seconds

# Load or create data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_data = json.load(f)
else:
    stored_data = {}

if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

# ------------------- Session State -------------------
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = None

# ------------------- Navigation -------------------
menu = ["Home", "Login", "Store Data", "Retrieve Data", "Logout"]
choice = st.sidebar.selectbox("Navigation", menu)

# ------------------- Pages -------------------
if choice == "Home":
    st.markdown('<div class="title">🔐 Secure Encryption App</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Built with Streamlit | PBKDF2 | Multi-User Login | JSON Storage</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("✅ Encrypt & store sensitive text.")
        st.markdown("🔐 Protected by secure hashing (PBKDF2).")
        st.markdown("👥 Each user has separate data.")
        st.markdown("📁 All data saved securely in `data.json`.")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png", width=200)

elif choice == "Login":
    st.markdown('<div class="title">🔑 Login or Register</div>', unsafe_allow_html=True)
    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("🔓 Login / Register"):
        if username and password:
            hashed = hash_password(password)
            if username in users:
                if users[username]["password"] == hashed:
                    st.session_state.current_user = username
                    st.success("✅ Logged in successfully!")
                    st.session_state.failed_attempts = 0
                else:
                    st.error("❌ Incorrect password!")
            else:
                salt = os.urandom(16)
                users[username] = {"password": hashed, "salt": base64.b64encode(salt).decode()}
                with open(USERS_FILE, "w") as f:
                    json.dump(users, f)
                st.success("✅ Registered & Logged in!")
                st.session_state.current_user = username

elif choice == "Store Data":
    if not st.session_state.current_user:
        st.warning("🔒 Please login first.")
    else:
        st.markdown('<div class="title">📂 Store Your Secret Data</div>', unsafe_allow_html=True)
        text = st.text_area("📝 Enter your text")
        passkey = st.text_input("🛡️ Create a secure passkey", type="password")

        if st.button("🔐 Encrypt & Save"):
            salt = base64.b64decode(users[st.session_state.current_user]["salt"])
            key = generate_key(passkey, salt)
            f = Fernet(key)
            encrypted_text = f.encrypt(text.encode()).decode()
            stored_data[st.session_state.current_user] = stored_data.get(st.session_state.current_user, [])
            stored_data[st.session_state.current_user].append(encrypted_text)

            with open(DATA_FILE, "w") as f:
                json.dump(stored_data, f)

            st.success("✅ Your data has been encrypted and saved.")

elif choice == "Retrieve Data":
    if not st.session_state.current_user:
        st.warning("🔒 Please login first.")
    else:
        st.markdown('<div class="title">🔍 Retrieve Your Data</div>', unsafe_allow_html=True)

        if st.session_state.lockout_time and time.time() - st.session_state.lockout_time < LOCKOUT_DURATION:
            st.error("⏱️ You are locked out. Please wait before trying again.")
        else:
            entries = stored_data.get(st.session_state.current_user, [])
            if not entries:
                st.info("ℹ️ No data stored yet.")
            else:
                encrypted_text = st.selectbox("🔐 Select Encrypted Entry", entries)
                passkey = st.text_input("🔑 Enter Your Passkey", type="password")

                if st.button("🔓 Decrypt"):
                    salt = base64.b64decode(users[st.session_state.current_user]["salt"])
                    key = generate_key(passkey, salt)
                    f = Fernet(key)
                    try:
                        decrypted = f.decrypt(encrypted_text.encode()).decode()
                        st.success(f"✅ Decrypted Data: {decrypted}")
                        st.session_state.failed_attempts = 0
                    except:
                        st.session_state.failed_attempts += 1
                        attempts_left = 3 - st.session_state.failed_attempts
                        st.error(f"❌ Wrong passkey! Attempts left: {attempts_left}")

                        if st.session_state.failed_attempts >= 3:
                            st.session_state.lockout_time = time.time()
                            st.error("🔒 Too many failed attempts! Please wait before trying again.")

elif choice == "Logout":
    st.session_state.current_user = None
    st.success("🚪 You have been logged out.")
