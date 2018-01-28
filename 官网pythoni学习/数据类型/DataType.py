from decimal import Decimal as D
# Output: Decimal('3.3')
print(D('1.1') + D('2.2'))

# Output: Decimal('3.000')
print(D('1.2') * D('2.50'))

import fractions as f;
#创建分数
print(f.Fraction(1.3));

print(f.Fraction(5));

print(f.Fraction("1.2"));

from fractions import Fraction as F

# 输出: 2/3
print(F(1, 3) + F(1, 3))

# 输出: 6/5
print(1 / F(5, 6))

# 输出: False
print(F(-3, 10) > 0)

# 输出: True
print(F(-3, 10) < 0)



#集合
my_list=[];
my_list.append(1);
my_list.append(2);
my_list.append(3);
my_list.append(4);


del my_list[1];
print(my_list);

pows=[2**x for x in range(10) if x>5];
print(pows);
print(sum(pows));
print(sorted(pows));
print(len(pows));

for i in pows:
    print(i);

