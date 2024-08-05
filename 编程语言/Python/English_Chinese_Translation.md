# English Chinese Translation


## 项目需求

1. 在命令行窗口运行
2. 当程序运行时，会要求我们输入中文或者英文单词或者句子，然后程序会自动翻译成对应的英语或者中文
3. 当输入q字母，程序不再询问并结束

## Python编程知识点

- while循环
- 用户输入字符串
- 条件判断
- 字典数据
- http post请求
- requests 模块 (需要使用`pip install requests`安装)

## 参考代码

```python
import requests

url = 'https://fanyi.baidu.com/sug'

while True:
    text = input('请输入中文或者英语：').strip()
    if text == 'q':
        break

    data = {'kw': text}

    resp = requests.post(url, data)

    found = False
    if resp.status_code == 200:
        data = resp.json()
        if data['errno'] == 0:
            ds = data['data']
            for kv in ds:
                if kv['k'] == text:
                    found = True
                    print(kv['v'])
            if not found:
                print('没有找到')
        else:
            print(data)
    else:
        print(resp.content)

```

## 运行测试
将代码保存为2.py，然后在控制台运行：

```
python 2.py
```
## 代码的详细解释：

导入库：
```python
import requests
```
导入 requests 库，用于发送 HTTP 请求。

定义 URL：

```python
url = 'https://fanyi.baidu.com/sug'
```
定义百度翻译接口的 URL。

进入循环：
```python
while True:
    text = input('请输入中文或者英语：').strip()
    if text == 'q':
        break
```
使用 while True 进入一个无限循环，不断提示用户输入文本。输入的文本通过 strip() 方法去除两端的空白字符。如果用户输入 'q'，则退出循环。

构造数据：
```python
data = {'kw': text}
将用户输入的文本放入字典中，键为 'kw'。
```

发送 POST 请求：

```python
resp = requests.post(url, data)
```
使用 requests.post 方法发送 POST 请求到百度翻译接口，并将数据作为请求体传递。

检查响应状态码：
```python
found = False
if resp.status_code == 200:
    data = resp.json()
```
检查响应状态码是否为 200（表示请求成功）。如果成功，将响应数据解析为 JSON 格式。

处理响应数据：
```python
if data['errno'] == 0:
    ds = data['data']
    for kv in ds:
        if kv['k'] == text:
            found = True
            print(kv['v'])
    if not found:
        print('没有找到')
else:
    print(data)
```
检查响应数据中的 errno 是否为 0（表示没有错误）。如果没有错误，遍历 data 字段中的所有键值对。对于每个键值对，检查键是否与用户输入的文本相同，如果相同，设置 found 为 True 并打印对应的翻译值。如果遍历完成后 found 仍然为 False，则打印“没有找到”。如果 errno 不为 0，则打印整个响应数据。

处理错误响应：
```python
else:
    print(resp.content)
```
如果响应状态码不是 200，打印响应内容以显示错误信息。

总结：这个程序可以实现用户输入文本后，通过百度翻译接口获取翻译结果，并打印出来。如果找不到对应的翻译或出现错误，会给出相应的提示。
