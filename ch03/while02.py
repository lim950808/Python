# 1 ~ 10 까지 합을 구하는 while 프로그램

i = 1
sum = 0

while i <= 10:
    sum = sum + i
    print('1~{}까지의 합={}'.format(i, sum))
    i = i + 1