---
title: 肆意生长|04期-我想要什么样的博客？
date: 2022-10-24 08:28:23
tags:
categories:
cover:
---

### 1.3 变量

**作用**：给一段指定的内存空间起名，方便操作这段内存

**语法**：`数据类型 变量名 = 初始值;`

**示例：**

```
#include<iostream>
using namespace std;

int main() {

	//变量的定义
	//语法：数据类型  变量名 = 初始值

	int a = 10;

	cout << "a = " << a << endl;
	
	system("pause");

	return 0;
}
```

> 注意：C++在创建变量时，必须给变量一个初始值，否则会报错

### 1.4 常量

**作用**：用于记录程序中不可更改的数据

C++定义常量两种方式

1. **#define** 宏常量： `#define 常量名 常量值`
   - ==通常在文件上方定义==，表示一个常量
2. **const**修饰的变量 `const 数据类型 常量名 = 常量值`
   - ==通常在变量定义前加关键字const==，修饰该变量为常量，不可修改

**示例：**

```c++
//1、宏常量
#define day 7

int main() {

	cout << "一周里总共有 " << day << " 天" << endl;
	//day = 8;  //报错，宏常量不可以修改

	//2、const修饰变量
	const int month = 12;
	cout << "一年里总共有 " << month << " 个月份" << endl;
	//month = 24; //报错，常量是不可以修改的
	
	
	system("pause");

	return 0;
}
```

### 1.5 关键字

**作用：**关键字是C++中预先保留的单词（标识符）

- **在定义变量或者常量时候，不要用关键字**

C++关键字如下：

| asm        | do           | if               | return      | typedef  |
| ---------- | ------------ | ---------------- | ----------- | -------- |
| auto       | double       | inline           | short       | typeid   |
| bool       | dynamic_cast | int              | signed      | typename |
| break      | else         | long             | sizeof      | union    |
| case       | enum         | mutable          | static      | unsigned |
| catch      | explicit     | namespace        | static_cast | using    |
| char       | export       | new              | struct      | virtual  |
| class      | extern       | operator         | switch      | void     |
| const      | false        | private          | template    | volatile |
| const_cast | float        | protected        | this        | wchar_t  |
| continue   | for          | public           | throw       | while    |
| default    | friend       | register         | true        |          |
| delete     | goto         | reinterpret_cast | try         |          |

```
提示：在给变量或者常量起名称时候，不要用C++得关键字，否则会产生歧义。
```

### 1.6 标识符命名规则

**作用**：C++规定给标识符（变量、常量）命名时，有一套自己的规则

- 标识符不能是关键字
- 标识符只能由字母、数字、下划线组成
- 第一个字符必须为字母或下划线
- 标识符中字母区分大小写

> 建议：给标识符命名时，争取做到见名知意的效果，方便自己和他人的阅读

## 2 数据类型

C++规定在创建一个变量或者常量时，必须要指定出相应的数据类型，否则无法给变量分配内存

> 数据类型存在的意义：给变量分配合适的内存空间

### 2.1 整型

**作用**：整型变量表示的是==整数类型==的数据

C++中能够表示整型的类型有以下几种方式，**区别在于所占内存空间不同**：

| **数据类型**        | **占用空间**                                    | 取值范围         |
| ------------------- | ----------------------------------------------- | ---------------- |
| short(短整型)       | 2字节                                           | (-2^15 ~ 2^15-1) |
| int(整型)           | 4字节                                           | (-2^31 ~ 2^31-1) |
| long(长整形)        | Windows为4字节，Linux为4字节(32位)，8字节(64位) | (-2^31 ~ 2^31-1) |
| long long(长长整形) | 8字节                                           | (-2^63 ~ 2^63-1) |

### 2.2 sizeof关键字

**作用：**利用sizeof关键字可以==统计数据类型所占内存大小==

**语法：** `sizeof( 数据类型 / 变量)`

**示例：**

```
int main() {

	cout << "short 类型所占内存空间为： " << sizeof(short) << endl;

	cout << "int 类型所占内存空间为： " << sizeof(int) << endl;

	cout << "long 类型所占内存空间为： " << sizeof(long) << endl;

	cout << "long long 类型所占内存空间为： " << sizeof(long long) << endl;

	system("pause");

	return 0;
}
```

> **整型结论**：==short < int <= long <= long long==

### 2.3 实型（浮点型）

**作用**：用于==表示小数==

浮点型变量分为两种：

1. 单精度float
2. 双精度double

两者的**区别**在于表示的有效数字范围不同。

| **数据类型** | **占用空间** | **有效数字范围** |
| ------------ | ------------ | ---------------- |
| float        | 4字节        | 7位有效数字      |
| double       | 8字节        | 15～16位有效数字 |

**示例：**

```c++
int main() {

	float f1 = 3.14f;
	double d1 = 3.14;

	cout << f1 << endl;
	cout << d1<< endl;

	cout << "float  sizeof = " << sizeof(f1) << endl;
	cout << "double sizeof = " << sizeof(d1) << endl;

	//科学计数法
	float f2 = 3e2; // 3 * 10 ^ 2 
	cout << "f2 = " << f2 << endl;

	float f3 = 3e-2;  // 3 * 0.1 ^ 2
	cout << "f3 = " << f3 << endl;

	system("pause");

	return 0;
}
```

### 2.4 字符型

**作用：**字符型变量用于显示单个字符

**语法：**`char ch = 'a';`

> 注意1：在显示字符型变量时，用单引号将字符括起来，不要用双引号

> 注意2：单引号内只能有一个字符，不可以是字符串

- C和C++中字符型变量只占用==1个字节==。
- 字符型变量并不是把字符本身放到内存中存储，而是将对应的ASCII编码放入到存储单元

cin将键盘输入的字符转换为数字；输出时，cout将值转换为所显示的字符

示例：

```c++
int main() {
	
	char ch = 'a';
	cout << ch << endl;
	cout << sizeof(char) << endl;

	//ch = "abcde"; //错误，不可以用双引号
	//ch = 'abcde'; //错误，单引号内只能引用一个字符

	cout << (int)ch << endl;  //查看字符a对应的ASCII码
	ch = 97; //可以直接用ASCII给字符型变量赋值
	cout << ch << endl;
	
	cout.put('!')//显示一个字符

	system("pause");

	return 0;
}
```

ASCII码表格：

