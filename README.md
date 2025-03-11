# JARVIS - Your Personal AI Assistant

Welcome to JARVIS! This is a simple yet powerful virtual assistant created with Python that can listen to your voice commands, generate responses using AI, and help you with tasks like opening websites or launching programs. Whether you want to browse YouTube, access your files, or have a friendly chat with your assistant, JARVIS has got you covered.

## Features
- **Voice Commands**: Talk to JARVIS and it will listen to your instructions.
- **Text-to-Speech**: JARVIS can speak back to you, making interactions feel more natural.
- **AI-Powered Conversations**: Using Google's Generative AI, JARVIS can respond intelligently to your queries.
- **Web Browsing**: Open websites like YouTube or ChatGPT with a simple command.
- **Folder Navigation**: Open local files or folders directly from your voice command.
- **Exit Command**: When you're done, simply say "Stop JARVIS" to end the session.

## Prerequisites
Before getting started, you'll need to have the following installed on your computer:

- Python 3.x (You can download it from [here](https://www.python.org/downloads/))
- Dependencies:
  - `speechrecognition`
  - `pyttsx3` (for text-to-speech)
  - `pywin32` (for using the Windows Speech API)
  - `google-generativeai` (for AI responses)
  - `python-dotenv` (for loading environment variables securely)

Install the dependencies by running:

```bash
pip install speechrecognition pyttsx3 pywin32 google-generativeai python-dotenv
```

## Setup
1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai
```

2. Create a `.env` file in the root directory of your project. In this file, add your Google Generative AI API Key like this:

```ini
GenaiAPIKey=your_api_key_here
```

3. Make sure your microphone is set up and working properly, as the assistant relies on it for voice recognition.

## Running JARVIS
Once everything is set up, you can start JARVIS by running the following command:

```bash
python jarvis.py
```

JARVIS will greet you and begin listening for your commands. Try saying something like "Open YouTube" or "Chat with me," and see what happens!

## Example Commands
Here are a few things you can ask JARVIS to do:
- "Open YouTube"
- "Open ChatGPT"
- "Launch Steam"
- "Stop JARVIS"

Feel free to add more commands or modify the existing ones to fit your needs!

## Notes
- The paths to your local files and programs may need to be updated based on your system's configuration.
- The AI responses are powered by Google's Gemini model.
- This assistant is built for Windows. It uses `win32com.client` for the text-to-speech functionality, so it might not work on non-Windows systems without modifications.

## License
This project is open-source. Feel free to contribute, report issues, or improve the project however you like!
