#for.py
# 평균 & 총점

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score               # A학급의 점수를 모두 더한다.
    
average = total / len(A)         # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
print("평균->", average)          # 평균 79.0 출력
print("총점->", total)            # 평균 790 출력