| **ASCII**值 | **控制字符** | **ASCII**值 | **字符** | **ASCII**值 | **字符** | **ASCII**值 | **字符** |
| ----------- | ------------ | ----------- | -------- | ----------- | -------- | ----------- | -------- |
| 0           | NUT          | 32          | (space)  | 64          | @        | 96          | 、       |
| 1           | SOH          | 33          | !        | 65          | A        | 97          | a        |
| 2           | STX          | 34          | "        | 66          | B        | 98          | b        |
| 3           | ETX          | 35          | #        | 67          | C        | 99          | c        |
| 4           | EOT          | 36          | $        | 68          | D        | 100         | d        |
| 5           | ENQ          | 37          | %        | 69          | E        | 101         | e        |
| 6           | ACK          | 38          | &        | 70          | F        | 102         | f        |
| 7           | BEL          | 39          | ,        | 71          | G        | 103         | g        |
| 8           | BS           | 40          | (        | 72          | H        | 104         | h        |
| 9           | HT           | 41          | )        | 73          | I        | 105         | i        |
| 10          | LF           | 42          | *        | 74          | J        | 106         | j        |
| 11          | VT           | 43          | +        | 75          | K        | 107         | k        |
| 12          | FF           | 44          | ,        | 76          | L        | 108         | l        |
| 13          | CR           | 45          | -        | 77          | M        | 109         | m        |
| 14          | SO           | 46          | .        | 78          | N        | 110         | n        |
| 15          | SI           | 47          | /        | 79          | O        | 111         | o        |
| 16          | DLE          | 48          | 0        | 80          | P        | 112         | p        |
| 17          | DCI          | 49          | 1        | 81          | Q        | 113         | q        |
| 18          | DC2          | 50          | 2        | 82          | R        | 114         | r        |
| 19          | DC3          | 51          | 3        | 83          | S        | 115         | s        |
| 20          | DC4          | 52          | 4        | 84          | T        | 116         | t        |
| 21          | NAK          | 53          | 5        | 85          | U        | 117         | u        |
| 22          | SYN          | 54          | 6        | 86          | V        | 118         | v        |
| 23          | TB           | 55          | 7        | 87          | W        | 119         | w        |
| 24          | CAN          | 56          | 8        | 88          | X        | 120         | x        |
| 25          | EM           | 57          | 9        | 89          | Y        | 121         | y        |
| 26          | SUB          | 58          | :        | 90          | Z        | 122         | z        |
| 27          | ESC          | 59          | ;        | 91          | [        | 123         | {        |
| 28          | FS           | 60          | <        | 92          | /        | 124         | \|       |
| 29          | GS           | 61          | =        | 93          | ]        | 125         | }        |
| 30          | RS           | 62          | >        | 94          | ^        | 126         | `        |
| 31          | US           | 63          | ?        | 95          | _        | 127         | DEL      |

ASCII 码大致由以下**两部分组**成：

- ASCII 非打印控制字符： ASCII 表上的数字 **0-31** 分配给了控制字符，用于控制像打印机等一些外围设备。
- ASCII 打印字符：数字 **32-126** 分配给了能在键盘上找到的字符，当查看或打印文档时就会出现。

### 2.5 转义字符

**作用：**用于表示一些==不能显示出来的ASCII字符==

现阶段我们常用的转义字符有：` \n  \\  \t`

| **转义字符** | **含义**                                | **ASCII**码值（十进制） |
| ------------ | --------------------------------------- | ----------------------- |
| \a           | 警报                                    | 007                     |
| \b           | 退格(BS) ，将当前位置移到前一列         | 008                     |
| \f           | 换页(FF)，将当前位置移到下页开头        | 012                     |
| **\n**       | **换行(LF) ，将当前位置移到下一行开头** | **010**                 |
| \r           | 回车(CR) ，将当前位置移到本行开头       | 013                     |
| **\t**       | **水平制表(HT) （跳到下一个TAB位置）**  | **009**                 |
| \v           | 垂直制表(VT)                            | 011                     |
| **\\**       | **代表一个反斜线字符""**                | **092**                 |
| '            | 代表一个单引号（撇号）字符              | 039                     |
| "            | 代表一个双引号字符                      | 034                     |
| ?            | 代表一个问号                            | 063                     |
| \0           | 数字0                                   | 000                     |
| \ddd         | 8进制转义字符，d范围0~7                 | 3位8进制                |
| \xhh         | 16进制转义字符，h范围0~~9，a~~f，A~F    | 3位16进制               |

示例：

```c++
int main() {
	
	
	cout << "\\" << endl;
    
    //水平制表符\t 作用可以整齐输出数据
	cout << "\tHello" << endl;
    
	cout << "\n" << endl;

	system("pause");

	return 0;
}
```

### 2.6 字符串型

**作用**：用于表示一串字符

**两种风格**

1. **C风格字符串**： `char 变量名[] = "字符串值"`

   示例：

   ```
   int main() {
   
   	char str1[] = "hello world";
   	cout << str1 << endl;
       
   	system("pause");
   
   	return 0;
   }
   ```

> 注意：C风格的字符串要用双引号括起来

1. **C++风格字符串**： `string  变量名 = "字符串值"`

   示例：

   ```
   int main() {
   
   	string str = "hello world";
   	cout << str << endl;
   	
   	system("pause");
   
   	return 0;
   }
   ```

   

> 注意：C++风格字符串，需要加入头文件==#include<string>==

### 2.7 布尔类型 bool

**作用：**布尔数据类型代表真或假的值

bool类型只有两个值：

- true --- 真（本质是1）
- false --- 假（本质是0）

**bool类型占==1个字节==大小**

- 字面值true和false都可以通过提升转换为int类型，true被转换为1，false转换为0
- 任何数字或指针值都可以被隐式转换为bool值，任何非零值被转换为true，而；零被转换为1

示例：

```c++
int main() {

	bool flag = true;
	cout << flag << endl; // 1

	flag = false;
	cout << flag << endl; // 0

	cout << "size of bool = " << sizeof(bool) << endl; //1
	
	int ans = true;
	int promise = false;
    
	bool start = -100;
	bool stop = 0;
    
	system("pause");

	return 0;
}
```

### 2.8 数据的输入

**作用：用于从键盘获取数据**

**关键字：**cin

**语法：** `cin >> 变量 `

示例：

```
int main(){

	//整型输入
	int a = 0;
	cout << "请输入整型变量：" << endl;
	cin >> a;
	cout << a << endl;

	//浮点型输入
	double d = 0;
	cout << "请输入浮点型变量：" << endl;
	cin >> d;
	cout << d << endl;

	//字符型输入
	char ch = 0;
	cout << "请输入字符型变量：" << endl;
	cin >> ch;
	cout << ch << endl;

	//字符串型输入
	string str;
	cout << "请输入字符串型变量：" << endl;
	cin >> str;
	cout << str << endl;

	//布尔类型输入
	bool flag = true;
	cout << "请输入布尔型变量：" << endl;
	cin >> flag;
	cout << flag << endl;
	system("pause");
	return EXIT_SUCCESS;
}
```

## 3 运算符

**作用：**用于执行代码的运算

本章我们主要讲解以下几类运算符：

| **运算符类型** | **作用**                               |
| -------------- | -------------------------------------- |
| 算术运算符     | 用于处理四则运算                       |
| 赋值运算符     | 用于将表达式的值赋给变量               |
| 比较运算符     | 用于表达式的比较，并返回一个真值或假值 |
| 逻辑运算符     | 用于根据表达式的值返回真值或假值       |

### 3.1 算术运算符

**作用**：用于处理四则运算

算术运算符包括以下符号：

| **运算符** | **术语**   | **示例**    | **结果**  |
| ---------- | ---------- | ----------- | --------- |
| +          | 正号       | +3          | 3         |
| -          | 负号       | -3          | -3        |
| +          | 加         | 10 + 5      | 15        |
| -          | 减         | 10 - 5      | 5         |
| *          | 乘         | 10 * 5      | 50        |
| /          | 除         | 10 / 5      | 2         |
| %          | 取模(取余) | 10 % 3      | 1         |
| ++         | 前置递增   | a=2; b=++a; | a=3; b=3; |
| ++         | 后置递增   | a=2; b=a++; | a=3; b=2; |
| --         | 前置递减   | a=2; b=--a; | a=1; b=1; |
| --         | 后置递减   | a=2; b=a--; | a=1; b=2; |

**示例1：**

```
//加减乘除
int main() {

	int a1 = 10;
	int b1 = 3;

	cout << a1 + b1 << endl;
	cout << a1 - b1 << endl;
	cout << a1 * b1 << endl;
	cout << a1 / b1 << endl;  //两个整数相除结果依然是整数

	int a2 = 10;
	int b2 = 20;
	cout << a2 / b2 << endl; 

	int a3 = 10;
	int b3 = 0;
	//cout << a3 / b3 << endl; //报错，除数不可以为0


	//两个小数可以相除
	double d1 = 0.5;
	double d2 = 0.25;
	cout << d1 / d2 << endl;

	system("pause");

	return 0;
}
```

> 总结：在除法运算中，除数不能为0

**示例2：**

```
//取模
int main() {

	int a1 = 10;
	int b1 = 3;

	cout << 10 % 3 << endl;

	int a2 = 10;
	int b2 = 20;

	cout << a2 % b2 << endl;//10

	int a3 = 10;
	int b3 = 0;

	//cout << a3 % b3 << endl; //取模运算时，除数也不能为0

	//两个小数不可以取模
	double d1 = 3.14;
	double d2 = 1.1;

	//cout << d1 % d2 << endl;

	system("pause");

	return 0;
}
```

> 总结：只有整型变量可以进行取模运算

**示例3：**

```
//递增
int main() {

	//后置递增
	int a = 10;
	a++; //等价于a = a + 1
	cout << a << endl; // 11

	//前置递增
	int b = 10;
	++b;
	cout << b << endl; // 11

	//区别
	//前置递增先对变量进行++，再计算表达式
	int a2 = 10;
	int b2 = ++a2 * 10;
	cout << b2 << endl;

	//后置递增先计算表达式，后对变量进行++
	int a3 = 10;
	int b3 = a3++ * 10;
	cout << b3 << endl;

	system("pause");

	return 0;
}
```

> 总结：前置递增先对变量进行++，再计算表达式，后置递增相反

### 3.2 赋值运算符

**作用：**用于将表达式的值赋给变量

赋值运算符包括以下几个符号：

| **运算符** | **术语** | **示例**   | **结果**  |
| ---------- | -------- | ---------- | --------- |
| =          | 赋值     | a=2; b=3;  | a=2; b=3; |
| +=         | 加等于   | a=0; a+=2; | a=2;      |
| -=         | 减等于   | a=5; a-=3; | a=2;      |
| *=         | 乘等于   | a=2; a*=2; | a=4;      |
| /=         | 除等于   | a=4; a/=2; | a=2;      |
| %=         | 模等于   | a=3; a%2;  | a=1;      |

**示例：**

```
int main() {

	//赋值运算符

	// =
	int a = 10;
	a = 100;
	cout << "a = " << a << endl;

	// +=
	a = 10;
	a += 2; // a = a + 2;
	cout << "a = " << a << endl;

	// -=
	a = 10;
	a -= 2; // a = a - 2
	cout << "a = " << a << endl;

	// *=
	a = 10;
	a *= 2; // a = a * 2
	cout << "a = " << a << endl;

	// /=
	a = 10;
	a /= 2;  // a = a / 2;
	cout << "a = " << a << endl;

	// %=
	a = 10;
	a %= 2;  // a = a % 2;
	cout << "a = " << a << endl;

	system("pause");

	return 0;
}
```

### 3.3 比较运算符

**作用：**用于表达式的比较，并返回一个真值或假值

比较运算符有以下符号：

| **运算符** | **术语** | **示例** | **结果** |
| ---------- | -------- | -------- | -------- |
| ==         | 相等于   | 4 == 3   | 0        |
| !=         | 不等于   | 4 != 3   | 1        |
| <          | 小于     | 4 < 3    | 0        |
| >          | 大于     | 4 > 3    | 1        |
| <=         | 小于等于 | 4 <= 3   | 0        |
| >=         | 大于等于 | 4 >= 1   | 1        |

示例：

```
int main() {

	int a = 10;
	int b = 20;

	cout << (a == b) << endl; // 0 

	cout << (a != b) << endl; // 1

	cout << (a > b) << endl; // 0

	cout << (a < b) << endl; // 1

	cout << (a >= b) << endl; // 0

	cout << (a <= b) << endl; // 1
	
	system("pause");

	return 0;
}
```

> 注意：C和C++ 语言的比较运算中， ==“真”用数字“1”来表示， “假”用数字“0”来表示。==

### 3.4 逻辑运算符

**作用：**用于根据表达式的值返回真值或假值

逻辑运算符有以下符号：

| **运算符** | **术语** | **示例** | **结果**                                                 |
| ---------- | -------- | -------- | -------------------------------------------------------- |
| !          | 非       | !a       | 如果a为假，则!a为真； 如果a为真，则!a为假。              |
| &&         | 与       | a && b   | 如果a和b都为真，则结果为真，否则为假。                   |
| \|\|       | 或       | a \|\| b | 如果a和b有一个为真，则结果为真，二者都为假时，结果为假。 |

**示例1：**逻辑非

```
//逻辑运算符  --- 非
int main() {

	int a = 10;

	cout << !a << endl; // 0

	cout << !!a << endl; // 1

	system("pause");

	return 0;
}
```

> 总结： 真变假，假变真

**示例2：**逻辑与

```
//逻辑运算符  --- 与
int main() {

	int a = 10;
	int b = 10;

	cout << (a && b) << endl;// 1

	a = 10;
	b = 0;

	cout << (a && b) << endl;// 0 

	a = 0;
	b = 0;

	cout << (a && b) << endl;// 0

	system("pause");

	return 0;
}
```

> 总结：逻辑==与==运算符总结： ==同真为真，其余为假==

**示例3：**逻辑或

```
//逻辑运算符  --- 或
int main() {

	int a = 10;
	int b = 10;

	cout << (a || b) << endl;// 1

	a = 10;
	b = 0;

	cout << (a || b) << endl;// 1 

	a = 0;
	b = 0;

	cout << (a ||
    b) << endl;// 0

	system("pause");

	return 0;
}
```

> 逻辑==或==运算符总结： ==同假为假，其余为真==



## 4 程序流程结构

C/C++支持最基本的三种程序运行结构：==顺序结构、选择结构、循环结构==

- 顺序结构：程序按顺序执行，不发生跳转
- 选择结构：依据条件是否满足，有选择的执行相应功能
- 循环结构：依据条件是否满足，循环多次执行某段代码

### 4.1 选择结构

#### 4.1.1 if语句

**作用：**执行满足条件的语句

if语句的三种形式

- 单行格式if语句

- 多行格式if语句

- 多条件的if语句

  

1. 单行格式if语句：`if(条件){ 条件满足执行的语句 }`

   [![img](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/clip_image002.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/clip_image002.png)

   示例：

   ```
   int main() {
   
   	//选择结构-单行if语句
   	//输入一个分数，如果分数大于600分，视为考上一本大学，并在屏幕上打印
   
   	int score = 0;
   	cout << "请输入一个分数：" << endl;
   	cin >> score;
   
   	cout << "您输入的分数为： " << score << endl;
   
   	//if语句
   	//注意事项，在if判断语句后面，不要加分号
   	if (score > 600)
   	{
   		cout << "我考上了一本大学！！！" << endl;
   	}
   
   	system("pause");
   
   	return 0;
   }
   ```

   

> 注意：if条件表达式后不要加分号，加了就会直接执行里面的代码

2.多行格式if语句：`if(条件){ 条件满足执行的语句 }else{ 条件不满足执行的语句 };`

[![img](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/clip_image002-1541662519170.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/clip_image002-1541662519170.png)



示例：

```
int main() {

	int score = 0;

	cout << "请输入考试分数：" << endl;

	cin >> score;

	if (score > 600)
	{
		cout << "我考上了一本大学" << endl;
	}
	else
	{
		cout << "我未考上一本大学" << endl;
	}

	system("pause");

	return 0;
}
```

3.多条件的if语句：`if(条件1){ 条件1满足执行的语句 }else if(条件2){条件2满足执行的语句}... else{ 都不满足执行的语句}`

[![img](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/clip_image002-1541662566808.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/clip_image002-1541662566808.png)







示例：

```
	int main() {

	int score = 0;

	cout << "请输入考试分数：" << endl;

	cin >> score;

	if (score > 600)
	{
		cout << "我考上了一本大学" << endl;
	}
	else if (score > 500)
	{
		cout << "我考上了二本大学" << endl;
	}
	else if (score > 400)
	{
		cout << "我考上了三本大学" << endl;
	}
	else
	{
		cout << "我未考上本科" << endl;
	}

	system("pause");

	return 0;
}
```



**嵌套if语句**：在if语句中，可以嵌套使用if语句，达到更精确的条件判断

案例需求：

- 提示用户输入一个高考考试分数，根据分数做如下判断
- 分数如果大于600分视为考上一本，大于500分考上二本，大于400考上三本，其余视为未考上本科；
- 在一本分数中，如果大于700分，考入北大，大于650分，考入清华，大于600考入人大。

**示例：**

```
int main() {

	int score = 0;

	cout << "请输入考试分数：" << endl;

	cin >> score;

	if (score > 600)
	{
		cout << "我考上了一本大学" << endl;
		if (score > 700)
		{
			cout << "我考上了北大" << endl;
		}
		else if (score > 650)
		{
			cout << "我考上了清华" << endl;
		}
		else
		{
			cout << "我考上了人大" << endl;
		}
		
	}
	else if (score > 500)
	{
		cout << "我考上了二本大学" << endl;
	}
	else if (score > 400)
	{
		cout << "我考上了三本大学" << endl;
	}
	else
	{
		cout << "我未考上本科" << endl;
	}

	system("pause");

	return 0;
}
```

**练习案例：** 三只小猪称体重

有三只小猪ABC，请分别输入三只小猪的体重，并且判断哪只小猪最重？

#### 4.1.2 三目运算符

**作用：** 通过三目运算符实现简单的判断

**语法：**`表达式1 ? 表达式2 ：表达式3`

**解释：**

如果表达式1的值为真，执行表达式2，并返回表达式2的结果；

如果表达式1的值为假，执行表达式3，并返回表达式3的结果。

**示例：**

```
int main() {

	int a = 10;
	int b = 20;
	int c = 0;

	c = a > b ? a : b;
	cout << "c = " << c << endl;

	//C++中三目运算符返回的是变量,可以继续赋值

	(a > b ? a : b) = 100;

	cout << "a = " << a << endl;
	cout << "b = " << b << endl;
	cout << "c = " << c << endl;

	system("pause");

	return 0;
}
```

> 总结：和if语句比较，三目运算符优点是短小整洁，缺点是如果用嵌套，结构不清晰

#### 4.1.3 switch语句

**作用：**执行多条件分支语句

**语法：**

```
switch(表达式)

