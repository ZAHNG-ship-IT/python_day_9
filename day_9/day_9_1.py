#####import import 对比 from(特定模块)更高效吧，因为可以省略导入库的部分
##例如 import math 要算平方根  math.sqrt
####而import math from  sqrt()


from math import sqrt
# ###print(sqrt(9))
#####import import 对比 from(特定模块) as(可以起名)
from math import sqrt as a
print(a(9))#显然，输出结果完全不变!!!!!!!!


######   from 模块 import *   导入全部模块   但是不推荐，命名冲突