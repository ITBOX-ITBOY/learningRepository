name="wangjiucheng";
'''
print(name[0]);
print(len(name));
for i in name:
    print(i);
    
    
print(name[::2]);
print(name[0:2]);
print(name[2:])
print(name[-1::-1]);
print(name.find("w"));
print(name.rfind("n"));
print(name.index("w"));

tit="this is test";
print(tit.title())

print(tit.lower());
print(tit.upper());
test="this is  test";
print(test.center(50));
print(test.rjust(50));
print(test.ljust(50));

test="      waangjiucheng       ";
print(test.lstrip());
print(test.rstrip());
print(test.strip());

test="this is test t";
print(test.partition("t"));
print(test.rpartition("t"));
names=["wan","tt","gg","dd","ff","yy"];
names1=["1","2","3","4","5","6"];
names.extend(names1);
print(names);

'''



names=["1","2","3","4","5"];
print(names.pop());
print(names.pop());
print(names.pop());


nameskey={"name":"wang","age":20};

print(nameskey.items())
for n in nameskey.values():
    print(n);


for a,b in nameskey.items():
    print(a,b);

print(id(nameskey))