head = 'Python'
tail = "is fun!"
print(head + tail)
a = "python"
print(a*2)
print("=" * 50)
print("Py Program")
print("=" * 50)


n = int(input())  # 숫자 입력을 받음
for i in range(1, n + 1):
    A, B = map(int, input().split())  # 두 개의 숫자 입력을 받음
    print(f'Case #{i}: {A} + {B} = {A + B}')   
