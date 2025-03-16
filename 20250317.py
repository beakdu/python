#큰 따옴표 표시하는 방법: 작은 따옴표로 묶어주기
say= '"Python is very easy."he says'
print(say)
food = 'Python\'s favorite food is perl'
print(food)
say1 = "\"Python is very easy.\" he says."
print(say1)

N = int(input())
A =['int']

for i in range(N//4):
    A.insert(0, 'long')
    
print(' '.join(A))