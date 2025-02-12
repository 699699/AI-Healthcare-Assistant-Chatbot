# AI-Healthcare-Assistant-Chatbot
Healthcare Assistant Chatbot 🤖
A simple and interactive healthcare chatbot built using Streamlit and Hugging Face's GPT-2 model. This chatbot assists users with common healthcare queries like symptoms, appointments, and medication. It provides responses in an engaging and interactive UI with custom styling and emojis.

Key Features ✨
Healthcare Query Assistance: Handles queries related to symptoms, appointments, and medication.
Interactive UI: Includes a user-friendly interface with emojis to make the interaction more engaging.
Custom Styling: The app uses custom CSS for styling and enhancing the user experience.
Hugging Face GPT-2 Model: The backend uses Hugging Face's GPT-2 model for generating responses.
Technologies Used 🔧
Streamlit: For building the interactive web application.
Hugging Face Transformers: For using GPT-2 model for text generation.
NLTK: For text processing, including tokenization and stopword handling.
Python 3.x: The core language for this project.
How to Set Up 🛠️

Step 1: Install Dependencies 📦
Clone the repository and create a virtual environment:

bash
Copy
Edit
git clone https://github.com/your-username/healthcare-chatbot.git
cd healthcare-chatbot
python -m venv myvenv
Activate the virtual environment:

Windows:

bash
Copy
Edit
.\myvenv\Scripts\activate
Mac/Linux:

bash
Copy
Edit
source myvenv/bin/activate
Install required dependencies:

bash
Copy
Edit
pip install streamlit transformers nltk
Step 2: Get Hugging Face API Key 🔑
Sign up on Hugging Face and get your API key.

Replace the api_key variable in backend.py with your API key:

python
Copy
Edit
api_key = "your_hugging_face_api_key"
Step 3: Run the Application 🚀
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
This will open the chatbot in your browser at http://localhost:8501.

How It Works 💡
User Interaction: The user types a query, and the chatbot responds based on predefined healthcare queries (e.g., "symptom", "appointment", "medication").
Text Generation: If the user's query doesn't match a predefined category, the chatbot uses the GPT-2 model to generate a general response.
UI Design: The UI is styled with custom CSS for a clean, modern look. Emojis are used to make the conversation more engaging.
File Structure 📁
bash
Copy
Edit
healthcare-chatbot/
│
├── app.py                  # Main application file
├── backend.py              # Backend logic (handles chatbot responses)
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
Dependencies 📜
streamlit: For building the web application.
transformers: For utilizing the Hugging Face model pipeline.
nltk: For text processing (tokenization and stopword handling).
You can also install the dependencies by running:

bash
Copy
Edit
pip install -r requirements.txt

Enhancements to UI 💅
Custom CSS: Enhanced button and input field styling for better user experience.
Emojis: Added emojis to buttons, messages, and responses to make it more interactive.
Engaging Design: The background color, fonts, and button shapes are styled to make the app look more modern and clean.
Contributions 🤝

Feel free to fork this project and submit pull requests for any improvements or bug fixes.
