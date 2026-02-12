from backend.core.config import GROQ_API_KEY, MODEL
from groq import Groq
import uuid
import json

client = Groq(api_key=GROQ_API_KEY)

# Sessões temporárias 
sessions = {}

def start_leveling(objective: str):
    session_id = str(uuid.uuid4())

    sessions[session_id] = {
        "objective": objective,
        "current_step": "writing",
        "writing_score": None,
        "reading_scores": [],
        "listening_scores": [],
        "reading_questions": [],
        "listening_questions": []
    }

    return session_id, {
        "step": "writing",
        "question": "Tell me about yourself and why you want to learn English."
    }

def evaluate_writing(session_id: str, answer: str):
    prompt = f"""
    You are an English proficiency evaluator.

    Analyze this student's text:

    "{answer}"

    Evaluate:
    - grammar (0-10)
    - vocabulary (0-10)
    - complexity (0-10)
    - coherence (0-10)

    Return JSON:
    {{
        "grammar": number,
        "vocabulary": number,
        "complexity": number,
        "coherence": number,
        "overall_score": average,
        "estimated_level": "Beginner | Intermediate | Advanced"
    }}
    Be strict but fair.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    result = json.loads(response.choices[0].message.content)

    sessions[session_id]["writing_score"] = result["overall_score"]
    sessions[session_id]["current_step"] = "reading"

    return result

def generate_reading(session_id: str):
    writing_score = sessions[session_id]["writing_score"]

    if writing_score <= 4:
        level = "Beginner"
    elif writing_score <= 7:
        level = "Intermediate"
    else:
        level = "Advanced"

    prompt = f"""
        Generate a short reading text for {level} level.
        Then generate 2 open comprehension questions.

        Return JSON:
        {{
            "text": "...",
            "questions": ["q1", "q2"]
        }}
        """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    result = json.loads(response.choices[0].message.content)

    sessions[session_id]["reading_questions"] = result["questions"]

    return result

def evaluate_reading_answer(session_id: str, answer: str):
    prompt = f"""
        Evaluate this answer for reading comprehension.
        Score from 0 to 10.

        Answer:
        "{answer}"

        Return JSON:
        {{
            "score": number
        }}
        """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    result = json.loads(response.choices[0].message.content)

    sessions[session_id]["reading_scores"].append(result["score"])

    return result