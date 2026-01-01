# 🧡 Swad Desi - Indian Food Ordering App 🇮🇳

**Swad Desi** is a modern, AI-powered Indian food ordering platform inspired by the richness of **Swadeshi culture**. Built using the **MERN (MongoDB, Express, React, Node.js)** stack, this full-stack web application offers seamless food ordering, menu browsing, admin product control, and intelligent AI features like image-based recognition, chatbot support, and a smart voice assistant.

---

## 🚀 Features

### 🏠 User-Facing Pages:
- **Home Page** — Introduction, highlights of offerings, and attractive design.
- **Menu Page** — Displays available Indian dishes with details and prices.
- **About Page** — Tells the story and mission of Swad Desi.
- **Login / Logout** — Secure user authentication system.

---

### 🧠 AI-Powered Features:

#### 🤖 Chatbot Integration (Dialogflow API)
An intelligent chatbot built using Google’s Dialogflow API helps customers with queries, food recommendations, and ordering.

#### 🖼️ Food Image Prediction  
Upload a food image, and the system will:
- Detect whether the food item is present in the menu.
- Redirect the user to that item’s page if available.

#### 🎙️ Voice Assistant (Gemini API + Flask) ✅ _NEW_  
A **voice-controlled AI agent** built with **Flask** and **Google's Gemini API**:
- Allows users to **speak commands** to:
  - Search menu items.
  - Add or remove items from the cart.
  - Navigate pages or get personalized recommendations.
- Offers **hands-free** interaction for accessibility and convenience.
- Integrated directly into the UI with real-time microphone input and text-to-speech responses.

> 🎧 This makes **Swad Desi** feel like you're talking to your personal food assistant.

---

## 🛠️ Admin Panel

- **Product Management** — Admins can add, edit, and remove food items.
- **Authentication** — Admin login/logout secured with JWT & bcrypt.

---

## 🧑‍💻 Tech Stack

| Layer              | Technology                            |
|--------------------|----------------------------------------|
| Frontend           | React.js, Tailwind CSS                 |
| Backend            | Node.js, Express.js                    |
| Database           | MongoDB                                |
| Authentication     | JWT + bcrypt                           |
| AI Models          | Flask (Python) for image & voice AI    |
| Chatbot            | Dialogflow (Google Cloud API)          |
| Voice Assistant    | Gemini API via Flask backend           |
| Deployment         | Vercel / Render / Railway / MongoDB Atlas |

---

## 📁 Project Structure (High-Level)

📦 SwadDesi
├── FLASK_BACKEND/         # Python Flask server for AI tasks
│   ├── voice_assistant/   # Gemini-powered voice assistant
│   └── image_model/       # Food image recognition module
├── FrontEnd/              # React + Tailwind + SpeechRecognition for UI
├── JS_BACKEND/            # Node.js + Express API
├── venv/                  # Python virtual environment
├── .github/               # GitHub Actions / CI workflows
├── .gitignore             # Files to ignore in Git
└── README.md              # You are here!


---

## 📢 Future Improvements

- 🔤 Multilingual voice support (e.g., Hindi, Bengali)
- 🧠 Voice assistant personalization


---

## 🎬 Demo

> Coming soon: Add a screen recording or GIF here showing voice assistant in action.

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

