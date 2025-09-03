# NeoChat

This project is a real-time AI chatbot built using Flask, HTML, CSS, and JavaScript, leveraging the Google Gemini AI API for generating responses. The application features a modern UI with a chat interface similar to popular chatbots, complete with user-friendly features like saving and deleting chats.

## Features

- Real-time AI chat functionality
- Save and delete chat history
- Modern and responsive UI
- Side navigation with chat history and new chat creation
- Deployment ready for Render (or any cloud platform)

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
└── vercel.json



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
    Replace the `YOUR_API_KEY` in `app.py` with your actual Google Gemini AI API key.
    ```python
    genai.configure(api_key='YOUR_API_KEY')
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```
    The app will be available at `http://127.0.0.1:5000`.

### File Descriptions

- **app.py**: The main Flask application file.
- **requirements.txt**: Contains all the dependencies required for the project.
- **vercel.json**: Configuration file for deploying the app on Vercel/Render.
- **static/css/styles.css**: CSS file for styling the application.
- **static/js/scripts.js**: JavaScript file for handling the frontend logic.
- **templates/index.html**: HTML file for the application's main interface.

## Deployment

To deploy the application on Render or Vercel, follow these steps:

1. **Push your code to GitHub**:
    ```bash
    git add .
    git commit -m "Initial commit"
    git push origin main
    ```

2. **Log in to Render / Vercel**: Create an account if you don't have one.

3. **Import Project**:
   - Click on "New Project" or "Import Project" from your dashboard.
   - Connect your GitHub account if you haven't already.
   - Select the repository where your Flask app is hosted.

4. **Configure Project**:
   - Ensure the framework preset is set to “Python” or that the platform detects the `vercel.json`/`render.yaml` file.

5. **Deploy**:
   - Click on "Deploy" to start the deployment process.
   - Monitor the build logs and deployment status.

6. **Access Your App**: Once deployed, the platform provides a unique URL for your application (e.g., `your-app-name.onrender.com`).

## Usage

- **Send Messages**: Type your message in the input box and press Enter to send. The AI response will appear in the chat area.
- **New Chat**: Click on "New Chat" in the sidebar to start a new conversation.
- **Delete Chat**: Click on the three dots next to a chat in the sidebar to delete it. A confirmation popup will appear.

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Contact

For any inquiries or feedback, feel free to contact **aasthasehrawat**  
Email: aasthasehrawat2@gmail.com
