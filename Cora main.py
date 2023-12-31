import streamlit as st
import os
from openai import OpenAI
import google.generativeai as genai

# Load your API key (using a preferred method)
client = OpenAI(api_key="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")
genai.configure(api_key="AIzaSyD9Kq0Ic_vRgqn198zIDEVG7Mf1IxPH7xg")

# Initial message to set the model's perspective
initial_message = """ You are a chatbot/conversational AI tool named Cora
that provides leaders with a personalized interface to access case studies, best practices, and innovative solutions based on their specific challenges and workforce demographics. You analyze leadership styles and suggest coaching tips, development resources, and personalized action plans. Facilitate virtual brainstorming sessions with diverse virtual collaborators to generate new ideas and challenge pre-existing biases, you are concise and to the point without talking to much unless asked to.

your first message will be as follows: "

Hey there! I'm Cora, your personalized leadership companion. Think of me as your AI co-pilot, here to navigate the ever-changing leadership landscape with you.

Tell me, what's the biggest challenge you're facing right now as a leader? Is it keeping your team motivated, driving innovation, or fostering a truly inclusive environment?

Understanding your unique needs and goals is key to how I can help. So, don't hold back; the more you share, the better I can tailor my support.

Here's a glimpse of what I can do for you:

Uncover best practices and case studies relevant to your specific challenges and workforce demographics. Analyze your leadership style and suggest personalized coaching tips, development resources, and action plans. Spark creativity and challenge biases through virtual brainstorming sessions with diverse virtual collaborators. Become your learning buddy, constantly evolving and learning from your interactions to provide even more relevant support over time. ** So, ready to chart your course to leadership success? Let's talk! **  "
"""

# Send the initial message to the model
chat_completion = client.chat.completions.create(
    messages=[{'role': 'user', 'content': initial_message}],
    model="gpt-3.5-turbo"  # Adjust model as needed
)

# Extract and store the model's initial response
initial_model_response = chat_completion.choices[0].message.content.strip()

# Create the Streamlit app
st.title("Cora: Your Personalized Leadership Companion")

# Container for chat messages
chat_container = st.container()

def display_chat_message(message, is_user_message):
    with chat_container:
        bubble_style = ""
        color = "black"  # Default color
        if is_user_message:
            bubble_style = "background-color: #30353D; padding: 10px; border-radius: 10px; margin-bottom: 10px;"
            color = "#E5E5EA"  # Adjust as desired
        else:
            bubble_style = "background-color: #3A4047; padding: 10px; border-radius: 10px; margin-bottom: 10px;"
            color = "#F2F2F2"  # Adjust as desired
        st.markdown(f"""<div style="{bubble_style}; color:{color}">{message}</div>""", unsafe_allow_html=True)

# Display the initial message from Cora
display_chat_message(initial_model_response, is_user_message=False)

# Input field for sending messages
user_input = st.text_input("You:", key="user_input", help="Type your message then click send.")

if st.button("Send"):
    
    display_chat_message(user_input, is_user_message=True)
    
    # Append user input to the conversation history
    prompt = f"User: {user_input}"
    
    #GOOGLE CODE

    model = genai.GenerativeModel('gemini-pro')    
    model_response = model.generate_content(user_input)
    display_chat_message(model_response.text, is_user_message=True)


    # # OPENAI CODE

    # # Send the prompt to the model for completion
    # chat_completion = client.chat.completions.create(
    #     messages=[{'role': 'user', 'content': prompt}],
    #     model="gpt-3.5-turbo"
    #)

    # Extract the model's response
    #model_response = chat_completion.choices[0].message.content.strip()

    # Update the initial_model_response for the next turn
    display_chat_message(model_response, is_user_message=False)