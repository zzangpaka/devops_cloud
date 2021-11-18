quotes = {
    "Moe": "A wise guy, huh?",
    "Larry": "Ow!",
    "Curly": "Nyuk nyuk!",
}
stooge = "Curly"
print(stooge, "says:", quotes[stooge])

# stooge = "Curly" 라고 지정하면서 quotes의 "이름" 부분은 stooge로 지정된것인가?
# 그래서 quotes[stooge]라고 했을때 "누군가"의 "말" 부분만 따로 출력이 되나?
# 척 보고 든 생각은 Curly says: Curly: Nyuk nyuk 으로 나오는 거 아닌가? 였기 때문에 의문!
# stooge를 지정하지 않았을 때 : Curly says: {'Moe': 'A wise guy, huh?', 'Larry': 'Ow!', 'Curly': 'Nyuk nyuk!'} 라고 출력
# stooge[quotes]로는 안되나 해봤을 때 : int 타입은 dict 안에 들어가야한다 즉 위치가 바뀌었다는 오류로 추정됨.
# 책에 나온 구문대로 적은 결과 : 깔끔하게 Curly says: Nyuk nyuk! 이라고 나옴.
