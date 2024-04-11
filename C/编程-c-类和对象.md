---
title: c++自学讲义第四章——类和对象
date: 2022-10-20 21:06:42
tags:
     - 编程
     - c++
categories: c++
cover:
---

> 引入：对于规模较小的程序，我们可以直接编写程序详细的过程，但是面对大型的程序，我们。从程序结构角度看,C++基于过程的程序和面向对象的程序是不同的。在基于过程的程序中,函数是构成程序的基本部分,程序面对的是一个个函数。每个函数都是独立存在于程序中,除了主函数只能被操作系统调用外,各函数可以互相调用。而在面向对象的程序中,除主函数外,其他函数基本上都是出现在“类”中的,只有通过类才能调用类中的函数。程序的基本构成单位是类,程序面对的是一个一个的类和对象。程序设计的主要工作是设计类、定义和使用类对象。显然,这时的程序设计是基于类(即基于对象)的,而不是基于函数或基于过程的。
> 凡是以类对象为基本构成单位的程序称为基于对象的程序。而面向对象程序设计则还有更多的要求。面向对象程序设计有4个主要特点:抽象、封装、继承和多态性。C++的类对象体现了抽象和封装的特性,在此基础上再利用继承和多态性,就成为真正的面向对象的程序设计。在本篇的3章中,介绍面向对象的基本知识和基于对象的程序设计,它是面向对象程序设计的基础。第4篇进一步介绍面向对象的程序设计。
> 为了与基于过程作比较,往往把基于对象程序设计和面向对象程序设计统称为面向对象程序设计。

# c++类&对象

## c++类声明

**类** （class）是用户自定义数据类型。如果程序中需要使用类类型（class type），必须根据实际需要定义，或者使用已设计好的类。

包括数据成员和函数成员

实际上没有定义任何数据，但是定义了类的名称意味着什么，即类的对象包括了什么，以及可以在这个对象上执行哪些操作

```c++
class classname   //关键字  类名
{
    Access specifiers:       //访问修饰符
           Date members/variables;  //变量
           Member functions(){}    //方法
}
```

例如

```c++ 
class Box
{
   public:
      double length;   // 盒子的长度
      double breadth;  // 盒子的宽度
      double height;   // 盒子的高度
};
```

### c++类成员函数

类的成员函数是把那些定义和原型写在类定义内部的函数

定义在内部

```c++
class 类名{
    //类体
    ...
    返回类型 函数名（形式参数列表）//成员函数定义
    {
        函数体
    }
    ...
}
```

定义在外部

```c++
class 类名{
    //类体
    ...
    //成员函数声明
    返回类型 函数名（类型一 参数名，类型2 参数名，...）；
    ...
};
返回类型 类名::函数名（形式参数列表）
{
    //成员函数定义在类外部实现
    函数体
}
```



```c++
class Box
{
   public:
      double length;      // 长度
      double breadth;     // 宽度
      double height;      // 高度
   
      double getVolume(void)
      {
         return length * breadth * height;
      }
};
//也可以在类的外部使用范围解析运算符::定义该函数
double Box::getVolume(void)
{
    return length * breadth * height;
}
```

调用成员函数

```c++
Box myBox;          // 创建一个对象
 
myBox.getVolume();  // 调用该对象的成员函数
```

例：

```c++
#include <iostream>
 
using namespace std;
 
class Box
{
   public:
      double length;         // 长度
      double breadth;        // 宽度
      double height;         // 高度
 
      // 成员函数声明
      double getVolume(void);
      void setLength( double len );
      void setBreadth( double bre );
      void setHeight( double hei );
};
 
// 成员函数定义
double Box::getVolume(void)
{
    return length * breadth * height;
}
 
void Box::setLength( double len )
{
    length = len;
}
 
void Box::setBreadth( double bre )
{
    breadth = bre;
}
 
void Box::setHeight( double hei )
{
    height = hei;
}
 
// 程序的主函数
int main( )
{
   Box Box1;                // 声明 Box1，类型为 Box
   Box Box2;                // 声明 Box2，类型为 Box
   double volume = 0.0;     // 用于存储体积
 
   // box 1 详述
   Box1.setLength(6.0); 
   Box1.setBreadth(7.0); 
   Box1.setHeight(5.0);
 
   // box 2 详述
   Box2.setLength(12.0); 
   Box2.setBreadth(13.0); 
   Box2.setHeight(10.0);
 
   // box 1 的体积
   volume = Box1.getVolume();
   cout << "Box1 的体积：" << volume <<endl;
 
   // box 2 的体积
   volume = Box2.getVolume();
   cout << "Box2 的体积：" << volume <<endl;
   return 0;
}
```

