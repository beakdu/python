a = "Life is too short,You need Python"
print(a[3])
print(a[0])
print(a[12])
print(a[-1])
print(a[-0])
print(a[-2])
print(a[-5])

n = int(input())

for i in range(1,n+1):
    print("*"*i)

# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 9
print("오늘은 "+ str(year)+"년 "+str(month)+"월 "+str(day)+"일입니다")
#입력할 부분을 {}로 표시하고, 마지막에 .format()안에 순서대로 표시
print("오늘은 {}년 {}월 {}일입니다.".format(year,month,day))
#문자열은 변수에 넣고 format메소드를 써도 됨
day_string ="오늘은 {}년 {}월 {}일입니다."
print(day_string.format(year,month,day))
#다음날을 출력하고 싶은 경우
print(day_string.format(year,month, day+1))