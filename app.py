import streamlit as st
from backend import healthcare_chatbot
import nltk

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

# Add custom CSS to style the app
def add_custom_css():
    st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
        padding: 10px;
        font-size: 18px;
        border: 2px solid #4CAF50;
    }
    .stTextInput>div>div>input:focus {
        border-color: #45a049;
    }
    .stTextInput>div>label {
        font-size: 18px;
        color: #333;
    }
    .stWrite {
        font-size: 18px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Add custom CSS to make the app beautiful
    add_custom_css()

    # Set the title of the app
    st.title("Healthcare Assistant Chatbot 🤖")

    # Add a fun introduction message
    st.markdown("👩‍⚕️ **Welcome to the Healthcare Assistant Chatbot**. How can I assist you today?")

    # Create a container for user input and assistant response
    user_input = st.text_input("Type your message here 💬")

    # Submit button with an icon
    if st.button("Submit 🚀"):
        if user_input:
            st.write(f"User: {user_input} 😃")
            with st.spinner("Processing your query... ⏳"):
                # Call the backend function to get the chatbot response
                response = healthcare_chatbot(user_input)
            st.write(f"Healthcare Assistant: {response} 🩺")
        else:
            st.write("Please enter a message to get a response. ❌")

# Run the app
if __name__ == "__main__":
    main()
s