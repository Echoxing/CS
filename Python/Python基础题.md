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
