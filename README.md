# 💬 Chat App

A simple real-time chat application built with **Flask** that allows users to join rooms and communicate with each other.  
Users can enter a username, select a room, and start chatting instantly.

---

## 🚀 Features

- Join chat using a **username**
- Create or join a **chat room**
- Real-time message exchange
- Messages stored in a JSON file (for learning/demo)
- Clean and simple UI

---

## 📁 Project Structure

```text
chat_app/
├── templates/
│   └── index.html
├── app.py
├── chat_data.json
├── requirements.txt
└── README.md
```

## 🛠️ Tech Stack

- Python 3  
- Flask  
- HTML, CSS, JavaScript  
- JSON for data storage  

**Optional:**
- Flask-SocketIO for real-time communication  

---

## 📥 Installation


### 1️⃣ Clone the repository

```
git clone https://github.com/suyXcode/chat_app.git
cd chat_app
```

### 2️⃣ Create virtual environment (recommended)

```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```


### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### ▶️ Run the Application

```
python app.py


Open your browser and visit:

http://127.0.0.1:5000
```

- Enter your username and room name to start chatting.
- 

### 📦 Dependencies

```
Your requirements.txt should include:

Flask
Flask-SocketIO
python-engineio
python-socketio
```

### 📌 Notes

- This project uses chat_data.json to store messages (not suitable for production).
- For production, consider:
```
Using a database (SQLite / PostgreSQL)

Adding authentication (Flask-Login)

Using proper WebSockets (Socket.IO)
```

### 🤝 Contributing

Contributions are welcome!
- Fork the repository
- Create a new branch
- Commit your changes
- Open a Pull Request



### 👨‍💻 Author

**Suyash Singh**

- GitHub: https://github.com/suyXcode
- Portfolio: https://suyxcode.netlify.app
  
