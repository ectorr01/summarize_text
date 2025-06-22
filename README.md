# 📝 Project Description
Automatic Text Summarizer with FastAPI and Hugging Face Transformers

This is a lightweight web application built with FastAPI that allows users to input text and automatically generate a summary using a pre-trained AI model from the Hugging Face Transformers library (sshleifer/distilbart-cnn-12-6).

The application includes:

 - A simple HTML form interface for text input.
 - Text processing using a summarization pipeline.
 - Display of the summarized result on a dedicated HTML page.
 - Basic error handling (e.g., empty input).
   
It's ideal for those who want to experiment with NLP (Natural Language Processing) models in a fast and interactive way, without complex dependencies or heavy frameworks.

## 💡 Technologies Used
  - FastAPI : Python framework for modern APIs and web applications.
  - Hugging Face Transformers : for using pre-trained AI models.
  - PyTorch : computation engine for AI models.
  - Jinja2 : template engine for dynamic HTML page generation.

## 🚀 Getting Started
Prerequisites
Make sure you have Python 3.8+ installed. You'll also need pip to install dependencies.

### Installation

  1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

  2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

  3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Run the Application

Start the FastAPI development server:
```bash
fastapi dev main.py
```

Then open your browser and go to:
```
http://localhost:8000
```

### How to Use

1. Enter a text in the form shown on the homepage.
2. Click on "Summarize".
3. The application will display a summarized version of the text.
