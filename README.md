# 🇮🇳 Swad Desi – AI-Powered Indian Food Ordering Platform

Swad Desi is a modern, AI-driven Indian food ordering application inspired by Swadeshi culture.  
It combines a full-stack MERN platform with a Python-based AI backend that enables **voice interaction**, **intelligent intent handling**, and **image-based food recognition**.

The goal of Swad Desi is to make food ordering natural, conversational, and smart — just like talking to your personal food assistant.

---

## 🚀 Features

### 🏠 User-Facing Experience
- **Home Page** – Brand introduction and featured dishes  
- **Menu Page** – Browse Indian dishes with prices and descriptions  
- **Cart Management** – Add, remove, and review items  
- **Authentication** – Secure login and logout  

---

## 🧠 AI-Powered Capabilities

### 🎙️ Smart Voice Assistant (Flask + LLM)
A custom-built voice assistant using **Flask** and **Large Language Models**.

Users can speak naturally to:
- Search menu items  
- Check availability  
- Add or remove items from the cart  
- Ask for prices  
- Navigate pages (home, menu, cart)  
- Proceed to checkout  

#### Voice Assistant Architecture
1. **Intent Detection** – LLM analyzes user speech  
2. **Intent Execution** – Backend business logic handles the task  
3. **Response Generation** – LLM generates a single, natural spoken sentence  

The assistant automatically asks follow-up questions if required information (like quantity) is missing.

---

### 🖼️ Food Image Recognition (Flask + Vision Transformer)
Users can upload a food image, and the system will:
- Use a **pretrained Vision Transformer (ViT)** model from Hugging Face  
- Predict the food item from the image  
- Check availability in the database  
- Redirect to the product page if available  

**Model Details**
- Architecture: Vision Transformer (ViT)  
- Source: Hugging Face pretrained models  
- Backend: Python + Flask  

---

### 🤖 Chatbot Support
An intelligent chatbot helps users with:
- Menu exploration  
- Food recommendations  
- General queries  

---

## 🛠️ Admin Panel
- Add, update, and delete food items  
- Secure admin authentication  
- Inventory and price management  

---

## 🧑‍💻 Tech Stack

| Layer | Technology |
|------|-----------|
| Frontend | React.js, Tailwind CSS |
| Backend | Node.js, Express.js |
| Database | MongoDB |
| Authentication | JWT, bcrypt |
| AI Backend | Python, Flask |
| Voice AI | LLM-based intent & response engine |
| Image AI | Vision Transformer (ViT – Hugging Face) |
| Speech | Text-to-Speech |
| Deployment | Vercel, Render, Railway, MongoDB Atlas |

---

## 📁 Project Structure

```text
SwadDesi
├── FLASK_BACKEND
│   ├── VoiceAssistance_Updated
│   │   ├── agent
│   │   ├── prompts
│   │   ├── service
│   │   ├── routes
│   │   └── utils
│   ├── image_model
│   └── app.py
├── JS_BACKEND
├── FrontEnd
├── venv
├── .env.example
├── .gitignore
└── README.md

---

## 🔐 Security Practices
- All API keys are stored securely using environment variables  
- The `.env` file is excluded from Git commits  
- No hardcoded secrets are present in the codebase  
- GitHub secret scanning is respected to prevent accidental key leaks  

---

## 📢 Future Enhancements
- 🌐 Multilingual voice support (Hindi, Bengali, etc.)  
- 🧠 Personalized voice assistant behavior  
- 🔁 Continuous conversational voice mode  
- 📊 Voice-based analytics and user insights  
- 🛒 Smarter cart recommendations using user history  

---

## 🎬 Demo
A demo video and screenshots showcasing:
- Voice-based food ordering  
- Image recognition workflow  
- Real-time cart interaction  

Coming soon.

---

## 📝 License
This project is open-source and available under the **MIT License**.

You are free to use, modify, and distribute this project with proper attribution.
