def print_square(x):
    print(x*x)

def get_square(x):
    return(x*x)

print_square(3)
get_square(3)
print(get_square(3))
#파이썬에서는 return값이 없으면 None이 리턴됨 그러면 함수 호출부분이 None으로 대채됨
print(print_square(3))

number = 10
day ='three'
print("I ate %d apples. so I was sick for %s days."%(number,day))

print(" I have %s apples."%3)
print("rate is %s."%3.245)