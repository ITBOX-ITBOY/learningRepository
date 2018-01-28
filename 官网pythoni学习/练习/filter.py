
import functools;

ref=filter(lambda x : x%2,[1,2,3,4,5,6,7,8,9]);
for t in ref:
    print(t);

print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]));
print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5],6));

class te1(object):
    def __getattr__(self, item):
        return self;
    def __setattr__(self, key, value):
        return self;
