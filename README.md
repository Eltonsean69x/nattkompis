# Nattkompis 🌙 — Swedish prototype

A small Streamlit proof of concept for new mums who are awake with their babies at night.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL Streamlit prints (usually http://localhost:8501).

## Share a link with your wife

1. Put `app.py` and `requirements.txt` in a GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a new app, select the repository, and choose `app.py` as the entry point.
4. Deploy and send her the public app URL.

This demo has **no shared live users, real online counts, authentication, persistent chat, or storage**. Chat messages and ping state exist only in a visitor's own browser session. The numbers and sample messages are fictional and labeled as demo content.

For a production app, plan privacy/GDPR, secure login, safeguarding, moderation, reporting/blocking, and a shared database.
