def check_available(received_text: str) -> bool:
    return received_text in ["응급상황", "긴급상황", "대사관 번호", "영사관"]


def make_response(received_text: str) -> str:
    return """여기서 재외 공관 정보를 검색해봐!
    https://consul.mofa.go.kr/
    """
