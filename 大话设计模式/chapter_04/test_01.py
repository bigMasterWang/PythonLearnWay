# coding=utf-8
# 2. 考研求职两不误----开放-封闭原则
# 开放,封闭原则, 是说软件实体(类, 模块, 函数等等)应该可以扩展, 但是不可修改, 对扩展开放, 对修改关闭
# 绝对的对修改关闭是不可能的
# 无论模块是多么的'封闭', 都会存在一些无法对之封闭的变化. 既然不可能完全封闭, 设计人员必须对于他设计的模块
# 应该应对哪种变化封闭走出选择, 也就是猜测, 但是大部分猜不到, 所以在我们最初编写代码时, 假设变化不会发生
# 当变化发生时, 我们就创建抽象来隔离以后发生的同类变化, 之后面对需求, 对程序的改动是通过增加新代码进行的, 而不是
# 更改现有的代码

# 总体来讲, 如果有修改的话, 就考虑对修改的部分进行抽象, 然而对于应用程序中的
# 每个部分都刻意地进行抽象同样不是一个好主意, 拒绝不成熟的抽象和抽象本身一样重要

# 总之, 有修改就尝试抽象, 抽象不好就算了