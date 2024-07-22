# chatbot

Greenedesk Swim School Chatbot
This repository contains the code and resources for a Streamlit-based chatbot application that answers questions related to swim schools. The chatbot is powered by OpenAI's GPT-3.5 language model and utilizes the LangChain library for efficient information retrieval and generation.
Project Structure

The project follows a modular structure with separate files for the main application logic and utility functions:

•	app.py: This file contains the main application logic, including the Streamlit user interface, handling user input (text and speech), and displaying the chatbot's responses.

•	utils.py: This file contains utility functions for creating the vector store, setting up the conversational retrieval chain, performing text-to-speech and speech-to-text conversions, and other helper functions.

Additionally, the repository contains the following files and directories:

•	pdf files: This directory contains the PDF files that the chatbot was trained on. These files are related to swim schools, their programs, and other relevant information.

•	Requirements.txt: This file lists all the Python libraries and packages required to run the chatbot application.

Getting Started

To run the chatbot application locally, follow these steps:
1.	Clone the repository:

		git clone https://github.com/your-username/swim-school-chatbot.git

2.	Install the required dependencies:

		pip install -r requirements.txt

3.	Set up your OpenAI API key: 
•	Create a .env file in the project root directory.
•	Add your OpenAI API key to the .env file: openai_api_key=YOUR_API_KEY_HERE
4.	Run the Streamlit application:
streamlit run app.py

The chatbot will now be accessible in your local Streamlit instance.
Usage
The chatbot application provides a user-friendly interface for interacting with the swim school chatbot. Users can input their questions or queries in the text field or use the microphone for speech input.
The chatbot will retrieve relevant information from the vector store (created from the PDF files) and generate a response based on the user's input and the conversation history. The response will be displayed in the chat window, and users can continue the conversation by providing additional input.

Additionally, the chatbot supports text-to-speech functionality, allowing users to hear the generated responses in audio format.

Notes
•	The chatbot's responses are based on the information contained in the provided PDF files. The quality and accuracy of the responses may vary depending on the comprehensiveness and relevance of the training data.
•	The project utilizes various Python libraries, including OpenAI, LangChain, Streamlit, and others. Make sure to install the required dependencies listed in the requirements.txt file.

•	The OpenAI API key is required to use the GPT-3.5 language model and other OpenAI services. Make sure to set up your API key correctly in the .env file.

•	The project is configured to use the gpt-3.5-turbo-1106 model from OpenAI. You can modify the model settings in the get_conversation_chain function in “utils.py” if needed.

•	The project includes functionality for text formatting and displaying metadata information (source files) along with the chatbot's responses.

Contributing
If you'd like to contribute to this project, please follow these steps:
1.	Fork the repository.
2.	Create a new branch for your feature or bug fix: git checkout -b my-new-feature
3.	Make your changes and commit them: git commit -am 'Add some feature'
4.	Push to the branch: git push origin my-new-feature
5.	Submit a pull request describing your changes.

License
This project is licensed under the MIT License.

Acknowledgements

This chatbot application was developed using the following libraries and resources:

•	OpenAI: For the GPT-3.5 language model and related services.

•	LangChain: For efficient information retrieval and generation.

•	Streamlit: For building the user interface and deploying the application.

•	PyPDF2: For loading and parsing PDF files.

•	FAISS: For efficient vector similarity search.

Please refer to the respective library documentation and licenses for more information.

