n = int(input())

# Please write your code here.

def f1(n):
    if n <= 0:
        return
    else:
        print("HelloWorld")
        f1(n-1)

f1(n)