{

	case 结果1：执行语句;break;

	case 结果2：执行语句;break;

	...

	default:执行语句;break;

}
```

**示例：**

```
int main() {

	//请给电影评分 
	//10 ~ 9   经典   
	// 8 ~ 7   非常好
	// 6 ~ 5   一般
	// 5分以下 烂片

	int score = 0;
	cout << "请给电影打分" << endl;
	cin >> score;

	switch (score)
	{
	case 10:
	case 9:
		cout << "经典" << endl;
		break;
	case 8:
		cout << "非常好" << endl;
		break;
	case 7:
	case 6:
		cout << "一般" << endl;
		break;
	default:
		cout << "烂片" << endl;
		break;
	}

	system("pause");

	return 0;
}
```

> 注意1：switch语句中表达式类型只能是整型或者字符型

> 注意2：case里如果没有break，那么程序会一直向下执行

> 总结：与if语句比，对于多条件判断时，switch的结构清晰，执行效率高，缺点是switch不可以判断区间

### 4.2 循环结构

#### 4.2.1 while循环语句

**作用：**满足循环条件，执行循环语句

**语法：**` while(循环条件){ 循环语句 }`

**解释：**==只要循环条件的结果为真，就执行循环语句==

[![img](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/clip_image002-1541668640382.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/clip_image002-1541668640382.png)

**示例：**

```
int main() {

	int num = 0;
	while (num < 10)
	{
		cout << "num = " << num << endl;
		num++;
	}
	
	system("pause");

	return 0;
}
```

> 注意：在执行循环语句时候，程序必须提供跳出循环的出口，否则出现死循环

**while循环练习案例：**==猜数字==

**案例描述：**系统随机生成一个1到100之间的数字，玩家进行猜测，如果猜错，提示玩家数字过大或过小，如果猜对恭喜玩家胜利，并且退出游戏。

#### 4.2.2 do...while循环语句

**作用：** 满足循环条件，执行循环语句

**语法：** `do{ 循环语句 } while(循环条件);`

**注意：**与while的区别在于==do...while会先执行一次循环语句==，再判断循环条件

[![img](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/clip_image002-1541671163478.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/clip_image002-1541671163478.png)

**示例：**

```
int main() {

	int num = 0;

	do
	{
		cout << num << endl;
		num++;

	} while (num < 10);
	
	
	system("pause");

	return 0;
}
```

> 总结：与while循环区别在于，do...while先执行一次循环语句，再判断循环条件

**练习案例：水仙花数**

**案例描述：**水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身

例如：1^3 + 5^3+ 3^3 = 153

请利用do...while语句，求出所有3位数中的水仙花数

#### 4.2.3 for循环语句

**作用：** 满足循环条件，执行循环语句

**语法：**` for(起始表达式;条件表达式;末尾循环体) { 循环语句; }`

**示例：**

```
int main() {

	for (int i = 0; i < 10; i++)
	{
		cout << i << endl;
	}
	
	system("pause");

	return 0;
}
```

**详解：**

[![1541673704101](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/1541673704101.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/1541673704101.png)

> 注意：for循环中的表达式，要用分号进行分隔

> 总结：while , do...while, for都是开发中常用的循环语句，for循环结构比较清晰，比较常用

**练习案例：敲桌子**

案例描述：从1开始数到数字100， 如果数字个位含有7，或者数字十位含有7，或者该数字是7的倍数，我们打印敲桌子，其余数字直接打印输出。

#### 4.2.4 嵌套循环

**作用：** 在循环体中再嵌套一层循环，解决一些实际问题

例如我们想在屏幕中打印如下图片，就需要利用嵌套循环

[![1541676003486](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/1541676003486.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/1541676003486.png)

**示例：**

```
int main() {

	//外层循环执行1次，内层循环执行1轮
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			cout << "*" << " ";
		}
		cout << endl;
	}

	system("pause");

	return 0;
}
```

**练习案例：**乘法口诀表

案例描述：利用嵌套循环，实现九九乘法表

[![0006018857256120_b](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/0006018857256120_b.jpg)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/0006018857256120_b.jpg)

### 4.3 跳转语句

#### 4.3.1 break语句

**作用:** 用于跳出==选择结构==或者==循环结构==

break使用的时机：

- 出现在switch条件语句中，作用是终止case并跳出switch
- 出现在循环语句中，作用是跳出当前的循环语句
- 出现在嵌套循环中，跳出最近的内层循环语句

**示例1：**

```
int main() {
	//1、在switch 语句中使用break
	cout << "请选择您挑战副本的难度：" << endl;
	cout << "1、普通" << endl;
	cout << "2、中等" << endl;
	cout << "3、困难" << endl;

	int num = 0;

	cin >> num;

	switch (num)
	{
	case 1:
		cout << "您选择的是普通难度" << endl;
		break;
	case 2:
		cout << "您选择的是中等难度" << endl;
		break;
	case 3:
		cout << "您选择的是困难难度" << endl;
		break;
	}

	system("pause");

	return 0;
}
```

**示例2：**

```
int main() {
	//2、在循环语句中用break
	for (int i = 0; i < 10; i++)
	{
		if (i == 5)
		{
			break; //跳出循环语句
		}
		cout << i << endl;
	}

	system("pause");

	return 0;
}
```

**示例3：**

```
int main() {
	//在嵌套循环语句中使用break，退出内层循环
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			if (j == 5)
			{
				break;
			}
			cout << "*" << " ";
		}
		cout << endl;
	}
	
	system("pause");

	return 0;
}
```

#### 4.3.2 continue语句

**作用：**在==循环语句==中，跳过本次循环中余下尚未执行的语句，继续执行下一次循环

**示例：**

```
int main() {

	for (int i = 0; i < 100; i++)
	{
		if (i % 2 == 0)
		{
			continue;
		}
		cout << i << endl;
	}
	
	system("pause");

	return 0;
}
```

> 注意：continue并没有使整个循环终止，而break会跳出循环

#### 4.3.3 goto语句

**作用：**可以无条件跳转语句

**语法：** `goto 标记;`

**解释：**如果标记的名称存在，执行到goto语句时，会跳转到标记的位置

**示例：**

```
int main() {

	cout << "1" << endl;

	goto FLAG;

	cout << "2" << endl;
	cout << "3" << endl;
	cout << "4" << endl;

	FLAG:

	cout << "5" << endl;
	
	system("pause");

	return 0;
}
```

> 注意：在程序中不建议使用goto语句，以免造成程序流程混乱

>  c++复合数据类型



## 1. 数组概述

### 1.1 数组的定义

数组（array）是一种数据格式，能够存储多个同类型的值。每个值都存储在一个独立的数组元素中，计算机在内存中依次存储数组的各个元素。

数组声明的三个特点：

- 存储在每个元素中的值的类型
- 数组名
- 数组中的元素数

C++中可以通过修改简单变量的声明，添加中括号（其中包含元素数目）来完成数组声明。

例如：

```
short days[24]; // 一天有24个小时
```



### 1.2 数组的声明

声明数组的的一般语法格式为：

```
// 数组类型 数组名字[数组的大小]
typeName arrayName[arrySize]; 
int score[4]; // 四个人的分数，整型数组
```

数组的大小是指定`元素的数目`，必须是`整型常数或const值`，也可以是常量表达式(8*sizeof(int))

### 1.3 复合类型的数组

可以使用其他的类型来创建（C语言使用术语：`派生类型`）

> float loans[20];
>
> loans的类型不是数组，而是“float数组”

数组的用途，可以单独访问数组元素，方法是：使用`下标`或`索引`对元素进行编号。`从0开始编号`。

> 编译器不会检查下标是否有效，所以要注意下标合法性，避免程序异常问题。 C++使用索引的方括号表示法来指定数组元素。

### 1.4 数组的初始化规则

1.只有在定义数组时才能初始化，此后不能使用，也~~不能将一个数值赋给另一个数组~~。

2.初始化数组时，提供的值少于数组的元素数目。

3.如果只对数组的一部分进行初始化，则编译器把其他元素设置为0。

4.如果初始化为`{1}`而不是`{0}`，则第一个元素被设置为1，其他元素都被设置为0.

5.如果初始化数组方括号内`（[]）`为空，C++编译器将`计算元素个数`。 例如：short things[] = {1,3,5,7};

### 1.5 C++11数组初始化方法

C++11将使用大括号的`初始化（列表初始化）`作为一种通用的初始化方式，可用于所有类型。

在C++中列表初始化就增加了一些功能：

- 初始化数组时，可省略`等号（=）`

```
double earnings[4] {1.2e4,1.6e4,1.1e4,1.7e4};
```

- 可不在大括号内包含任何东西，这会将所元素都设置为零。

```
unsigned int const[10] = {};

float balances[100] {};
```

- 列表初始化禁止缩窄转换。

```
long num[] = {25,92,3.0}; // 浮点数转换为整型是缩窄操作
```

例子：

```
#include<iostream>

using namespace std;

int main()
{
    // 创建一个名字为yams的数组，包含了3个元素，编号是0～2.
    int yams[3];
    yams[0] = 7;
    yams[1] = 8;
    yams[2] = 6;

    // 使用逗号分隔的值列表（初始化列表），然后用花括号括起来即可。
    // 列表中的空格是可选的，如果没有初始化函数中定义的数组，其元素值也是不确定。
    int yamcosts[3] = {1,2,3};

    cout<<"yams 数组是："<<yams[0]+yams[1]+yams[2]<<endl;
    cout<<"yams[1] = "<<yams[1]<<endl;
    int total = yams[0] * yamcosts[0] + yams[1] * yamcosts[1];
    total = total + yams[2] * yamcosts[2];
    cout<<"total yam = "<<total<<endl;

    // sizeof运算符返回类型或数据对象的长度（单位为字节）。
    // 如果将sizeof运算符用于数组名，得到的是整个数组的字节数。
    // 如果sizeof用于数组元素，得到的是元素的长度（单位为字节）。
    cout<<"\n yams数组的大小 = "<<sizeof(yams)<<" Bytes.\n";
    cout<<"一个元素的大小 = "<<sizeof(yams[0])<<" Bytes.\n";

    return 0;
}
```

## 2. 字符串

字符串是存储在内存的连续字节中的一系列字符。

### 2.1 C++处理字符串的两种方式：

- C语言，常常被称为

  ```
  C-风格字符串(C-style String)
  ```

  > 以空字符（\0,ASCII码对应为0）来标记字符串的结尾。

- 基于String类库的方法

存储在`连续字节`中的一系列字符意味着可以将`字符串`存储在`char数组`中。其中每个字符都位于自己的数组元素中。

使用`引号`括起来的字符串，这种字符串叫 **`字符串常量（String constant）` 或 `字符串字面值（string literal）`** 。

> 字符串常量（使用双引号）不能与字符常量（使用单引号）互换。

例如：

```
char name[] = "Soler";
```

字符串`结尾的空字符`，`不用直接显式包括`，机器在键盘输入，将字符串读入到`char类型`中，会在结尾`自动加上空字符`。

⚠️注意：确定了存储字符串所需的最短数组时，不要忘记把`结尾的空字符`包括在内。

### 2.2 字符串常量的拼接

方法：直接两个引号括起来的字符串合并为一个。任何两个由`空白（空格、制表符和换行符）`分隔的字符串常量都将自动拼接成一个。

```
cout<<"My name is " "Soler HO.\n" 
```

### 2.3 在数组中使用字符串

将字符串存储到数组的常用方法：

- 将数组初始化为字符串常量
- 将键盘或文件输入读入到数组中。

```
#include <iostream>
#include <cstring> /*提供strlen()函数*/
using namespace std;

