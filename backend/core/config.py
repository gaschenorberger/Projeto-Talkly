# backend/core/config.py

import os


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama-3.1-8b-instant"
TEMPERATURE = 0.7
MAX_TOKENS = 300