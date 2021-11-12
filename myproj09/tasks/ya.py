import random

def check_available(received_text: str) -> bool:
    return received_text in ["야", "짱파카", "짱파카야"]


def make_response(received_text: str) -> str:
    answer = ["왜?", "도와줄까?", "궁금한거 있어?", "무슨일이야?"]
    return random.choice(answer)