const int Size = 15;

int main()
{
    char name1[Size];
    char name2[Size] = "C++owboy";
    // 字符串的拼接
    cout<<"Howdy!I'm "<< name2;
    cout<<"!,What's your name?\n";
    cin>>name1;

    cout<<"Well, "<<name1<<",your name has : "<<strlen(name1)<<" letters and is stored!\n" ;
    cout<<"In an array of "<<sizeof(name1)<<" Bytes\n";
    cout<<"Your iniatial is "<<name1[0]<<".\n"; // name1数组中的第一个元素
    name2[3] = '\0';
    cout<<"Here are the first 3 characters of my name:"<<name2<<endl;

    return 0;
}
```

`strlen() 函数` 和 `sizeof()运算符`的区别

- `strlen()`函数
  - 返回的是`存储在数组中的字符串的长度`，而`~~不是数组本身的长度~~`。
  - strlen()只计算`可见的字符`，而~~不把空字符计算在内~~。
- `sizeof()` 运算符
  - 指出`变量`或`数据类型`的`字节大小`。
  - 可用于获取`类、结构、共用体和其他用户自定义数据类型`的大小。

### 2.4 读取一行字符串的输入

解决没有逐行读取输入的缺陷。

istream中提供了面向行的类成员函数：`getline()` 和 `get()` 函数

#### 2.4.1 面向行的输入：`getline()`

使用通过回车键输入的换行符来确定输入结尾。使用 `cin.getline()` 。

函数有两个参数：

- 第一个参数：存储输入行的`数组名称`。
- 第二个参数：要读取的字符数（注意包含结尾的`空字符（\0）`）。

格式：

```
cin.getline(name,ArSize);
```

#### 2.4.2 面向行的输入：`get()`

与`getline()` 函数类似，接受的`参数相同`，解释参数的方式也相同，并`读到行尾`。

区别：`get()` 读取并`丢弃`换行符，将其留在输入队列中。

格式：

```
cin.get(name,ArSize);
```

get() 将两个类成员函数拼接（合并）：

```
cin.get(name,ArSize).get();
```

⚠️注意：get() 函数读取空行后设置会失效，输入会被阻断。可用如下恢复：

```
cin.clear();
```

混合输入数字和面向行的字符串会导致的问题：无法输入地址。

> 解决方法：直接使用get()进行读取之前丢弃换行符。

## 3. string类

`string类`位于名称空间`std`中，所以需要提供`using指令`或者是直接使用`std::string`进行引用。

要使用`string类`，必须在程序中包含`头文件string`中。

string类定义隐藏了字符串的数组性质。

### 3.1 string对象的方式

使用string对象的方式和使用字符数组相同。

- `C-风格字符串`来初始化string对象中。
- 使用`cin来将键盘输入`存储到string对象中。
- 使用`cout`来显示string对象。
- 可以使用`数组表示方法`来访问存储在string1对象中的字符。

赋值 —— 不能将一个数组赋给另一个数组，但可以将一个string对象赋另一个string对象。

```
char char01[20];                // 创建一个空列表
char char02[20] = "Jason";      // 创建一个初始化数组

string str01;                   // 创建一个空的string对象
string str02 = "Soler Ho";      // 创建一个初始化的string对象

char01 = char01;                // 不可执行，一个数组不能赋值给另一个数组
str01 = str02;                  // 可执行，可将一个string对象赋给另一个string对象。
```

### 3.2 复制、拼接和附加

string类简化字符串合并操作。

- 利用`运算符 + `将两个string对象合并起来。

```
string str01;                  
string str02 = "Soler Ho";

string = str01 + str02;
```

- 可以使用`运算符 += `将字符串`附加`到string对象的`末尾`。

```
string str01;                  
string str02 = "Soler Ho";

str01 += str02;
```

## 4. 结构简介

结构是`用户定义`的类型，而结构声明定义了类型的`数据属性`。

定义类型之后，就直接创建类型的变量。

结构比数组灵活，同一个结构中可以存储多种类型的数据。

### 4.1 创建结构的步骤：

- 定义结构描述 —— 描述并标记能够存储在结构中的各种数据类型
- 按描述创建结构变量（结构数据对象）。

### 4.2 结构的定义：

```
struct(关键字) 类型名(标记成为新类型的名称)
{
    结构成员1;
    结构成员2;
    结构成员3;
};//(结束结构声明)
```

对于结构中的成员，使用`成员运算符（.）`来进行访问各个成员。

### 4.3 结构的初始化（C++11）

- 与数组一样，列表的初始化用于结构，且`等号（=）可有可无`。

```
infor Soler_infor {"Soler HO",55,168}; // 在C++11中，= 号可以省略
```

- 如果大括号内未包含任何东西，各个成员都将设置为零。

```
infor Soler_infor {};
```

- 不允许缩窄转换

✅ 小Tips：C++允许在声明结构变量时省略关键字struct。

### 4.4 成员赋值

***成员赋值（memberwise assignment）***：可以使用`赋值运算符（=）`将结构赋另一个同类型的结构。这样结构中的每个成员都将被设置为另一个结构中相应成员的值。即使成员是数组。这种方式就是`成员赋值`。

## 5. 共用体

共用体（union），也叫做`联合（union）`。一种 **`构造数据类型`** 。

**关键字：union**

联合（union）：将`不同类型的数据`在一起**共同占用同一段内存**

存储不同的数据类型，但只能同时存储其中的一种类型

示例：

```
union sample
{
    int int_val;
    long long_val;
    double double_val;
};
```

### 5.1 结构体和共用体的区别

- 结构可以`同时存储int、long和double`。
- 共用体`只能存储int、long和double`三种。
- 含义不同。
- 关键字不同
  - 结构体：struct
  - 共用体：union

### 5.2 共用体的用途：

- 当数据使用两种格式或更多格式（但不会同时使用）时，可以节省空间。
  - 嵌入式系统编程（如控制烤箱、MP3播放器），内存非常宝贵。
- 常用于操作系统数据结构或硬件数据结构。

### 5.3 匿名共用体

匿名共用体（anonymous union）`没有名称`，其成员将成为位于`相同地址`处的变量。

## 6. 枚举

C++的enum工具提供了另一种创建`符号常量`的方式，可以代替const，允许定义新类型，但必须有严格限制。

使用enum的语法格式与结构的使用类似。

```
enum color{red,orange,yellow,green,blue,voilet};
```

### 6.1 设置枚举量的值

```
enum week{Monday = 1,Tuesday = 2;Wednesday = 3;Thursday = 4};
```

指定的值必须是`整数`。也可以只显示定义其中一些`枚举量的值`。

如果第一个变量未初始化，默认为0。后面没有被初始化的枚举量的值将比其前面的枚举量大1。也可以创建多个值相同的枚举量。

```
enum {zero,null = 0,numero_one,one = 1};
```

### 6.2 枚举的取值范围

每个枚举都有取值范围的上限，通过强制类型转换，可以将取值范围中的任何整数值赋给枚举常量，即使这个值不是枚举值。

### 6.3 取值范围的定义

- 找出上限，需要知道枚举量的最大值。
  - 找到大于最大值的，最小的2的幂，减去1，得到就是取值范围的上限。
- 计算下限，知道枚举量的最小值。
  - 如果不小于0，则取值范围的下限为0，否则，采用寻找上限方式相同的方式，但是要加上负号。

对于选择使用多少空间来存储枚举由`编译器`决定。

## 7. 指针和自由空间

对于地址显示结果是`十六进制表示法`，因为都是常常描述`内存的表示法`。

- 指针与C++基本原理

  > 面向对象编程和传统的过程性编程的区别，OOP强调的是运行阶段(而不是编译阶段)进行决策。

  - **运行阶段**：程序正在运行是，取决于不同的情况。
  - **编译阶段**：编译器将程序组合起来时。坚持原先设定的安排

指针用于存储值的地址。指针名表示的是地址。

> `*运算符`称为间接值或解除引用运算符，将其应用于指针，得到该地址处存储的值。

### 7.1 声明和初始化指针

指针的声明必须指定`指向的数据的类型`。

```
int *p_updates; 
```

> `*p_updates` 的类型是`int`，所以`*运算符`被用于`指针`，所以p_updates变量必须是指针。

运算符*两边的`空格`是可选的。

```
int *ptr; /*该情况强调：*ptr是一个int类型的值。*/

int* ptr; /*该情况强调：int* 是一种类型，指向int的指针。*/
```

在C++中，`int*`是一种复合类型，是`指向int的指针`。

```
double *tax_ptr;
```

### 7.2 指针的危险

在C++创建指针时，计算机将分配用来`存储地址的内存`，但是不会分配用来存储指针所指向的数据的内存。

⚠️注意：一定要在对指针应用`解除引用运算符(*)`之前，将指针初始化为一个`确定`的、适当的`地址`。

### 7.3 指针和数字

整数可以加减乘除等运算，而`指针`描述的是`位置`。

C++语言~~数字不能作为地址使用~~，如果要把数字当地址来使用，应通过`强制类型转换`将数字转换为适当的地址类型。

### 7.4 使用`new分配`和`delete释放`内存

指针在`运行阶段` 分配未命名的内存以存储值。然后使用内存来访问内存。

C语言中，使用 **库函数malloc()**来分配内存。C++中使用 ———— new运算符。

#### 7.4.1 要注意使用delete进行内存的释放

需要内存时，直接使用new来请求，这是内存管理数据包的一个方面。

如果使用了`delete运算符`，使得在使用完内存后，能够将其`归还给内存池`，这是有效使用内存的关键。

使用delete时，后面要加上指向内存块的指针。

```
int * ps = new int; // 使用new进行内存分配
 ...
delete ps; // 使用delete进行内存的释放
```

#### ⚠️注意点：

1.使用delete释放ps的内存，但是~~不会删除指针ps本身~~。

2.只能用`delete`来释放使用`new分配的内存`，但是如果是`空的指针`使用delete是安全的。

**使用delete的关键**：用于`new分配的内存`。~~不是要使用于new的指针~~，而是用于`new的地址`。

❌警告：不能创建两个指向同一个内存块的指针。会增加错误地删除同一个内存块两次的可能性。

### 7.5 使用new创建动态数组

C++中，创建动态数组，只需要将`数组的元素类型`和`元素数目`告诉new即可。必须在`类型名`后面加上`方括号`，其中包含了元素数目。

通用格式：

```
Type_name *pointer_name = new Type_name[num_element];
//例子
int * psome =new int[10]; // 创建10个int元素的数组
```

new运算符会返回第一个元素的地址

如果使用完new分配的内存，使用delete进行内存的释放。

```
delete [] psome; // 进行内存的释放
```

delete和指针直接的方括号告诉程序，应`释放整个数组`，不仅仅是指针指向的元素。

delete中的`方括号的有无`取决于使用`new时的方括号有无`。

对于指针数组的使用，直接可以按照普通数组的使用即可。

### 7.6 使用new和delete时，要遵循的规则

- 不要使用delete来释放不是new分配的内存。
- 不要使用delete释放同一个内存块两次。
- 如果使用`new[]`为`数组`分配内存时，则应使用`delete[] `来释放。
- 如果使用new[]为一个`实体`分配内存，则应使用`delete（没有方括号）`来释放。
- 对空指针使用delete时很安全。

## 8. 指针、数组和指针算术

指针和数组基本等价的原因：`指针算术(pointer arithmetic)` 和`C++ 内部处理数组的方式`。

> - 对`整数变量` + 1，其`值`增加1
> - 对`指针变量` + 1，增加的量等于它`指向的类型的字节数`。 获取数组地址的两种方式

```
double * pw = wages; // 数组名 = 地址 ;将pw声明为指向double类型的指针。然后将其初始化为wages - - - wages数组中第一个元素的地址。

short * ps = &wages[0]; // 使用地址操作；使用地址运算符来将ps指针初始化为stacks数组的第一个元素。
```

### 8.1 指针问题小结

#### 8.1.1 声明指针

要声明指向特定类型的指针，语法格式：

```
TypeName *pointerName;
// 例子
double * pn; // pn 指向一个double类型
char * ps;  // ps 指向一个char类型
```

#### 8.1.2 给指针赋值

将内存地址赋给指针。可以对变量名应用 `& 运算符`，来获得被变量名的`内存地址`，new运算符返回未命名的内存的地址。

示例：

```
double * pn;  // pn 指向一个double类型
double * pa; // pa 指向一个double类型

