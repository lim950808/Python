kk = [1,2,3,['a','b','c']]
print("kk->", kk)
print("kk[-1][1]->", kk[-1][1])

kk[1] = 7               # list는 숫자가 변할 수 있지만 tuple은 불가능
print("kk->", kk)