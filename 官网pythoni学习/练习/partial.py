import functools;

def te(*args,**keys):
    print(args);
    print(keys);



p1=functools.partial(te,1,2,3);

p1();
p1(4,5,6);