char * pc; // pc 指向一个char类型
double bubble = 3.2; 

pn = &bubble; // 把bubble的地址赋值给 pn
pc = new char; // 新建char地址并分配给pc
```

#### 8.1.3 对指针解除引用

对指针解除引用意味着获得`指针指向的值`。

- 方法1：对指针应用解除`引用`或`间接值运算符(*)`来解除引用。

```
cout<<*pn;
*pc = 's';
```

- 方法2：使用`数组表示法`。~~不可以对未初始化为适当地址的指针解除引用~~。

#### 8.1.4 数组名

多数情况下，C++将`数组名`视为数组的`第一个元素的地址`。

```
int tacos[10]; // 此时的tacos同样也是&tacos[0]
```

#### 8.1.5 指针算术

C++中允许指针和整数`相加`。加1 的结果等于`原来的地址值`加上指向的对象占用的`总字节数`。

也可以将一个指针减去另一个指针，获得两个指针的差。得到一个整数，仅当两个指针指向同一个数组(也可以指向超出结尾的一个位置)时，这种情况会得到两个元素的间隔。

#### 8.1.6 数组的动态联编和静态联编

使用数组声明来创建数组时，将采用`静态联编`，即数组长度在`编译`时设置。

```
int tacos[10] // 静态联编
```

使用`new[]运算符`创建数组时，将采用`动态联编(动态数组)`，即将在运行时为数组分配空间，其长度为运行时设置。

> 使用这类数组后，要使用`delete[]`释放所占用的内存。

#### 8.1.7 数组表示法和指针表示法

使用`方括号数组表示法`等同于对指针`解除引用`。

数组名和指针变量也是一样。所以对于指针和数组名，既可以使用`指针表示法`，也可以使用`数组表示法`。

```
int * pt = new int [10];
*pt = 5;
pt[0] = 6;
pt[9] = 5;
int coats[10];
*(coats + 4) = 12;
```

### 8.2 指针和字符串

数组名是`第一个元素地址`。

如果给cout提供一个字符的地址，则它将从该字符开始打印，直到遇到空字符为止。

在cout和多数C++表达式中，`char数组名`、`char指针`以及用引号括起来的`字符串常量`都被解释为`字符串第一个字符的地址`。

~~不要使用字符串常量或未被初始化的指针来接收输入~~。

> 在字符串读入程序时，应使用已分配的内存地址。该地址不是数组名，也可以使用new初始化过的指针。

`strcpy()`接受两个参数,第一个：`目标地址`，第二个：`要复制的字符串的地址`。

> 要确定目标空间有足够的空间来存储副本。

### 8.3 使用new创建动态结构

对于在指定结构成员时，`句点运算符`和`箭头运算符`的选择时：

- 如果结构标识符是`结构名`，则使用`句点运算符（.）`。
- 如果标识符是`指向结构的指针`，则使用`箭头运算符（->）`。

把new用于结构的两个步骤

- 创建结构

  > 要创建结构，需要同时使用结构类型和new。

- 创建访问其成员。

### 8.4 C++管理数据内存的方式

- 自动存储 在函数内部定义的常规变量使用自动存储空间，称为

  ```
  自动变量
  ```

  。

  > 只在特定函数被执行时存在。

自动变量时一个`局部变量`，作用域为包含它的`代码块`。通常存储在`栈`中，遵循`后进先出（LIFO）`。

- 静态存储

  - 变量称为静态的方式
    - 在函数外面定义
    - 在声明变量时使用关键字static。

  整个程序执行期间都存在的存储方式（存在于程序的`整个生命周期`）。

- 动态存储 内存池（自由存储空间或堆）用于静态变量和自动变量，且内存是分开的。

- 线程存储（C++11特性）

## 9. 数组替代品 --- 模板类

模板类`vector`和`array`是数组的替代品。

### 9.1 模板类vector

模板类`vector`类似于`string`类，也是一种`动态数组`。

- `vector对象`包含在`vector头文件`中。
- vector包含在名称空间std中，使用`using编译指令`、`using声明`或`std::vector`。
- 模板使用不同的`语法`来指出它存储的`数据类型`。
- vector类使用不用的语法来指定`元素数`。

### 9.2 模板类array（C++11）

位于名称空间`std`中，与数组一样，array对象的`长度固定`，也使用`栈（静态内存分配）`，而不是`自由存储区`。

> 头文件 array。

### 9.3 数组、vector和array的区别

无论是数组、vector对象还是array对象，都可使用`标准数组表示法`来访问各个元素。

从`地址`可知，array对象和数组存储在相同的`内存区域（即栈）`中，vector对象存储在`自由存储区域或堆`中。

可以将一个array对象赋给另一个array对象，对于数组，必须`逐个`元素`复制`数据。

## Footer

© 2022 GitHub, Inc.

Footer navigation[Terms](https://docs.github.com/en/github/site-policy/github-terms-of-service)[Privacy](https://docs.github.com/en/github/site-policy/github-privacy-statement)[Security](https://github.com/security)[Status](https://www.githubstatus.com/)[Docs](https://docs.github.com/)[Contact GitHub](https://support.github.com/?tags=dotcom-footer)[Pricing](https://github.com/pricing)[API](https://docs.github.com/)[Training](https://services.github.com/)[Blog](https://github.blog/)[About](https://github.com/about)

cpp-Primer-Plus-6e-Notes/Chapter04 at master · SolerHo/cpp-Primer-Plus-6e-Notes


## 8 结构体

### 8.1 结构体基本概念

结构体属于用户==自定义的数据类型==，允许用户存储不同的数据类型

### 8.2 结构体定义和使用

**语法：**`struct 结构体名 { 结构体成员列表 }；`

通过结构体创建变量的方式有三种：

- struct 结构体名 变量名
- struct 结构体名 变量名 = { 成员1值 ， 成员2值...}
- 定义结构体时顺便创建变量

**示例：**

```
//结构体定义
struct student
{
	//成员列表
	string name;  //姓名
	int age;      //年龄
	int score;    //分数
}stu3; //结构体变量创建方式3 


int main() {

	//结构体变量创建方式1
	struct student stu1; //struct 关键字可以省略

	stu1.name = "张三";
	stu1.age = 18;
	stu1.score = 100;
	
	cout << "姓名：" << stu1.name << " 年龄：" << stu1.age  << " 分数：" << stu1.score << endl;

	//结构体变量创建方式2
	struct student stu2 = { "李四",19,60 };

	cout << "姓名：" << stu2.name << " 年龄：" << stu2.age  << " 分数：" << stu2.score << endl;


	stu3.name = "王五";
	stu3.age = 18;
	stu3.score = 80;
	

	cout << "姓名：" << stu3.name << " 年龄：" << stu3.age  << " 分数：" << stu3.score << endl;

	system("pause");

	return 0;
}
```

> 总结1：定义结构体时的关键字是struct，不可省略

> 总结2：创建结构体变量时，关键字struct可以省略

> 总结3：结构体变量利用操作符 ''.'' 访问成员

### 8.3 结构体数组

**作用：**将自定义的结构体放入到数组中方便维护

**语法：**` struct  结构体名 数组名[元素个数] = {  {} , {} , ... {} }`

**示例：**

```
//结构体定义
struct student
{
	//成员列表
	string name;  //姓名
	int age;      //年龄
	int score;    //分数
}

int main() {
	
	//结构体数组
	struct student arr[3]=
	{
		{"张三",18,80 },
		{"李四",19,60 },
		{"王五",20,70 }
	};

	for (int i = 0; i < 3; i++)
	{
		cout << "姓名：" << arr[i].name << " 年龄：" << arr[i].age << " 分数：" << arr[i].score << endl;
	}

	system("pause");

	return 0;
}
```

### 8.4 结构体指针

**作用：**通过指针访问结构体中的成员

- 利用操作符 `-> `可以通过结构体指针访问结构体属性

**示例：**

```
//结构体定义
struct student
{
	//成员列表
	string name;  //姓名
	int age;      //年龄
	int score;    //分数
};


int main() {
	
	struct student stu = { "张三",18,100, };
	
	struct student * p = &stu;
	
	p->score = 80; //指针通过 -> 操作符可以访问成员

	cout << "姓名：" << p->name << " 年龄：" << p->age << " 分数：" << p->score << endl;
	
	system("pause");

	return 0;
}
```

> 总结：结构体指针可以通过 -> 操作符 来访问结构体中的成员

### 8.5 结构体嵌套结构体

**作用：** 结构体中的成员可以是另一个结构体

**例如：**每个老师辅导一个学员，一个老师的结构体中，记录一个学生的结构体

**示例：**

```
//学生结构体定义
struct student
{
	//成员列表
	string name;  //姓名
	int age;      //年龄
	int score;    //分数
};

//教师结构体定义
struct teacher
{
    //成员列表
	int id; //职工编号
	string name;  //教师姓名
	int age;   //教师年龄
	struct student stu; //子结构体 学生
};


int main() {

	struct teacher t1;
	t1.id = 10000;
	t1.name = "老王";
	t1.age = 40;

	t1.stu.name = "张三";
	t1.stu.age = 18;
	t1.stu.score = 100;

	cout << "教师 职工编号： " << t1.id << " 姓名： " << t1.name << " 年龄： " << t1.age << endl;
	
	cout << "辅导学员 姓名： " << t1.stu.name << " 年龄：" << t1.stu.age << " 考试分数： " << t1.stu.score << endl;

	system("pause");

	return 0;
}
```

**总结：**在结构体中可以定义另一个结构体作为成员，用来解决实际问题

### 8.6 结构体做函数参数

**作用：**将结构体作为参数向函数中传递

传递方式有两种：

- 值传递
- 地址传递

**示例：**

```
//学生结构体定义
struct student
{
	//成员列表
	string name;  //姓名
	int age;      //年龄
	int score;    //分数
};

//值传递
void printStudent(student stu )
{
	stu.age = 28;
	cout << "子函数中 姓名：" << stu.name << " 年龄： " << stu.age  << " 分数：" << stu.score << endl;
}

//地址传递
void printStudent2(student *stu)
{
	stu->age = 28;
	cout << "子函数中 姓名：" << stu->name << " 年龄： " << stu->age  << " 分数：" << stu->score << endl;
}

int main() {

	student stu = { "张三",18,100};
	//值传递
	printStudent(stu);
	cout << "主函数中 姓名：" << stu.name << " 年龄： " << stu.age << " 分数：" << stu.score << endl;

	cout << endl;

	//地址传递
	printStudent2(&stu);
	cout << "主函数中 姓名：" << stu.name << " 年龄： " << stu.age  << " 分数：" << stu.score << endl;

	system("pause");

	return 0;
}
```

> 总结：如果不想修改主函数中的数据，用值传递，反之用地址传递

### 8.7 结构体中 const使用场景

**作用：**用const来防止误操作

**示例：**

```
//学生结构体定义
struct student
{
	//成员列表
	string name;  //姓名
	int age;      //年龄
	int score;    //分数
};

//const使用场景
void printStudent(const student *stu) //加const防止函数体中的误操作
{
	//stu->age = 100; //操作失败，因为加了const修饰
	cout << "姓名：" << stu->name << " 年龄：" << stu->age << " 分数：" << stu->score << endl;

}

int main() {

	student stu = { "张三",18,100 };

	printStudent(&stu);

	system("pause");

	return 0;
}
```

### 8.8 结构体案例

#### 8.8.1 案例1

**案例描述：**

学校正在做毕设项目，每名老师带领5个学生，总共有3名老师，需求如下

设计学生和老师的结构体，其中在老师的结构体中，有老师姓名和一个存放5名学生的数组作为成员

学生的成员有姓名、考试分数，创建数组存放3名老师，通过函数给每个老师及所带的学生赋值

最终打印出老师数据以及老师所带的学生数据。

**示例：**

```
struct Student
{
	string name;
	int score;
};
struct Teacher
{
	string name;
	Student sArray[5];
};

