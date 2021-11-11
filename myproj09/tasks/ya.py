import random


def check_available(received_text: str) -> bool:
    question = ["야", "짱파카", "짱파카야", "짱파카봇아"]
    return received_text == question


def make_response(received_text: str) -> str:
    return random.format("왜?", "무슨일이야?", "궁금한거 있어?", "도와줄까?")