## 类访问修饰符

### public

### private









# 类的构造函数和析构函数

## 构造函数

类的构造函数是类的一种特殊的成员函数，会在每次创建类的新对象时执行

构造函数的名称与类的名称是完全相同的，并且不会返回任何类型，也不会返回void。构造函数可用于为某些成员变量设置初始值

```c++
#include <iostream>
using namespace std;
 
class Line
{
   public:
      void setLength( double len );
      double getLength( void );
      Line();  // 这是构造函数
   private:
      double length;
}; 
// 成员函数定义，包括构造函数
Line::Line(void)
{
    cout << "Object is being created" << endl;
}
void Line::setLength( double len )
{
    length = len;
}
double Line::getLength( void )
{
    return length;
}
// 程序的主函数
int main( )
{
   Line line;
 
   // 设置长度
   line.setLength(6.0); 
   cout << "Length of line : " << line.getLength() <<endl;
 
   return 0;
}
```

编译运行结果：

```c++
Object is being created
Length of line : 6
```



### 声明和定义构造函数

### 使用构造函数





## 析构函数

一种特殊的成员函数，会在每次删除所创建的对象时执行

析构函数的名称与类的名称是完全相同的，只是前面加了个波浪号（～），不会有返回值，也不能带有任何参数，有助于在跳出程序前释放资源

```c++
#include <iostream>
using namespace std;
 
class Line
{
   public:
      void setLength( double len );
      double getLength( void );
      Line();   // 这是构造函数声明
      ~Line();  // 这是析构函数声明
   private:
      double length;
}; 
// 成员函数定义，包括构造函数
Line::Line(void)
{
    cout << "Object is being created" << endl;
}
Line::~Line(void)
{
    cout << "Object is being deleted" << endl;
}
void Line::setLength( double len )
{
    length = len;
} 
double Line::getLength( void )
{
    return length;
}
// 程序的主函数
int main( )
{
   Line line;
 
   // 设置长度
   line.setLength(6.0); 
   cout << "Length of line : " << line.getLength() <<endl;
 
   return 0;
}
```

编译执行结果：

```c++
Object is being created
Length of line : 6
Object is being deleted
```

# c++this指针

每个对象都能通过指针来访问自己的地址。this指针是所有成员函数的隐含参数。

```c++
#include <iostream>
 
using namespace std;
 
class Box
{
   public:
      // 构造函数定义
      Box(double l=2.0, double b=2.0, double h=2.0)
      {
         cout <<"Constructor called." << endl;
         length = l;
         breadth = b;
         height = h;
      }
      double Volume()
      {
         return length * breadth * height;
      }
      int compare(Box box)
      {
         return this->Volume() > box.Volume();
      }
   private:
      double length;     // Length of a box
      double breadth;    // Breadth of a box
      double height;     // Height of a box
};
 
int main(void)
{
   Box Box1(3.3, 1.2, 1.5);    // Declare box1
   Box Box2(8.5, 6.0, 2.0);    // Declare box2
 
   if(Box1.compare(Box2))
   {
      cout << "Box2 is smaller than Box1" <<endl;
   }
   else
   {
      cout << "Box2 is equal to or larger than Box1" <<endl;
   }
   return 0;
}
```

结果

```c++
Constructor called.
Constructor called.
Box2 is equal to or larger than Box1
```



