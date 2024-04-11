---
title: Python爬虫
date: 2022-12-22 12:02:43
tags:
    - CS
    - Python
    - 爬虫
categories: Python
---

**网络爬虫的第一步就是根据URL，获取网页的HTML信息。**在Python3中，可以使用**urllib.request**和**requests**进行网页爬取。

1. urllib库是python内置的，无需我们额外安装，只要安装了Python就可以使用这个库。
2. requests库是第三方库，需要我们自己安装。

API（Application Programming Interface）即应用程序接口。可以理解成一个地方，那里有整理得非常好的、供人随意调用的资源。

python爬虫中通常提到的API一般有两种情况：数据API和库的API。

库的API
库的API很好理解，就是一个人写了一个python库，他要找一个地方告诉你库里的每个函数接什么样的参数，一个对象可以调用什么样的方法，这个地方可以称为API。它其实是开发者和使用者之间的一个桥梁，一个接口。

数据API
这种形式的API一般是前端和后端的桥梁。后端计算出结果或者要展示什么数据，就设计一个数据接口(API)，前端人员调用这个接口，即可获取数据，将数据展示到页面上。这种API的设计是很有讲究的，设计一个方便易用、易于维护的接口，对前后端工作人员的协作是非常有帮助的。

这种API一般以URL形式存在，有些API不仅在网站内部使用，而且也向外界提供，我们可以通过访问这些URL来获取数据。

假设一个场景，比如我要做一个app，每天展示知乎上被浏览数量最多的几个回答，再拿一些数据做图表等。这时我需要拿到知乎的数据进行分析再展示。如何拿到数据呢？我可以用爬虫去全网爬，但是这样不仅耗时耗力，而且对知乎服务器会造成比较大的压力。如果知乎给我提供一个API，里面整齐地放着我想要的数据，那么我就可以更方便地获取数据，同时知乎服务器压力也会小很多。如果另一个人也有了一个idea，想做另一个关于知乎的app，他也要获得数据，他也可以用这同一个API。甚至知乎网站上展示的页面中的信息也可以是从API中调用的。所以这样一个数据接口就可以供多方使用，非常方便且多方获益，很多网站都会提供。

通常来说，如果网站提供了API，我们就不要去抓他们的HTML代码了，应该直接接入他们的API获取数据。这样做既减轻了他们的服务器压力，也让我们免去解析他们网页的繁杂工作。

读者可以再自己试试访问这两个URL

```python
https://github.com/python/cpython
https://api.github.com/repos/python/cpython
```
一个是项目地址，一个是该项目的API，API中会将这个项目的信息整合成json的形式供开发者调用

# 示例