void allocateSpace(Teacher tArray[] , int len)
{
	string tName = "教师";
	string sName = "学生";
	string nameSeed = "ABCDE";
	for (int i = 0; i < len; i++)
	{
		tArray[i].name = tName + nameSeed[i];
		
		for (int j = 0; j < 5; j++)
		{
			tArray[i].sArray[j].name = sName + nameSeed[j];
			tArray[i].sArray[j].score = rand() % 61 + 40;
		}
	}
}

void printTeachers(Teacher tArray[], int len)
{
	for (int i = 0; i < len; i++)
	{
		cout << tArray[i].name << endl;
		for (int j = 0; j < 5; j++)
		{
			cout << "\t姓名：" << tArray[i].sArray[j].name << " 分数：" << tArray[i].sArray[j].score << endl;
		}
	}
}

int main() {

	srand((unsigned int)time(NULL)); //随机数种子 头文件 #include <ctime>

	Teacher tArray[3]; //老师数组

	int len = sizeof(tArray) / sizeof(Teacher);

	allocateSpace(tArray, len); //创建数据

	printTeachers(tArray, len); //打印数据
	
	system("pause");

	return 0;
}
```

#### 8.8.2 案例2

**案例描述：**

设计一个英雄的结构体，包括成员姓名，年龄，性别;创建结构体数组，数组中存放5名英雄。

通过冒泡排序的算法，将数组中的英雄按照年龄进行升序排序，最终打印排序后的结果。

五名英雄信息如下：

```
		{"刘备",23,"男"},
		{"关羽",22,"男"},
		{"张飞",20,"男"},
		{"赵云",21,"男"},
		{"貂蝉",19,"女"},
