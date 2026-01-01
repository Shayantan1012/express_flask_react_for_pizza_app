🇮🇳 Swad Desi – AI-Powered Indian Food Ordering Platform

Swad Desi is a modern, AI-enhanced Indian food ordering application inspired by Swadeshi culture.
It combines a full-stack MERN web platform with a Python-based AI backend that enables voice interaction, intelligent intent handling, and smart food discovery.

The goal is to make food ordering feel natural — as if you’re talking to a human assistant.

🚀 Key Features
🏠 User-Facing Experience

Home Page — Highlights Indian cuisine and brand story

Menu Page — Browse dishes with prices, descriptions, and availability

Cart Management — Add, remove, and review items

Authentication — Secure login & logout system

🧠 AI-Powered Capabilities
🎙️ Smart Voice Assistant (Flask + LLM) ✅

A fully custom voice-controlled AI agent built with Flask and Large Language Models:

Users can speak naturally to:

Search for food items

Ask if an item is available

Add or remove items from the cart

Ask for prices

Navigate pages (menu, home, cart)

Proceed to checkout

🔹 The system first detects intent, then executes business logic, and finally generates a natural spoken response.
🔹 Missing information (like quantity) is handled intelligently via conversation loops.

Example:

User: “Add butter naan”

Assistant: “How many butter naan would you like?”

User: “Two”

Assistant: “Two butter naan have been added to your cart.”

🧠 Intent-Driven AI Architecture (New System)

The voice assistant follows a clean three-stage flow:

Intent Detection (LLM Prompting)

Classifies intent (add_cart, price_query, product_query, etc.)

Extracts products and quantities

Intent Execution (Pure Backend Logic)

Executes database actions (MongoDB)

No LLM decision-making here

Response Generation (LLM-Based Natural Speech)

Generates exactly one human-like sentence

Strictly aligned with the detected intent

This design ensures:

Predictable behavior

Clean separation of concerns

Easy future expansion

🖼️ Food Image Recognition (Flask + ML)

Users can upload a food image:

The system detects whether the dish exists in the menu

Redirects the user to the matching item if available

🤖 Chatbot Integration

An intelligent chatbot helps users with:

Menu exploration

General queries

Food recommendations

(Chatbot runs independently from the voice assistant)

🛠️ Admin Panel

Add, update, and delete food items

Secure admin authentication

Inventory & price management

🧑‍💻 Tech Stack
Layer	Technology
Frontend	React.js, Tailwind CSS
Backend (Main API)	Node.js, Express.js
Database	MongoDB
Authentication	JWT, bcrypt
AI Backend	Python, Flask
Voice AI	LLM-based intent & response engine
Speech	Text-to-Speech (TTS)
Image AI	Python ML models
Deployment	Vercel / Render / Railway / MongoDB Atlas
📁 Project Structure (High-Level)
📦 SwadDesi
├── FLASK_BACKEND/
│   ├── VoiceAssistance_Updated/
│   │   ├── agent/          # LLM orchestrator & memory
│   │   ├── prompts/        # Intent & response prompts
│   │   ├── service/        # Business logic (intent execution)
│   │   ├── routes/         # Flask API routes
│   │   └── utils/          # TTS, validators, helpers
│   ├── image_model/        # Food image recognition
│   └── app.py
├── JS_BACKEND/             # Node.js + Express APIs
├── FrontEnd/               # React + Tailwind UI
├── venv/                   # Python virtual environment
├── .gitignore
├── .env.example
└── README.md

🔐 Security & Best Practices

API keys stored only in .env

.env excluded from Git history

Secrets rotated if ever exposed

Clean separation between AI logic and backend logic

📢 Future Enhancements

🌐 Multilingual voice support (Hindi, Bengali, etc.)

🧠 Personalized voice assistant behavior

🗣️ Continuous voice conversation mode

📊 Voice-driven order analytics

🎬 Demo

🎥 Coming soon — voice assistant live demo video

📝 License

This project is open-source and available under the MIT License.
