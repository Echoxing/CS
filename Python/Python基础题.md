# 两数之和
```python
a=int(input())
b=int(input())
print('a+b=',a+b)
```

# 判断用户输入的年份是否为闰年

闰年：400的倍数；是4的倍数且不是100的倍数

```python
n=int(input('请输入年份：'))
if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
    print('{0}是闰年'.format(n))
else:
    print('{0}不是闰年'.format(n))
```

# 数字的阶乘
```python
n=int(input())
count=1
for i in range(1,n+1):
    count = count*i
print(count)
```

# 求区间内的素数
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def demo(a,b):
    result=[]
    for i in range(a,b+1):
        if is_prime(i):
            result.append(i)
    return result

a=int(input())
b=int(input())
print(demo(a,b))
```
# 求前n个数的平方和
```python
def square(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i*i
    return sum

a=int(input())
print(square(a))
```