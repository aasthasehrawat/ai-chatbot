# NeoChat

This project is a real-time AI chatbot built using Flask, HTML, CSS, and JavaScript, leveraging the Google Gemini AI API for generating responses. The application features a modern UI with a chat interface similar to popular chatbots, complete with user-friendly features like saving and deleting chats.

## Features

- Real-time AI chat functionality
- Save and delete chat history
- Modern and responsive UI
- Side navigation with chat history and new chat creation
- Deployment ready for Render / Vercel

## Technologies Used

- Flask (Python)
- HTML, CSS, JavaScript
- Google Gemini AI API
- Render / Vercel for deployment

## Directory Structure

```text
project/
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   │   ├── ai_logo.png
│   │   └── user_logo.png
│   └── js/
│       └── scripts.js
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── vercel.json```

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Google Gemini AI API Key
- Render / Vercel account (for deployment)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/aasthasehrawat/NeoChat.git
    cd NeoChat
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the API key**:
    Replace `YOUR_API_KEY` in `app.py` with your actual Google Gemini AI API key:
    ```python
    genai.configure(api_key='YOUR_API_KEY')
    ```

4. **Run the application locally**:
    ```bash
    python app.py
    ```
    Open your browser at `http://127.0.0.1:5000`.

### File Descriptions

- **app.py**: Main Flask application file  
- **requirements.txt**: Project dependencies  
- **vercel.json**: Deployment configuration  
- **static/css/styles.css**: CSS styling  
- **static/js/scripts.js**: Frontend logic  
- **templates/index.html**: Main HTML interface  

## Deployment

1. **Push code to GitHub**:
    ```bash
    git add .
    git commit -m "Initial commit"
    git push origin main
    ```

2. **Log in to Render / Vercel** and import project  
3. **Configure project** (framework preset: Python)  
4. **Deploy** and get unique URL (e.g., `your-app-name.onrender.com`)  

## Usage

- **Send Messages**: Type in the input box and press Enter  
- **New Chat**: Click "New Chat" in the sidebar  
- **Delete Chat**: Click three dots next to a chat to delete  

## Contributing

Fork the repository, create a feature branch, and submit pull requests. Contributions are welcome.  

## Contact

**aasthasehrawat**  
Email: aasthasehrawat2@gmail.com  
GitHub: [https://github.com/aasthasehrawat](https://github.com/aasthasehrawat)
