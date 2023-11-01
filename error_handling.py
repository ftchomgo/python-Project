try:
    print(a)
except Exception as e:
    print(e)
else:
    print("me voici")
print("hello")


try:
    num=int(input('please enter a number '))
    print(num)
except Exception as e:
    print(e)