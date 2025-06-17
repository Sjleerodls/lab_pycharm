def plus(x, y):
    """
    두 숫자의 합 x + y를 리턴
    :param x: 숫자(int, float)
    :param y: 숫자(int, float)
    :return: x + y
    """
    return x + y

# print('plus.py __name__ =', __name__)

# myutil.plus
if __name__ == '__main__':      # 각 모듈은 기본적으로 __name__에 __main__을 저장하고 있음.
                                # 하지만 해당 모듈을 다른곳에서 import 할 경우 호출한 이름으로 변경됨. (myutil.plus)
                                # 따라서 print문이 실행되지 않음 (if문 부적합)
    print(plus(1, 2))       # 단독으로 해당 스크립트 실행 시 테스트 가능.

# print(plus(1, 2))   # positional argument를 자동으로 pycharm은 보여줌.

"""
모듈: 파일(*.py)
패키지 : 폴더(__init__.py)
"""

"""
print(plus.__dir__())     # 객체가 어떤 속성 이름들을 갖고 있는지 문자열 리스트로 반환.
print(dir(plus))          # ""
print(getattr(plus, '__name__'))    # 그 중 하나의 실제 속성값을 가져옴
"""