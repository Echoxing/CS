
判断用户输入的年份是否为闰年

```python
n=int(input('请输入年份：'))
if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
    print('{0}是闰年'.format(n))
else:
    print('{0}不是闰年'.format(n))
```