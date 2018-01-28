#自定义lambda函数
double=lambda x:x*2;
#输入值
print("自定义lambda函数\t",double(5));

#自定义函数
def doublet(x):
    return x*2;

print("自定义函数\t",doublet(5));

# 过滤偶数filter函数
my_list = [1, 5, 4, 6, 8, 11, 3, 12];
new_list = list(filter(lambda x:(x%2==0),my_list));

# 输出: [4, 6, 8, 12]
print(new_list);


#map函数,第个元素乘以2
new_map=[1,2,3,4,5,6,7,8,9];
new_map=list(map(lambda x:x*2,new_map));
print(new_map);