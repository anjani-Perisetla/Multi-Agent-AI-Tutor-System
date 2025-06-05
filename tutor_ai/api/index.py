from fastapi import FastAPI
from tutor_ai.main import app as fastapi_app  # import your app

# Expose FastAPI app for Vercel
app = fastapi_app
