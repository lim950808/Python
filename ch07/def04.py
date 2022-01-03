# 1~n 까지 합을 구하는 프로그램
# 1~n 까지 합을 구해주는 함수 for - range
def sum(n):
    sum = 0
    for i in range(1, n + 1):       # 1~n 까지 loop가 돌아감
        sum = sum + i
    print('1~{}까지의 합={}'.format(n, sum))

# 함수 호출
sum(3)
sum(10)
sum(20)