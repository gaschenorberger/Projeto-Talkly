from pydantic import BaseModel
from typing import Optional

class StartLevelingRequest(BaseModel):
    objective: str  # Qual objeto para aprender inglês? (Trabalho, estudo, viagem...)

class AnswerRequest(BaseModel):
    session_id: str
    answer: str

class QuestionResponse(BaseModel):
    session_id: str
    question: str
    question_number: int

class AnswerResponse(BaseModel):
    feedback: str
    next_question: Optional[str] = None
    finished = bool
    final_level: Optional[str] = None