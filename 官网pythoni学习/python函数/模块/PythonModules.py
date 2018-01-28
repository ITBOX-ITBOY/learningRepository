#导入模块和命名
import example as e;
import imp;
import sys;
#调用模块中的函数名
print(e.add(5,5));
#输出路径
print(dir(e));
#重新加载路径
imp.reload(e);
#获取系统的路径
print(sys.path);
#打印出当前模块中的所有模块函数
print(dir())
