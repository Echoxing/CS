---
title: c++自学讲义第二章——c++数据
date: 2022-10-20 21:05:58
tags:
    - 编程
    - c++
categories: c++
cover:
---



# 2.3 c++数据结构

>程序的运行离不开一个个数据，其中数组的存在让我们可以存储相同类型的数据，比如一个班级学生的成绩，但是一个学生还有学号、性别等，如果用三个数组来储存未免过于麻烦，所以我们能不能引入一个可以存储所有信息的结构单元，这就是结构（struct）
>
>这与GIS中的空间数据库有异曲同工之妙。

**结构**是c++中一种用户可以自定义的可用数据类型，允许存储不同类型的数据项。

## 2.3.1 定义结构

```c++ 
struct type_name{
    member_type1 member_name1;//变量定义，类似于int a;float b
    member_type2 member_name2;
    member_type3 member_name3;
    .
    .
}object_names;//注意这个分号！
```

- **type_name** 是结构体类型的名称
- **member_type1 member_name1** 是标准的变量定义，比如 **int i;** 或者 **float f;** 或者其他有效的变量定义。在结构定义的末尾，最后一个分号之前，您可以指定一个或多个结构变量，这是可选的。

```c++
//声明一个结构体类型Books，变量为book
struct Books {   
    char  title[50];   
    char  author[50];   
    char  subject[100];   
    int   book_id; 
} book;
```

## 2.3.2 访问结构成员

成员访问运算符（.）

```c++ 
#include <iostream>
#include <cstring> 
using namespace std;
 
// 声明一个结构体类型 Books 
struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
};
 
int main( )
{
   Books Book1;        // 定义结构体类型 Books 的变量 Book1
   Books Book2;        // 定义结构体类型 Books 的变量 Book2
 
   // Book1 详述
   strcpy( Book1.title, "C++ 教程");
   strcpy( Book1.author, "Runoob"); 
   strcpy( Book1.subject, "编程语言");
   Book1.book_id = 12345;
 
   // Book2 详述
   strcpy( Book2.title, "CSS 教程");
   strcpy( Book2.author, "Runoob");
   strcpy( Book2.subject, "前端技术");
   Book2.book_id = 12346;
 
   // 输出 Book1 信息
   cout << "第一本书标题 : " << Book1.title <<endl;
   cout << "第一本书作者 : " << Book1.author <<endl;
   cout << "第一本书类目 : " << Book1.subject <<endl;
   cout << "第一本书 ID : " << Book1.book_id <<endl;
 
   // 输出 Book2 信息
   cout << "第二本书标题 : " << Book2.title <<endl;
   cout << "第二本书作者 : " << Book2.author <<endl;
   cout << "第二本书类目 : " << Book2.subject <<endl;
   cout << "第二本书 ID : " << Book2.book_id <<endl;
 
   return 0;
}

输出：
第一本书标题 : C++ 教程
第一本书作者 : Runoob
第一本书类目 : 编程语言
第一本书 ID : 12345
第二本书标题 : CSS 教程
第二本书作者 : Runoob
第二本书类目 : 前端技术
第二本书 ID : 12346
```

> Strcpy函数用法
>
> 1.函数原型 char *strcpy(char *dest,const char *src)
>
> 2.头文件：#include<string.h>
>
> 3.功能：从src地址开始且含有null结束符的字符串复制到以dest地址开始的字符串中，并返回指向dest的指针。通俗的讲就是将 src字符数组复制到dest数组中，如果dest数组本身有数据，会把src里的数据全部复制到dest中，如果dest中有数据小于src地址长度的将会被覆盖，而大于src长度的将保留
>
> 4.说明：dest的地址长度要足够大，不然会产生溢出。Dest的内存长度要大于等于src的内存长度。

结构也可以作为函数参数，同时也有指向结构的指针

## 2.3.3 typedef关键字

一种更简单的定义结构的方式，为创建的类型取一个"别名"。例如：

```c++
typedef struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
}Books;
```

现在，您可以直接使用 *Books* 来定义 *Books* 类型的变量，而不需要使用 struct 关键字。下面是实例：

```
Books Book1, Book2;
```

您可以使用 **typedef** 关键字来定义非结构类型，如下所示：

```c++
typedef long int *pint32;
 
pint32 x, y, z;//x, y 和 z 都是指向长整型 long int 的指针。
```















# c++数组

**数组** （array）是一种数据格式，能够存储多个同类型的值

## 数组声明

●数组名

●存储在数组中值的类型

●数组中的元素数

```
type arrayName [ arraySize ];
```

这叫做一维数组。**arraySize** 必须是一个大于零的整数常量，**type** 可以是任意有效的 C++ 数据类型。

  一维数组名用途：

1.可以统计整个数组在内存中的长度    sizeof(arr)

2.可以获取数组在内存中的首地址

## 初始化数组

```
double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};
```

## 访问数组元素

```c++
double salary = balance[9];
```



### 数组元素倒序输出

1.for循环直接倒序输出？不行

```
temp=arr[i];
 arr[i] = arr[j];
 arr[j] = temp;
```

#### 冒泡排序

将一无序数组升序输出

```c++
//外循环，元素个数-1
for (i = 0; i < 8; i++) {
        //内循环，元素个数-i-1
        for (j = 0; j < 9-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
 
        }
    }
```

## 3.二维数组

### 3.1定义方式



### 3.2数组名

* 查看二维数组所占内存空间 sizeof（arr）
* 获取二维数组首地址

# 模板类vector

> 一种动态数组，要使用vector对象，必须包含头文件vector，其次vector包含在名称空间std中，因此可使用using编译指令、using声明或std::vector

例子

```c++ 
#include <vector>
...
using namespace std;
vector<int>vi;
int n;
cin>>n;
vector<double>vd(n);
```

vi是一个vector<int>对象，vd是一个vector<double>对象。

下面创建一个名为vt的vector对象，可以存储n_elem个类型为typeName的元素

vector<typeName> vt(n_elem);

# 模板类array

> 位于名称空间std中，长度是固定的，需要包含头文件array。

创建语法：

```c++
#include<array>
...
using namespace std;
array<int,5>ai;
array<double,4>ad={1.2,2.1,3.43,4.3}
```

下面创建一个名为arr的array对象，它包含n_elem个类型为typename的元素

array<typeName,n_elem>arr;
