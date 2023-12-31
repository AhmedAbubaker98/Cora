**This project is still under development and is updated regularly, expect bugs, expect them to get fixed soon as well**

**This project creates a Streamlit app that provides a conversational interface to interact with a large language model called Cora. Cora is designed to offer personalized guidance and support to leaders, helping them navigate challenges, develop their skills, and foster innovative and inclusive workplaces.**

**Key Features:**

- **Personalized leadership advice:**
    - Provides tailored recommendations based on the user's specific challenges and goals.
    - Suggests coaching tips, development resources, and action plans.
- **Contextual conversation:**
    - Maintains ongoing conversation history for context-aware responses.
    - Refers to previous discussions for consistency and personalization.
- **Diverse virtual brainstorming:**
    - Facilitates idea generation and challenges biases through virtual collaborators.
- **Continuous learning:**
    - Evolves and improves over time based on user interactions.

**Technical Components:**

- **Streamlit:** Creates a user-friendly web interface for interacting with Cora.
- **Google's Generative AI API:** Powers Cora's conversation and response generation using the Gemini-Pro language model.
- **Python:** Implements core functionality, including:
    - Conversation history management
    - User input handling
    - Model response generation
- **External API Key:** Requires a Google API key to access the Generative AI API.

**Setup and Usage:**

1. **Install dependencies:**
   ```bash
   pip install streamlit google-generativeai
   ```
2. **Obtain a Google API key:**
   - Follow instructions to create a Google Cloud project and enable the Generative AI API.
   - Set the API key as an environment variable named `GOOGLE_API_KEY`.
3. **Run the app:**
   ```bash
   python -m streamlit run your_app_file.py
   ```

**Interacting with Cora:**

1. Access the app in your web browser.
2. Type your messages and press "Send" to initiate conversations with Cora.
3. Engage in ongoing dialogue, exploring various leadership topics and seeking guidance.

**Additional Information:**

- **Conversation History:** Stored in `conversation_history.txt` for context and continuity.
- **Initial Message:** Written to the history file if it's empty, providing Cora's introduction.
- **API Flexibility:** Code includes commented sections for using OpenAI's API as an alternative.