下面我们使用github的API做一个实际的东西：抓取fork[这个项目](https://link.zhihu.com/?target=https%3A//github.com/python/cpython)的所有5千多个项目的star数

我们可以从[这个页面](https://link.zhihu.com/?target=https%3A//github.com/python/cpython/network/members)中查看fork的项目，但是只会展示1000个，要获取所有的项目，并找到star数最多的几个项目，就可以通过接入api来实现

在这个URL中

```text
https://api.github.com/repos/python/cpython
```

可以找到

```text
"forks_url": "https://api.github.com/repos/python/cpython/forks"
```

请求一下这个URL看能获得什么数据

```python3
import requests
r = requests.get('https://api.github.com/repos/python/cpython/forks')
data = r.json()
print(len(data))
# 30
```

得到的是一个list，每一个元素都是一个大dict，其中一个如下所示

![img](https://pic4.zhimg.com/80/v2-900fce8c5e8a59c3a3e986ed8ffaef47_1440w.webp)

其中stargazers_count就是该项目被star的次数

这次访问只能获取30个数据，如何获取5千多条数据呢？这就需要了解如何使用这个API了，需要到[帮助页面](https://link.zhihu.com/?target=https%3A//developer.github.com/v3/)中ctrl+F搜索page，可以看到下面这个页面

![img](https://pic2.zhimg.com/80/v2-f04a98bd476413f76de0ea67c55a95cd_1440w.webp)

我们猜测可以通过构造URL如下进行翻页

```text
https://api.github.com/repos/python/cpython/forks?page=10
```

发现这样做是可以的，接下来我们遍历1-171页抓取5千多个项目的名称、URL地址和star数，按照star的多少存到json文件中，并计算程序运行时间。

代码如下

```python3
import requests
import operator
import json
import time

def start_requests(url):
    print('getting', url)
    return requests.get(url, auth = ('你的邮箱', '你的github密码'))

def get_info(rep):
    data = rep.json()
    for datai in data:
        yield {
            'project_name': datai['full_name'],
            'project_url': datai['html_url'],
            'project_api_url': datai['url'],
            'star_count': datai['stargazers_count']
        }

def get_all():
    baseurl = 'https://api.github.com/repos/python/cpython/forks?page={}'
    for i in range(1, 171+1):
        url = baseurl.format(i)
        r = start_requests(url)
        yield from get_info(r)

def main():
    start = time.time()
    data = list(get_all())
    data.sort(key=operator.itemgetter('star_count'), reverse=True)
    s = json.dumps(data, ensure_ascii=False, indent=4)
    with open('github.json', 'w', encoding='utf-8') as f:
        f.write(s)
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
```

程序运行了333秒，得到json数据如下所示

![img](https://pic1.zhimg.com/80/v2-bab9031f0f56b41b88366d550077d748_1440w.webp)

其中start_requests函数中，传入了auth参数，里面读者要自己**修改成自己的github登录邮箱和密码**。如果没有的话，把auth参数去掉程序也可以运行，只是可能在没抓取完全部页面，就会被github封掉。如果不想注册一个账号，也不想被封掉，那就设置time.sleep降低抓取速度吧。

关于github上的抓取速度限制，可以看[官网上的说明](https://link.zhihu.com/?target=https%3A//developer.github.com/v3/%23rate-limiting)

从抓取到的数据可以看出，几乎所有fork去的项目star都是0，超过5的也只有1个。

有了这个例子，读者们就可以自己去想一想可以从github上爬点什么好玩的了。

## **httpbin**

[httpbin网站](https://link.zhihu.com/?target=https%3A//httpbin.org/)是requests库作者写的一个请求测试网站，通过请求这个网站的API可以返回当前请求携带的信息。当我们想知道自己请求时携带的信息时，可以通过请求这个网站的一些API获知。

[上一篇文章](https://zhuanlan.zhihu.com/p/36207770)中我就用它来测试请求时携带的IP是什么。

可以看到它的界面如下

![img](https://pic4.zhimg.com/80/v2-76f7d20690e46e6bf5e8c8fe4a6f1ddb_1440w.webp)

其中的ip user-agent等点进去都表示的浏览器请求时使用的ip user-agent等

你也可以用它来测试你的代码使用的是什么user-agent

```text
>>> import requests
>>> r = requests.get('https://httpbin.org/user-agent')
>>> r.json()
{'user-agent': 'python-requests/2.18.4'}
```

同时还可以用这个网站测试post请求（这是浏览器无法做到的，下面这个URL直接在浏览器中是打不开的）

```text
>>> import requests
>>> r = requests.post('https://httpbin.org/post',
...                   data = {'content': 'anything'})
>>> print(r.text)
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "content": "anything"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "upgrade",
    "Content-Length": "16",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.4"
  },
  "json": null,
  "origin": "59.77.43.118",
  "url": "https://httpbin.org/post"
}
```

我们平时使用浏览器访问的都是get请求，而对于post请求，需要请求时额外提供一些信息（data参数中），就无法通过浏览器达成。

## **其他API**

如果你想要爬一个网页

- 可以先去百度搜这个网页的API，如果有的话，就去读它API的说明，从API中抓取数据
- 如果没有对外开放的API，则到网页中，右键-检查-network，看有没有API文件（一般动态加载网页都会有）
- 实在没有再实打实去解析网页

如果想找一些API练手，可以看知乎上的[这个回答](https://www.zhihu.com/question/39479153)

一些API比如豆瓣、新浪微博，都会有一些限制，它们都默认你是要做一个应用才来申请的API，所以你需要假装真的要做一个应用。

假装创建一个应用以使用新浪微博的API的操作步骤可以看[这篇文章](https://link.zhihu.com/?target=https%3A//segmentfault.com/a/1190000012548487)，亲测有效。通过这个步骤获得token，用文章后面的代码就可以使用新浪微博的API调用数据了。访问哪些API可以看[新浪微博的开发者官网](https://link.zhihu.com/?target=http%3A//open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI)，只要按照要求构造URL，在限制范围内访问，即可获得想要的数据。

作者：Dwzb
链接：https://zhuanlan.zhihu.com/p/35324806
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



## **总结**

当我们要爬一个网页的时候，只需要如下流程

- 导入两个库，一个用于请求，一个用于网页解析
- 请求网页，获得源代码
- 初始化soup对象，使其可以调用更简单易用的方法
- 用浏览器打开网页，右键-检查，使用那个鼠标定位你要找的资源的位置
- 分析那个位置的源代码，找到合适的用于定位的标签及属性
- 编写解析代码，获得想要的资源

现在，对于一些没有丝毫反爬措施的网站我们都可以游刃有余了。至于抓取多个字段的数据如何组织在一起、抓取多页（URL有规律的情况下）的代码如何设计，就不是爬虫知识范畴了，这是用python基础知识就可以解决的。下一系列文章就主要讲这一部分。接下来给几个当前可以练手的网站

- CSDN首页除了标题之外的其他信息，比如作者名、发布的时间等，可以存储到一个以字典为元素的list里
- 豆瓣top250的信息，会翻页的话250个电影的信息可以直接一个循环抓取下来，其实找到规律构造出10个URL即可
- stackoverflow 简书 伯乐在线 等等网站都可以拿来练手

如果使用BeautifulSoup的定位的过程中遇到困难，可以直接到网上搜教程，也可以等我们这个专题后面更新的BeautifulSoup详细介绍。

如果你去抓取其他网站，最好先看一下`r.text`是不是和网站源代码一模一样，如果不是，说明你对方服务器没有把真正的信息给你，说明他可能看出你是爬虫了（进行网页请求的时候，浏览器和requests.get都相当于带着一堆资格证去敲门，对方会检查你这些资格证，浏览器的资格证一般是可以通过的，而代码的资格证就可能不合格，因为代码的资格证可能有一些比较固定的特点，对方服务器预先设定好，资格证是这样的请求一律拒绝，因为他们一定是爬虫，这就是反爬虫机制），这时就需要懂一些反反爬措施才能获得真正的信息，反反爬方法的学习是一个积累的过程，我们后面再讲。读者如果遇到一些反爬机制，可以到网上查这个网站的爬虫，估计都能查到一些博客讲如何破解，甚至直接贴出代码。