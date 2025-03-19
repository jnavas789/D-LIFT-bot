# Secure PDF Chatbot

This is a simple Streamlit application that allows you to interact with your PDF documents through a chatbot interface while maintaining control over your intellectual property.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository to your local machine**

2. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

3. **Prepare your document summaries:**
   - Create text files named `policy_review_summary.txt` and `agroecology_report_summary.txt` containing the summaries of your PDF documents
   - Place these files in the same directory as the application

4. **Set up environment variables:**
   - Create a file named `.env` in the same directory
   - Add the following line to the file:
     ```
     ADMIN_PASSWORD=your_secure_password
     ```
   - Replace `your_secure_password` with a password of your choice

### Running the Application Locally

Run the following command in your terminal:
```
streamlit run streamlit_pdf_chatbot.py
```

This will start the application and open it in your default web browser. You'll need to enter the password you set in the `.env` file to access the chatbot.

### Deploying to Streamlit Community Cloud

1. **Create a GitHub repository and push your code:**
   - Create a new repository on GitHub
   - Push your code to the repository

2. **Sign up for Streamlit Community Cloud:**
   - Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account

3. **Deploy your app:**
   - Click "New app"
   - Select your repository, branch, and the main file (`streamlit_pdf_chatbot.py`)
   - Click "Deploy"

4. **Set up secrets:**
   - In your app's settings, go to "Secrets"
   - Add your password:
     ```
     ADMIN_PASSWORD=your_secure_password
     ```

Your app will now be accessible online with password protection.

## Usage

1. Enter the password in the sidebar to access the chatbot
2. Type your query in the text input field
3. Click "Submit Query" to get a response based on your PDF documents

## Security Considerations

- Keep your `.env` file secure and never commit it to public repositories
- For additional security, consider hosting on a private server or using a VPN
- Regularly update your password

