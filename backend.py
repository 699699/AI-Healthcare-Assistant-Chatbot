from transformers import pipeline

# Set up the Hugging Face pipeline
api_key = "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"  # Replace with your Hugging Face API key
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    # Handle specific healthcare queries
    if "symptom" in user_input:
        return "Please consult a doctor for accurate results. 🏥"
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor? 📅"
    elif "medication" in user_input:
        return "It's important to take prescribed medications regularly. If you have concerns, consult a doctor. 💊"
    else:
        # If query doesn't match specific cases, generate a general response
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']
