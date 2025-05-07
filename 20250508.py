#return문의 역할: 돌려주기, 함수종료하기
def square(x):
    return(x*x)

print(square(3))

def square(x):
    print("함수 시작")
    return x*x
    print("함수 끝")

print(square(3))
print("Hello World!")

print("I eat %d apples."%3)
print("I eat %s apples."%"five")

number =3
print("I eat %d apples."%number)