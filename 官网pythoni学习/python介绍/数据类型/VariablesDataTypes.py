'''
Python变量和数据类型
一、Python变量
    1.变量是用于存储某些数据（值）的内存中的一个位置。
    2.它们被赋予独特的名称来区分不同的记忆位置。编写变量名的规则与Python中编写标识符的规则相同。
    3.在使用之前，我们不需要声明一个变量。
        a.在Python中，我们只需为变量分配一个值即可。我们甚至不必声明变量的类型。
        b.这是根据我们分配给变量的值的类型在内部处理的。
二、变量赋值
    我们使用赋值运算符（=）为变量赋值。任何类型的值都可以分配给任何有效的变量。
    a = 5
    b = 3.2
    c = "Hello"
    在这里，我们有三个赋值语句。5是分配给变量a的整数。
    3.2是一个浮点数，分别"Hello"是分配给变量b和c的字符串（字符序列）。

三、多个变量进行赋值
    在Python中，可以在单个语句中进行多个分配，如下所示：
    a, b, c = 5, 3.2, "Hello"
    如果我们要同时为多个变量分配相同的值，我们可以这样做
    x = y = z = "same"
    这将为所有三个变量分配“相同”字符串。
四、python中的数据类型
    Python中的每个值都有一个数据类型。由于一切都是Python编程中的对象，数据类型实际上是类，变量是这些类的实例（对象）。
    Python中有各种数据类型。以下列出了一些重要类型。
    Python中数据类型包含：
        数字类型：1）整型   2）浮点类型（float）
        字符串类型：
        列表类型：
        字典类型：
        集合类型：
        元组类型：

    1、Python数字类型
        a、整数，浮点数和复数落在Python数字类别之下。他们被定义为int，float并complex在Python类。
        b、 我们可以使用该type()函数来知道一个变量或一个值属于哪个类，以及isinstance()检查一个对象是否属于一个特定类的函数。
        c、整数可以是任何长度，它只受到可用内存的限制。
        d、浮点数精确到15位小数位。整数和浮点用小数点分隔。1是整数，1.0是浮点数。
    注意：
        复数以形式写入x + yj，其中x是实部，y是虚部。这里有些例子。
        >>> a = 1234567890123456789
        >>> a
        1234567890123456789
        >>> b = 0.1234567890123456789
        >>> b
        0.12345678901234568
        >>> c = 1+2j
        >>> c
        (1+2j)
        注意float变量b被截断。

    2、Python列表（类似Java中的数组）
        a、列表是有序的项目顺序。它是Python中最常用的数据类型之一，非常灵活。
        b、列表中的所有项目不需要是相同类型的。
        c、宣布一个列表是非常简单的。用逗号分隔的项目用括号[]括起来。
        d、列表是可变的，意思是，列表的元素的值可以被改变。
        >>> a = [1, 2.2, 'python']
        我们可以使用切片运算符[]从列表中提取项目或一系列项目。索引在Python中从0开始。

        a = [5,10,15,20,25,30,35,40]
        1）.获取某个下标的值
            ＃a[2] = 15
            print（“a [2] =”，a [2]）
        2）.获取某个范围的值
            ＃a [0：3] = [ 5，10，15]
            print（“a [0：3] =”，a [0：3]）
        3）.从第几个值读，读取到最后
            ＃a [5：] = [30,35,40]
            print（“a [5：] =一个[5：]）
            >>> a = [1,2,3]
            >>> a[2]=4
            >>> a
            [1, 2, 4]
    3、Python元组
        1）、元组是与列表相同的有序序列。唯一的区别是元组是不可变的。创建的元组无法修改。
        2）、元组用于写保护数据，通常比列表快，因为它不能动态更改。
        3）、它在括号（）中定义，其中项目用逗号分隔。
             >>> t = (5,'program', 1+3j)
       4）、 我们可以使用切片操作符[]来提取项目，但是我们不能更改其值。
            t = (5,'program', 1+3j)
            a、通过下标获取值
            # t[1] = 'program'
            print("t[1] = ", t[1])
            b、设定一个范围获取值
            # t[0:3] = (5, 'program', (1+3j))
            print("t[0:3] = ", t[0:3])

            # Generates error
             # 元组的值不能改变
            t[0] = 10

    4、Python字符串
        1）字符串是Unicode字符的序列。我们可以使用单引号或双引号来表示字符串。
        2）多行字符串可以使用三重引号'''或"""。
            >>> s = "This is a string"
            >>> s = '''a multiline
            像列表和元组一样，切片操作符[]可以与字符串一起使用。
        3）字符串是不可变的。
            s = 'Hello world!'
            # s[4] = 'o'
            print("s[4] = ", s[4])

            # s[6:11] = 'world'
            print("s[6:11] = ", s[6:11])

            # Generates error
            # 字符串在Python中是不可变的
            s[5] ='d'
    5、Python集合
        a、Set是一个无序的独特项目集合。集合由大括号{}中的逗号分隔的值定义。一组中的项目未订购。
            a = {5,2,3,1,4}
            # 输出集合的值
            print("a = ", a)

            # 判断数据的类型
            print(type(a))
        b、我们可以执行两套集合操作，如联合，交集。设置有唯一的值。他们消除重复。
            >>> a = {1,2,2,3,3,3}
            >>> a
            {1, 2, 3}
        c、set是无序集合，索引没有意义。因此切片操作符[]不起作用。
            >>> a = {1,2,3}
            >>> a[1]
            Traceback (most recent call last):
              File "<string>", line 301, in runcode
              File "<interactive input>", line 1, in <module>
            TypeError: 'set' object does not support indexing

    6、Python词典
        1）字典是键值对的无序集合。

        2）当我们有大量的数据时通常使用它。字典优化用于检索数据。我们必须知道检索值的关键。
        3） 在Python中，字典在大括号{}中定义，每个项目都是表单中的一个key:value。钥匙和价值可以是任何类型。
            >>> d = {1:'value','key':2}
            >>> type(d)
            <class 'dict'>
        4）我们可以用key来检索相应的值。但不是相反。
            d = {1:'value','key':2}
            #判断数据的类型
            print(type(d))
            print("d[1] = ", d[1]);
            print("d['key'] = ", d['key']);
            #生成错误
            print("d[2] = ", d[2]);


五、数据类型之间的转换
    1）我们可以通过使用不同的类型转换函数，如int（），float（），str（）等来转换不同的数据类型。
        >>> float(5)
        5.0
    2）从float到int的转换将会截断值（使其接近零）。
        >>> int(10.6)
        10
        >>> int(-10.6)
        -10
    3）字符串的转换必须包含兼容值。
        >>> float('2.5')
        2.5
        >>> str(25)
        '25'
        >>> int('1p')
        Traceback (most recent call last):
          File "<string>", line 301, in runcode
          File "<interactive input>", line 1, in <module>
        ValueError: invalid literal for int() with base 10: '1p'
    5）我们甚至可以将一个序列转换为另一个序列。
        >>> set([1,2,3])
        {1, 2, 3}
        >>> tuple({5,6,7})
        (5, 6, 7)
        >>> list('hello')
        ['h', 'e', 'l', 'l', 'o']
    6）要转换为字典，每个元素必须是一对
        >>> dict([[1,2],[3,4]])
        {1: 2, 3: 4}
        >>> dict([(3,26),(4,44)])
        {3: 26, 4: 44}
'''



