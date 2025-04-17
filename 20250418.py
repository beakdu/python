while True:
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    print(a+b)

print(type(3))
print(type(3.0))
print(type("3"))
print(type("True"))
print(type(True))

def hello():
    print("Hello World")

print(type(hello))
print(type(print))