```

**示例：**

```
//英雄结构体
struct hero
{
	string name;
	int age;
	string sex;
};
//冒泡排序
void bubbleSort(hero arr[] , int len)
{
	for (int i = 0; i < len - 1; i++)
	{
		for (int j = 0; j < len - 1 - i; j++)
		{
			if (arr[j].age > arr[j + 1].age)
			{
				hero temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}
//打印数组
void printHeros(hero arr[], int len)
{
	for (int i = 0; i < len; i++)
	{
		cout << "姓名： " << arr[i].name << " 性别： " << arr[i].sex << " 年龄： " << arr[i].age << endl;
	}
}

int main() {

	struct hero arr[5] =
	{
		{"刘备",23,"男"},
		{"关羽",22,"男"},
		{"张飞",20,"男"},
		{"赵云",21,"男"},
		{"貂蝉",19,"女"},
	};

	int len = sizeof(arr) / sizeof(hero); //获取数组元素个数

	bubbleSort(arr, len); //排序

	printHeros(arr, len); //打印

	system("pause");

	return 0;
}
```



# 

<details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog" style="box-sizing: border-box; display: block;"><summary data-hotkey="l" aria-label="Jump to line" role="button" style="box-sizing: border-box; display: list-item; cursor: pointer; list-style: none; transition: color 80ms cubic-bezier(0.33, 1, 0.68, 1) 0s, background-color, box-shadow, border-color;"></summary></details>

Give feedback

## 7 指针

### 7.1 指针的基本概念

**指针的作用：** 可以通过指针间接访问内存

- 内存编号是从0开始记录的，一般用十六进制数字表示

- 可以利用指针变量保存地址

  

### 7.2 指针变量的定义和使用

指针变量定义语法： `数据类型 * 变量名；`

**示例：**

```
int main() {

	//1、指针的定义
	int a = 10; //定义整型变量a
	
	//指针定义语法： 数据类型 * 变量名 ;
	int * p;

	//指针变量赋值
	p = &a; //指针指向变量a的地址
	cout << &a << endl; //打印数据a的地址
	cout << p << endl;  //打印指针变量p

	//2、指针的使用
	//通过*操作指针变量指向的内存
	cout << "*p = " << *p << endl;

	system("pause");

	return 0;
}
```

指针变量和普通变量的区别

- 普通变量存放的是数据,指针变量存放的是地址
- 指针变量可以通过" * "操作符，操作指针变量指向的内存空间，这个过程称为解引用

> 总结1： 我们可以通过 & 符号 获取变量的地址

> 总结2：利用指针可以记录地址

> 总结3：对指针变量解引用，可以操作指针指向的内存

### 7.3 指针所占内存空间

提问：指针也是种数据类型，那么这种数据类型占用多少内存空间？

**示例：**

```
int main() {

	int a = 10;

	int * p;
	p = &a; //指针指向数据a的地址

	cout << *p << endl; //* 解引用
	cout << sizeof(p) << endl;
	cout << sizeof(char *) << endl;
	cout << sizeof(float *) << endl;
	cout << sizeof(double *) << endl;

	system("pause");

	return 0;
}
```

> 总结：所有指针类型在32位操作系统下是4个字节

### 7.4 空指针和野指针

**空指针**：指针变量指向内存中编号为0的空间

**用途：**初始化指针变量

**注意：**空指针指向的内存是不可以访问的

**示例1：空指针**

```
int main() {

	//指针变量p指向内存地址编号为0的空间
	int * p = NULL;

	//访问空指针报错 
	//内存编号0 ~255为系统占用内存，不允许用户访问
	cout << *p << endl;

	system("pause");

	return 0;
}
```

**野指针**：指针变量指向非法的内存空间

**示例2：野指针**

```
int main() {

	//指针变量p指向内存地址编号为0x1100的空间
	int * p = (int *)0x1100;

	//访问野指针报错 
	cout << *p << endl;

	system("pause");

	return 0;
}
```

> 总结：空指针和野指针都不是我们申请的空间，因此不要访问。

### 7.5 const修饰指针

const修饰指针有三种情况

1. const修饰指针 --- 常量指针
2. const修饰常量 --- 指针常量
3. const即修饰指针，又修饰常量

**示例：**

```
int main() {

	int a = 10;
	int b = 10;

	//const修饰的是指针，指针指向可以改，指针指向的值不可以更改
	const int * p1 = &a; 
	p1 = &b; //正确
	//*p1 = 100;  报错
	

	//const修饰的是常量，指针指向不可以改，指针指向的值可以更改
	int * const p2 = &a;
	//p2 = &b; //错误
	*p2 = 100; //正确

    //const既修饰指针又修饰常量
	const int * const p3 = &a;
	//p3 = &b; //错误
	//*p3 = 100; //错误

	system("pause");

	return 0;
}
```

> 技巧：看const右侧紧跟着的是指针还是常量, 是指针就是常量指针，是常量就是指针常量

### 7.6 指针和数组

**作用：**利用指针访问数组中元素

**示例：**

```
int main() {

	int arr[] = { 1,2,3,4,5,6,7,8,9,10 };

	int * p = arr;  //指向数组的指针

	cout << "第一个元素： " << arr[0] << endl;
	cout << "指针访问第一个元素： " << *p << endl;

	for (int i = 0; i < 10; i++)
	{
		//利用指针遍历数组
		cout << *p << endl;
		p++;
	}

	system("pause");

	return 0;
}
```

### 7.7 指针和函数

**作用：**利用指针作函数参数，可以修改实参的值

**示例：**

```
//值传递
void swap1(int a ,int b)
{
	int temp = a;
	a = b; 
	b = temp;
}
//地址传递
void swap2(int * p1, int *p2)
{
	int temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

int main() {

	int a = 10;
	int b = 20;
	swap1(a, b); // 值传递不会改变实参

	swap2(&a, &b); //地址传递会改变实参

	cout << "a = " << a << endl;

	cout << "b = " << b << endl;

	system("pause");

	return 0;
}
```

> 总结：如果不想修改实参，就用值传递，如果想修改实参，就用地址传递

### 7.8 指针、数组、函数

**案例描述：**封装一个函数，利用冒泡排序，实现对整型数组的升序排序

例如数组：int arr[10] = { 4,3,6,9,1,2,10,8,7,5 };

**示例：**

```
//冒泡排序函数
void bubbleSort(int * arr, int len)  //int * arr 也可以写为int arr[]
{
	for (int i = 0; i < len - 1; i++)
	{
		for (int j = 0; j < len - 1 - i; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

//打印数组函数
void printArray(int arr[], int len)
{
	for (int i = 0; i < len; i++)
	{
		cout << arr[i] << endl;
	}
}

int main() {

	int arr[10] = { 4,3,6,9,1,2,10,8,7,5 };
	int len = sizeof(arr) / sizeof(int);

	bubbleSort(arr, len);

	printArray(arr, len);

	system("pause");

	return 0;
}
```

> 总结：当数组名传入到函数作为参数时，被退化为指向首元素的指针



## 5 数组

### 5.1 概述

所谓数组，就是一个集合，里面存放了相同类型的数据元素

**特点1：**数组中的每个==数据元素都是相同的数据类型==

**特点2：**数组是由==连续的内存==位置组成的

### 5.2 一维数组

#### 5.2.1 一维数组定义方式

一维数组定义的三种方式：

1. `数据类型  数组名[ 数组长度 ];`
2. `数据类型  数组名[ 数组长度 ] = { 值1，值2 ...};`
3. `数据类型  数组名[ ] = { 值1，值2 ...};`

示例

```
int main() {

	//定义方式1
	//数据类型 数组名[元素个数];
	int score[10];

	//利用下标赋值
	score[0] = 100;
	score[1] = 99;
	score[2] = 85;

	//利用下标输出
	cout << score[0] << endl;
	cout << score[1] << endl;
	cout << score[2] << endl;


	//第二种定义方式
	//数据类型 数组名[元素个数] =  {值1，值2 ，值3 ...};
	//如果{}内不足10个数据，剩余数据用0补全
	int score2[10] = { 100, 90,80,70,60,50,40,30,20,10 };
	
	//逐个输出
	//cout << score2[0] << endl;
	//cout << score2[1] << endl;

	//一个一个输出太麻烦，因此可以利用循环进行输出
	for (int i = 0; i < 10; i++)
	{
		cout << score2[i] << endl;
	}

	//定义方式3
	//数据类型 数组名[] =  {值1，值2 ，值3 ...};
	int score3[] = { 100,90,80,70,60,50,40,30,20,10 };

	for (int i = 0; i < 10; i++)
	{
		cout << score3[i] << endl;
	}

	system("pause");

	return 0;
}
```

> 总结1：数组名的命名规范与变量名命名规范一致，不要和变量重名

> 总结2：数组中下标是从0开始索引

#### 5.2.2 一维数组数组名

一维数组名称的**用途**：

1. 可以统计整个数组在内存中的长度
2. 可以获取数组在内存中的首地址

**示例：**

```
int main() {

	//数组名用途
	//1、可以获取整个数组占用内存空间大小
	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };

	cout << "整个数组所占内存空间为： " << sizeof(arr) << endl;
	cout << "每个元素所占内存空间为： " << sizeof(arr[0]) << endl;
	cout << "数组的元素个数为： " << sizeof(arr) / sizeof(arr[0]) << endl;

	//2、可以通过数组名获取到数组首地址
	cout << "数组首地址为： " << (int)arr << endl;
	cout << "数组中第一个元素地址为： " << (int)&arr[0] << endl;
	cout << "数组中第二个元素地址为： " << (int)&arr[1] << endl;

	//arr = 100; 错误，数组名是常量，因此不可以赋值


	system("pause");

	return 0;
}
```

> 注意：数组名是常量，不可以赋值

> 总结1：直接打印数组名，可以查看数组所占内存的首地址

> 总结2：对数组名进行sizeof，可以获取整个数组占内存空间的大小

**练习案例1**：五只小猪称体重

**案例描述：**

在一个数组中记录了五只小猪的体重，如：int arr[5] = {300,350,200,400,250};

找出并打印最重的小猪体重。

**练习案例2：**数组元素逆置

**案例描述：**请声明一个5个元素的数组，并且将元素逆置.

(如原数组元素为：1,3,2,5,4;逆置后输出结果为:4,5,2,3,1);

#### 5.2.3 冒泡排序

**作用：** 最常用的排序算法，对数组内元素进行排序

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素做同样的工作，执行完毕后，找到第一个最大值。
3. 重复以上的步骤，每次比较次数-1，直到不需要比较

[![1541905327273](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/1541905327273.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/1541905327273.png)

**示例：** 将数组 { 4,2,8,0,5,7,1,3,9 } 进行升序排序

```
int main() {

	int arr[9] = { 4,2,8,0,5,7,1,3,9 };

	for (int i = 0; i < 9 - 1; i++)
	{
		for (int j = 0; j < 9 - 1 - i; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}

	for (int i = 0; i < 9; i++)
	{
		cout << arr[i] << endl;
	}
    
	system("pause");

	return 0;
}
```

### 5.3 二维数组

二维数组就是在一维数组上，多加一个维度。

[![1541905559138](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/assets/1541905559138.png)](https://github.com/Blitzer207/C-Resource/blob/master/第1阶段C%2B%2B 匠心之作 从0到1入门/C%2B%2B基础入门讲义/assets/1541905559138.png)

#### 5.3.1 二维数组定义方式

二维数组定义的四种方式：

1. `数据类型  数组名[ 行数 ][ 列数 ];`
2. `数据类型  数组名[ 行数 ][ 列数 ] = { {数据1，数据2 } ，{数据3，数据4 } };`
3. `数据类型  数组名[ 行数 ][ 列数 ] = { 数据1，数据2，数据3，数据4};`
4. ` 数据类型  数组名[  ][ 列数 ] = { 数据1，数据2，数据3，数据4};`

> 建议：以上4种定义方式，利用==第二种更加直观，提高代码的可读性==

示例：

```
int main() {

	//方式1  
	//数组类型 数组名 [行数][列数]
	int arr[2][3];
	arr[0][0] = 1;
	arr[0][1] = 2;
	arr[0][2] = 3;
	arr[1][0] = 4;
	arr[1][1] = 5;
	arr[1][2] = 6;

	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}

	//方式2 
	//数据类型 数组名[行数][列数] = { {数据1，数据2 } ，{数据3，数据4 } };
	int arr2[2][3] =
	{
		{1,2,3},
		{4,5,6}
	};

	//方式3
	//数据类型 数组名[行数][列数] = { 数据1，数据2 ,数据3，数据4  };
	int arr3[2][3] = { 1,2,3,4,5,6 }; 

	//方式4 
	//数据类型 数组名[][列数] = { 数据1，数据2 ,数据3，数据4  };
	int arr4[][3] = { 1,2,3,4,5,6 };
	
	system("pause");

	return 0;
}
```

> 总结：在定义二维数组时，如果初始化了数据，可以省略行数

#### 5.3.2 二维数组数组名

- 查看二维数组所占内存空间
- 获取二维数组首地址

**示例：**

```
int main() {

	//二维数组数组名
	int arr[2][3] =
	{
		{1,2,3},
		{4,5,6}
	};

	cout << "二维数组大小： " << sizeof(arr) << endl;
	cout << "二维数组一行大小： " << sizeof(arr[0]) << endl;
	cout << "二维数组元素大小： " << sizeof(arr[0][0]) << endl;

	cout << "二维数组行数： " << sizeof(arr) / sizeof(arr[0]) << endl;
	cout << "二维数组列数： " << sizeof(arr[0]) / sizeof(arr[0][0]) << endl;

	//地址
	cout << "二维数组首地址：" << arr << endl;
	cout << "二维数组第一行地址：" << arr[0] << endl;
	cout << "二维数组第二行地址：" << arr[1] << endl;

	cout << "二维数组第一个元素地址：" << &arr[0][0] << endl;
	cout << "二维数组第二个元素地址：" << &arr[0][1] << endl;

	system("pause");

	return 0;
}
```

> 总结1：二维数组名就是这个数组的首地址

> 总结2：对二维数组名进行sizeof时，可以获取整个二维数组占用的内存空间大小

#### **5.3.3 二维数组应用案例**

**考试成绩统计：**

案例描述：有三名同学（张三，李四，王五），在一次考试中的成绩分别如下表，**请分别输出三名同学的总成绩**

|      | 语文 | 数学 | 英语 |
| ---- | ---- | ---- | ---- |
| 张三 | 100  | 100  | 100  |
| 李四 | 90   | 50   | 100  |
| 王五 | 60   | 70   | 80   |

**参考答案：**

```
int main() {

	int scores[3][3] =
	{
		{100,100,100},
		{90,50,100},
		{60,70,80},
	};

	string names[3] = { "张三","李四","王五" };

	for (int i = 0; i < 3; i++)
	{
		int sum = 0;
		for (int j = 0; j < 3; j++)
		{
			sum += scores[i][j];
		}
		cout << names[i] << "同学总成绩为： " << sum << endl;
	}

	system("pause");

	return 0;
}
```

函数基础

> 库函数是已经定义和编译好的函数，同时使用标准库头文件提供原型，只需要正确调用

使用c++函数

- 提供函数定义
- 提供函数原型
- 调用函数

## 定义函数

C++ 中的函数定义的一般形式如下：

```c++
return_type function_name( parameter list ) 
{

    body of the function 

} 
```

在 C++ 中，函数由一个函数头和一个函数主体组成。下面列出一个函数的所有组成部分：

- **返回类型：**一个函数可以返回一个值。**return_type** 是函数返回的值的数据类型。有些函数执行所需的操作而不返回值，在这种情况下，return_type 是关键字 **void**。
- **函数名称：**这是函数的实际名称。函数名和参数列表一起构成了函数签名。
- **参数：**参数就像是占位符。当函数被调用时，您向参数传递一个值，这个值被称为实际参数。参数列表包括函数参数的类型、顺序、数量。参数是可选的，也就是说，函数可能不包含参数。
- **函数主体：**函数主体包含一组定义函数执行任务的语句。

实例：定义一个加法函数，实现两个数相加

```c++
//函数定义
int add(int num1,int num2){
    int sum=sum1+sum2;
    return sum;
}
```

## 函数调用

```c++
//函数调用语法：函数名称（参数）
	int a=10, b=20;
	int c=add(a, b);
	cout << c << endl;
```

## c++传值调用

向函数传递参数的**传值调用**方法，<u>把参数的实际值复制给函数的形式参数</u>。在这种情况下，修改函数内的形式参数不会影响实际参数。

默认情况下，C++ 使用*传值调用*方法来传递参数。一般来说，这意味着函数内的代码不会改变用于调用函数的实际参数。函数 **swap()** 定义如下：

# 函数与数组

## 6 函数

### 6.1 概述

**作用：**将一段经常使用的代码封装起来，减少重复代码

一个较大的程序，一般分为若干个程序块，每个模块实现特定的功能。

### 6.2 函数的定义

函数的定义一般主要有5个步骤：

1、返回值类型

2、函数名

3、参数表列

4、函数体语句

5、return 表达式

**语法：**

```
返回值类型 函数名 （参数列表）
{

       函数体语句

       return表达式

}
```

- 返回值类型 ：一个函数可以返回一个值。在函数定义中
- 函数名：给函数起个名称
- 参数列表：使用该函数时，传入的数据
- 函数体语句：花括号内的代码，函数内需要执行的语句
- return表达式： 和返回值类型挂钩，函数执行完后，返回相应的数据

**示例：**定义一个加法函数，实现两个数相加

```
//函数定义
int add(int num1, int num2)
{
	int sum = num1 + num2;
	return sum;
}
```

### 6.3 函数的调用

**功能：**使用定义好的函数

**语法：**` 函数名（参数）`

**示例：**

```
//函数定义
int add(int num1, int num2) //定义中的num1,num2称为形式参数，简称形参
{
	int sum = num1 + num2;
	return sum;
}

int main() {

	int a = 10;
	int b = 10;
	//调用add函数
	int sum = add(a, b);//调用时的a，b称为实际参数，简称实参
	cout << "sum = " << sum << endl;

	a = 100;
	b = 100;

	sum = add(a, b);
	cout << "sum = " << sum << endl;

	system("pause");

	return 0;
}
```

> 总结：函数定义里小括号内称为形参，函数调用时传入的参数称为实参

### 6.4 值传递

- 所谓值传递，就是函数调用时实参将数值传入给形参
- 值传递时，==如果形参发生，并不会影响实参==

**示例：**

```
void swap(int num1, int num2)
{
	cout << "交换前：" << endl;
	cout << "num1 = " << num1 << endl;
	cout << "num2 = " << num2 << endl;

	int temp = num1;
	num1 = num2;
	num2 = temp;

	cout << "交换后：" << endl;
	cout << "num1 = " << num1 << endl;
	cout << "num2 = " << num2 << endl;

	//return ; 当函数声明时候，不需要返回值，可以不写return
}

int main() {

	int a = 10;
	int b = 20;

	swap(a, b);

	cout << "mian中的 a = " << a << endl;
	cout << "mian中的 b = " << b << endl;

	system("pause");

	return 0;
}
```

> 总结： 值传递时，形参是修饰不了实参的

### **6.5 函数的常见样式**

常见的函数样式有4种

1. 无参无返
2. 有参无返
3. 无参有返
4. 有参有返

**示例：**

```
//函数常见样式
//1、 无参无返
void test01()
{
	//void a = 10; //无类型不可以创建变量,原因无法分配内存
	cout << "this is test01" << endl;
	//test01(); 函数调用
}

//2、 有参无返
void test02(int a)
{
	cout << "this is test02" << endl;
	cout << "a = " << a << endl;
}

//3、无参有返
int test03()
{
	cout << "this is test03 " << endl;
	return 10;
}

//4、有参有返
int test04(int a, int b)
{
	cout << "this is test04 " << endl;
	int sum = a + b;
	return sum;
}
```

### 6.6 函数的声明

**作用：** 告诉编译器函数名称及如何调用函数。函数的实际主体可以单独定义。

- 函数的**声明可以多次**，但是函数的**定义只能有一次**

**示例：**

```
//声明可以多次，定义只能一次
//声明
int max(int a, int b);
int max(int a, int b);
//定义
int max(int a, int b)
{
	return a > b ? a : b;
}

int main() {

	int a = 100;
	int b = 200;

	cout << max(a, b) << endl;

	system("pause");

	return 0;
}
```

### 6.7 函数的分文件编写

**作用：**让代码结构更加清晰

函数分文件编写一般有4个步骤

1. 创建后缀名为.h的头文件
2. 创建后缀名为.cpp的源文件
3. 在头文件中写函数的声明
4. 在源文件中写函数的定义

**示例：**

```
//swap.h文件
#include<iostream>
using namespace std;

//实现两个数字交换的函数声明
void swap(int a, int b);
//swap.cpp文件
#include "swap.h"

void swap(int a, int b)
{
	int temp = a;
	a = b;
	b = temp;

	cout << "a = " << a << endl;
	cout << "b = " << b << endl;
}
//main函数文件
#include "swap.h"
int main() {

	int a = 100;
	int b = 200;
	swap(a, b);

	system("pause");

	return 0;
}
```

# 通讯录管理系统

## 1、系统需求

通讯录是一个可以记录亲人、好友信息的工具。

本教程主要利用C++来实现一个通讯录管理系统

系统中需要实现的功能如下：

- 添加联系人：向通讯录中添加新人，信息包括（姓名、性别、年龄、联系电话、家庭住址）最多记录1000人
- 显示联系人：显示通讯录中所有联系人信息
- 删除联系人：按照姓名进行删除指定联系人
- 查找联系人：按照姓名查看指定联系人信息
- 修改联系人：按照姓名重新修改指定联系人
- 清空联系人：清空通讯录中所有信息
- 退出通讯录：退出当前使用的通讯录

## 2、创建项目

创建项目步骤如下：

- 创建新项目
- 添加文件

### 2.1 创建项目

打开vs2017后，点击创建新项目，创建新的C++项目

[![1544151401138](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544151401138.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544151401138.png)

填写项目名称，选择项目路径

[![1544151579620](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544151579620.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544151579620.png)

### 2.2添加文件

[![1544161551746](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544161551746.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544161551746.png)

[![1544161648175](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544161648175.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544161648175.png)

添加成功后，效果如图：

[![1544162344057](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544162344057.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544162344057.png)

至此，项目已创建完毕

## 3、菜单功能

**功能描述：** 用户选择功能的界面

菜单界面效果如下图：

[![1544149559893](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544149559893.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544149559893.png)

**步骤：**

- 封装函数显示该界面 如 `void showMenu()`
- 在main函数中调用封装好的函数

**代码：**

```
#include<iostream>
using namespace std;

//菜单界面
void showMenu()
{
	cout << "***************************" << endl;
	cout << "*****  1、添加联系人  *****" << endl;
	cout << "*****  2、显示联系人  *****" << endl;
	cout << "*****  3、删除联系人  *****" << endl;
	cout << "*****  4、查找联系人  *****" << endl;
	cout << "*****  5、修改联系人  *****" << endl;
	cout << "*****  6、清空联系人  *****" << endl;
	cout << "*****  0、退出通讯录  *****" << endl;
	cout << "***************************" << endl;
}

int main() {

	showMenu();

	system("pause");

	return 0;
}
```

## 4、退出功能

功能描述：退出通讯录系统

思路：根据用户不同的选择，进入不同的功能，可以选择switch分支结构，将整个架构进行搭建

当用户选择0时候，执行退出，选择其他先不做操作，也不会退出程序

**代码：**

```
int main() {

	int select = 0;

	while (true)
	{
		showMenu();

		cin >> select;
		
		switch (select)
		{
		case 1:  //添加联系人
			break;
		case 2:  //显示联系人
			break;
		case 3:  //删除联系人
			break;
		case 4:  //查找联系人
			break;
		case 5:  //修改联系人
			break;
		case 6:  //清空联系人
			break;
		case 0:  //退出通讯录
			cout << "欢迎下次使用" << endl;
			system("pause");
			return 0;
			break;
		default:
			break;
		}
	}

	system("pause");

	return 0;
}
```

效果图：

[![1544163868043](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544163868043.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544163868043.png)

## 5、添加联系人

功能描述：

实现添加联系人功能，联系人上限为1000人，联系人信息包括（姓名、性别、年龄、联系电话、家庭住址）

添加联系人实现步骤：

- 设计联系人结构体
- 设计通讯录结构体
- main函数中创建通讯录
- 封装添加联系人函数
- 测试添加联系人功能

### 5.1 设计联系人结构体

联系人信息包括：姓名、性别、年龄、联系电话、家庭住址

设计如下：

```
#include <string>  //string头文件
//联系人结构体
struct Person
{
	string m_Name; //姓名
	int m_Sex; //性别：1男 2女
	int m_Age; //年龄
	string m_Phone; //电话
	string m_Addr; //住址
};
```

### 5.2 设计通讯录结构体

设计时候可以在通讯录结构体中，维护一个容量为1000的存放联系人的数组，并记录当前通讯录中联系人数量

设计如下

```
#define MAX 1000 //最大人数

//通讯录结构体
struct Addressbooks
{
	struct Person personArray[MAX]; //通讯录中保存的联系人数组
	int m_Size; //通讯录中人员个数
};
```

### 5.3 main函数中创建通讯录

添加联系人函数封装好后，在main函数中创建一个通讯录变量，这个就是我们需要一直维护的通讯录

```
mian函数起始位置添加：

	//创建通讯录
	Addressbooks abs;
	//初始化通讯录中人数
	abs.m_Size = 0;
```

### 5.4 封装添加联系人函数

思路：添加联系人前先判断通讯录是否已满，如果满了就不再添加，未满情况将新联系人信息逐个加入到通讯录

添加联系人代码：

```
//1、添加联系人信息
void addPerson(Addressbooks *abs)
{
	//判断电话本是否满了
	if (abs->m_Size == MAX)
	{
		cout << "通讯录已满，无法添加" << endl;
		return;
	}
	else
	{
		//姓名
		string name;
		cout << "请输入姓名：" << endl;
		cin >> name;
		abs->personArray[abs->m_Size].m_Name = name;

		cout << "请输入性别：" << endl;
		cout << "1 -- 男" << endl;
		cout << "2 -- 女" << endl;

		//性别
		int sex = 0;
		while (true)
		{
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[abs->m_Size].m_Sex = sex;
				break;
			}
			cout << "输入有误，请重新输入";
		}

		//年龄
		cout << "请输入年龄：" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[abs->m_Size].m_Age = age;

		//联系电话
		cout << "请输入联系电话：" << endl;
		string phone = "";
		cin >> phone;
		abs->personArray[abs->m_Size].m_Phone = phone;

		//家庭住址
		cout << "请输入家庭住址：" << endl;
		string address;
		cin >> address;
		abs->personArray[abs->m_Size].m_Addr = address;

		//更新通讯录人数
		abs->m_Size++;

		cout << "添加成功" << endl;
		system("pause");
		system("cls");
	}
}
```

### 5.5 测试添加联系人功能

选择界面中，如果玩家选择了1，代表添加联系人，我们可以测试下该功能

在switch case 语句中，case1里添加：

```
case 1:  //添加联系人
	addPerson(&abs);
	break;
```

测试效果如图：

[![1544165554002](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544165554002.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544165554002.png)

## 6、显示联系人

功能描述：显示通讯录中已有的联系人信息

显示联系人实现步骤：

- 封装显示联系人函数
- 测试显示联系人功能

### 6.1 封装显示联系人函数

思路：判断如果当前通讯录中没有人员，就提示记录为空，人数大于0，显示通讯录中信息

显示联系人代码：

```
//2、显示所有联系人信息
void showPerson(Addressbooks * abs)
{
	if (abs->m_Size == 0)
	{
		cout << "当前记录为空" << endl;
	}
	else
	{
		for (int i = 0; i < abs->m_Size; i++)
		{
			cout << "姓名：" << abs->personArray[i].m_Name << "\t";
			cout << "性别：" << (abs->personArray[i].m_Sex == 1 ? "男" : "女") << "\t";
			cout << "年龄：" << abs->personArray[i].m_Age << "\t";
			cout << "电话：" << abs->personArray[i].m_Phone << "\t";
			cout << "住址：" << abs->personArray[i].m_Addr << endl;
		}
	}
	
	system("pause");
	system("cls");

}
```

### 6.2 测试显示联系人功能

在switch case语句中，case 2 里添加

```
case 2:  //显示联系人
	showPerson(&abs);
	break;
```

测试效果如图：

[![1544166401582](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544166401582.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544166401582.png)

## 7、删除联系人

功能描述：按照姓名进行删除指定联系人

删除联系人实现步骤：

- 封装检测联系人是否存在
- 封装删除联系人函数
- 测试删除联系人功能

### 7.1 封装检测联系人是否存在

设计思路：

删除联系人前，我们需要先判断用户输入的联系人是否存在，如果存在删除，不存在提示用户没有要删除的联系人

因此我们可以把检测联系人是否存在封装成一个函数中，如果存在，返回联系人在通讯录中的位置，不存在返回-1

检测联系人是否存在代码：

```
//判断是否存在查询的人员，存在返回在数组中索引位置，不存在返回-1
int isExist(Addressbooks * abs, string name)
{
	for (int i = 0; i < abs->m_Size; i++)
	{
		if (abs->personArray[i].m_Name == name)
		{
			return i;
		}
	}
	return -1;
}
```

### 7.2 封装删除联系人函数

根据用户输入的联系人判断该通讯录中是否有此人

查找到进行删除，并提示删除成功

查不到提示查无此人。

```
//3、删除指定联系人信息
void deletePerson(Addressbooks * abs)
{
	cout << "请输入您要删除的联系人" << endl;
	string name;
	cin >> name;

	int ret = isExist(abs, name);
	if (ret != -1)
	{
		for (int i = ret; i < abs->m_Size; i++)
		{
			abs->personArray[i] = abs->personArray[i + 1];
		}
         abs->m_Size--;
		cout << "删除成功" << endl;
	}
	else
	{
		cout << "查无此人" << endl;
	}

	system("pause");
	system("cls");
}
```

### 7.3 测试删除联系人功能

在switch case 语句中，case3里添加：

```
case 3:  //删除联系人
	deletePerson(&abs);
	break;
```

测试效果如图：

存在情况：

[![1544167951559](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544167951559.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544167951559.png)

不存在情况：

[![1544168010831](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544168010831.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544168010831.png)

## 8、查找联系人

功能描述：按照姓名查看指定联系人信息

查找联系人实现步骤

- 封装查找联系人函数
- 测试查找指定联系人

### 8.1 封装查找联系人函数

实现思路：判断用户指定的联系人是否存在，如果存在显示信息，不存在则提示查无此人。

查找联系人代码：

```
//4、查找指定联系人信息
void findPerson(Addressbooks * abs)
{
	cout << "请输入您要查找的联系人" << endl;
	string name;
	cin >> name;

	int ret = isExist(abs, name);
	if (ret != -1)
	{
		cout << "姓名：" << abs->personArray[ret].m_Name << "\t";
		cout << "性别：" << abs->personArray[ret].m_Sex << "\t";
		cout << "年龄：" << abs->personArray[ret].m_Age << "\t";
		cout << "电话：" << abs->personArray[ret].m_Phone << "\t";
		cout << "住址：" << abs->personArray[ret].m_Addr << endl;
	}
	else
	{
		cout << "查无此人" << endl;
	}

	system("pause");
	system("cls");

}
```

### 8.2 测试查找指定联系人

在switch case 语句中，case4里添加：

```
case 4:  //查找联系人
	findPerson(&abs);
	break;
```

测试效果如图

存在情况：

[![1544170057646](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544170057646.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544170057646.png)

不存在情况：

[![1544170254021](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544170254021.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544170254021.png)

## 9、修改联系人

功能描述：按照姓名重新修改指定联系人

修改联系人实现步骤

- 封装修改联系人函数
- 测试修改联系人功能

### 9.1 封装修改联系人函数

实现思路：查找用户输入的联系人，如果查找成功进行修改操作，查找失败提示查无此人

修改联系人代码：

```
//5、修改指定联系人信息
void modifyPerson(Addressbooks * abs)
{
	cout << "请输入您要修改的联系人" << endl;
	string name;
	cin >> name;

	int ret = isExist(abs, name);
	if (ret != -1)
	{
		//姓名
		string name;
		cout << "请输入姓名：" << endl;
		cin >> name;
		abs->personArray[ret].m_Name = name;

		cout << "请输入性别：" << endl;
		cout << "1 -- 男" << endl;
		cout << "2 -- 女" << endl;

		//性别
		int sex = 0;
		while (true)
		{
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[ret].m_Sex = sex;
				break;
			}
			cout << "输入有误，请重新输入";
		}

		//年龄
		cout << "请输入年龄：" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[ret].m_Age = age;

		//联系电话
		cout << "请输入联系电话：" << endl;
		string phone = "";
		cin >> phone;
		abs->personArray[ret].m_Phone = phone;

		//家庭住址
		cout << "请输入家庭住址：" << endl;
		string address;
		cin >> address;
		abs->personArray[ret].m_Addr = address;

		cout << "修改成功" << endl;
	}
	else
	{
		cout << "查无此人" << endl;
	}

	system("pause");
	system("cls");

}
```

### 9.2 测试修改联系人功能

在switch case 语句中，case 5里添加：

```
case 5:  //修改联系人
	modifyPerson(&abs);
	break;
```

测试效果如图：

查不到指定联系人情况：

[![1544172265676](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544172265676.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544172265676.png)

查找到联系人，并修改成功：

[![1544172164141](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544172164141.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544172164141.png)

再次查看通讯录，确认修改完毕

[![1544172228627](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544172228627.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544172228627.png)

## 10、清空联系人

功能描述：清空通讯录中所有信息

清空联系人实现步骤

- 封装清空联系人函数
- 测试清空联系人

### 10.1 封装清空联系人函数

实现思路： 将通讯录所有联系人信息清除掉，只要将通讯录记录的联系人数量置为0，做逻辑清空即可。

清空联系人代码：

```
//6、清空所有联系人
void cleanPerson(Addressbooks * abs)
{
	abs->m_Size = 0;
	cout << "通讯录已清空" << endl;
	system("pause");
	system("cls");
}
```

### 10.2 测试清空联系人

在switch case 语句中，case 6 里添加：

```
case 6:  //清空联系人
	cleanPerson(&abs);
	break;
```

测试效果如图：

清空通讯录

[![1544172909693](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544172909693.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544172909693.png)

再次查看信息，显示记录为空

[![1544172943653](https://github.com/Blitzer207/C-Resource/raw/master/%E7%AC%AC2%E9%98%B6%E6%AE%B5%E5%AE%9E%E6%88%98-%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86/%E9%80%9A%E8%AE%AF%E5%BD%95%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AE%B2%E4%B9%89/assets/1544172943653.png)](https://github.com/Blitzer207/C-Resource/blob/master/第2阶段实战-通讯录管理/通讯录管理系统讲义/assets/1544172943653.png)

**至此，通讯录管理系统完成！**