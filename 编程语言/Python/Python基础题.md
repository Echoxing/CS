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
# 求区间内的偶数
```python
def oushu(n1,n2):
    result=[]
    for i in range(n1,n2+1):
        if i%2==0:
            result.append(i)
    return(result)

n1=int(input())
n2=int(input())
print(oushu(n1,n2))
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

# 求圆的面积
```python
import math
radius=int (input("请输入圆的半径"))

area=math.pi*radius**2
print(area)
```

# 数据类型
## 计算列表数字和
```python
def sum_list(li):
    total = 0
    for i in li:
        total += i
    return total

# li=list(input())input() 直接将输入作为字符串处理，导致 list(input()) 会将字符串拆分成字符列表。
# sum_list 函数和内置的 sum 函数都期望输入是数值列表，而字符列表不能直接进行求和。
# 输入一个由空格分隔的数字字符串并转化为整数列表
li = list(map(int, input("请输入一组数字（空格分隔）：").split()))
print("输出列表和：%s"% sum_list(li))
print(sum(li))
```

## 从列表中移除多个元素
```python
li = list(input("Enter the main list of characters: "))
move = input("Enter the characters to remove: ")
for i in move:
    li.remove(i)
print(li)
```
