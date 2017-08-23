#import sendmsg
#sendmsg.test1()

from sendmsg import test1,test2
test1()

# 使用 * 导入，如果导入多个，同名时，后面会替换前面的
from sendmsg import *


import time as tt
tt.sleep(3)
