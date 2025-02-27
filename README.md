# 💬 AI Chatbot with NVIDIA LLaMA Nemotron & FastAPI

A sleek, modern chatbot built with **FastAPI** and **NVIDIA LLaMA Nemotron 70B**, supporting:
- **Summarization**
- **Translation**
- **Q&A** 
- **General AI conversations**

🚀 **Tech Stack:**
- **Frontend:** HTML, CSS, JavaScript (Chat UI)
- **Backend:** FastAPI (Python)
- **AI Model:** NVIDIA LLaMA Nemotron 70B via OpenAI API
- **Deployment:** Localhost / Cloud

## 🏗️ Project Structure
chatbot-project/
│── static/
│   ├── styles.css        # Frontend styling
│── templates/
│   ├── index.html        # Chatbot UI
│── main.py               # FastAPI backend
│── api_handler.py        # NVIDIA API logic
│── requirements.txt      # Dependencies
│── README.md             # Documentation



## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **AI Model:** NVIDIA LLaMA Nemotron 70B via OpenAI API  
- **Deployment:** Localhost / Cloud  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

git clone 
cd chatbot-project

####2️⃣ Create a virtual environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

###3️⃣ Install dependencies

pip install -r requirements.txt

###4️⃣ Set up NVIDIA API key

Replace YOUR_API_KEY_HERE in main.py with your actual NVIDIA API key.

###5️⃣ Run the FastAPI server

uvicorn main:app --reload

🔗 Open in browser: http://127.0.0.1:8000

##🎨 Frontend UI Overview
📌 UI Features
###✅ Clean and minimal design
###✅ Chat messages with smooth animations
###✅ User and AI messages displayed separately
###✅ Auto-scroll and responsive layout
##🛠️ API Endpoints
--Method	Endpoint	Description
 ---POST	/chat	Sends user input to the chatbot and returns a response
##📌 Future Enhancements
###🏗️ Add user authentication
###🌍 Support more languages for translation
###🎤 Voice input and text-to-speech integration


#🎉 Built with ❤️ by [Chitrangi]


