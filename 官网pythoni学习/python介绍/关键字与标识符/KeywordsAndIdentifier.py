'''
变量的代码操作
'''
a=20;
b="27";
c=2.0;

print("a的值是a=",a);
print("a的值是a="+b);

print(float(20));
print(int(c));
#集合
testList=list({1,2,3,4,5,6,7,8,9});
print(testList);
print(type(testList));

testSet=set([1,2,3]);
print(testSet);
print(type(testSet));
#字典
d=dict([[1,2],[3,4],[5,6]]);
print(d);



#元组
t=tuple([1,2,3,4,5,2,3,3]);
#打印元组的内容
print(t);
#打印元组中某个下标的值
print(t[0]);
#获取元组中某个元素的值
print(t.index(2));
#获取元组中某个元素出现的个数
print(t.count(3));
