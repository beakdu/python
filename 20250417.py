#불린: 따옴표를 사용하면 문자이므로 따옴표 없이 사용
print(True)
print(False)
#and은 둘다 True인경우만 True
print(True and True)
print(True and False)
print(False and True)
print(False and False)
#or은 하나라도 True면 True로 나옴
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not은 반대로 나옴
print(not True)
print(not False)

print(2 >1)
print(2 <1)
print(3 >=2)
print( 3<=3)
print(2==2)
print(2 !=2)

#문자열도 비교
print("Hello" == "Hello")
print("Hello" != "Hello")

print(2>1 and "Hello"=="Hello") #True and True

print(not not True) # not False
print(not not False) #not True

print( 7==7 or (4<3 and 12>10)) #True or False

x=3
print(x>4 or not (x<2 or x==3)) #False or False