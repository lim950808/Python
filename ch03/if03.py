# 키보드로 입력받은 값이 홀수, 짝수인지
n = int(input('정수를 입력하세요?'))

if n % 2 == 0:
    print(n, '는 짝수입니다.')
else:
    print(n, '는 홀수입니다.')