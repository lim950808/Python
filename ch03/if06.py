# 키보드로 입력한 점수(0 ~ 100)가 어느 학점에 해당하는지 구하는 프로그램
# 90~ A학점
# 80~ B학점
# 70~ C학점
# 60~ D학점
# 60점 미만 F학점

n = int(input('학점은?'))

if n >= 90:
    print('A학점')
elif n >= 80:
    print('B학점')
elif n >= 70:
    print('C학점')
elif n >= 60:
    print('D학점')
else:
    print('F학점')