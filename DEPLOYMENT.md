# Deployment Guide: Travel Insurance Multi-Agent System

## Local Deployment

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Environment Variables
- Create a `.env` file in the project root (if not already present).
- Add your API keys and secrets, e.g.:
```
GOOGLE_API_KEY=your_google_api_key
SECRET_KEY=your_secret_key
```

### 5. Run the ADK Web Server
```sh
adk web
```
- The ADK server will start at `http://localhost:8000` by default.

### 6. Run the Streamlit UI (in a new terminal)
```sh
streamlit run app1.py
```
- The UI will be available at `http://localhost:8501`.

---

## Streamlit Cloud Deployment

### 1. Push Your Code to GitHub
- Make sure your latest code is committed and pushed to your GitHub repository.

### 2. Prepare for Cloud Deployment
- Ensure your `requirements.txt` includes all dependencies (including `streamlit`, `google-adk`, etc.).
- Add a `.streamlit/secrets.toml` file for your API keys and secrets:

```toml
# .streamlit/secrets.toml
GOOGLE_API_KEY = "your_google_api_key"
SECRET_KEY = "your_secret_key"
```

### 3. Deploy on Streamlit Cloud
- Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
- Click **New app** and select your GitHub repo and branch.
- Set the main file to `app1.py`.
- In the app settings, add your secrets (or use the `secrets.toml` file).
- Click **Deploy**.

### 4. (Optional) ADK Server in the Cloud
- If you want to run the ADK server in the cloud, use a cloud VM (e.g., Google Cloud, AWS EC2) and follow the local deployment steps.
- Make sure to open the necessary ports (e.g., 8000 for ADK, 8501 for Streamlit).

---

## Troubleshooting
- **Missing dependencies:** Double-check your `requirements.txt`.
- **API key errors:** Ensure your keys are set in `.env` (local) or `secrets.toml` (cloud).
- **Port conflicts:** Make sure no other process is using ports 8000 or 8501.
- **Quota errors:** Check your Google API usage and upgrade if needed.

---

## Contact
For deployment support, see the main project documentation or contact the development team. 