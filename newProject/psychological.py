# 심리게임
# https://gajokstory.com/1036

totalScore = 0

def q1():
    question1 = input("하루 중에서 기분이 가장 좋을 때는? >> ")
    # 라디오 박스 체크
    answer1Dict = {"아침": 2, "오후나 늦은 저녁": 4, "늦은 밤": 6}

    if question1 not in answer1Dict:
        print(answer1Dict[0])
    #
    # if question1 == answer1Dict[0]:
    #     totalScore += answer1Dict[0]