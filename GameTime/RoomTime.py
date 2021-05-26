# coding=utf-8
import time


class RoomTime(object):
    """
    1. 根据代码大全进行更改和, 加上重构
    2. 最后别忘了加入防御式编程
    """

    def __init__(self, rate, start_time='0:0:0'):
        """

        :type rate: float
        :type start_time: str
        """
        super(RoomTime, self).__init__()
        # 现实世界过一秒, 游戏里面过几秒
        self._rate = rate

        self._current_hours = int(start_time.split(':')[0])
        self._current_minutes = int(start_time.split(':')[1])
        self._current_seconds = int(start_time.split(':')[2])

        self._pre_real_time = time.time()
        self._pre_game_time = RoomTime.calculate_game_time_seconds(self._current_hours,
                                                                   self._current_minutes,
                                                                   self._current_seconds)
        self.task_manager = RoomTaskManager()

    def tick(self):
        """
        第一种实现方式, 在别的类的循环里面写
        第二种实现方式, 用Timer.addTimer()进行自我循环
        """
        # 第一种实现方式
        self._current_seconds += (time.time() - self._pre_real_time) * self._rate

        if self._current_seconds >= 60:
            self._current_minutes += int(self._current_seconds / 60)
            self._current_seconds %= 60

        if self._current_minutes >= 60:
            self._current_hours += int(self._current_minutes / 60)
            self._current_minutes %= 60

        if self._current_hours >= 24:
            self._current_hours %= 24

        self._pre_real_time = time.time()

        current_game_seconds = RoomTime.calculate_game_time_seconds(self._current_hours,
                                                                    self._current_minutes,
                                                                    self._current_seconds)
        self.task_manager.execute_task(self._pre_game_time, current_game_seconds)

        self._pre_game_time = current_game_seconds


    def set_rate(self, rate):
        self._rate = rate

    def get_time(self):
        return RoomTime.format_game_time(self._current_hours, self._current_minutes, self._current_seconds)

    def set_time(self, time_str):
        self._current_seconds = float(time_str.split(':')[0])
        self._current_minutes = float(time_str.split(':')[1])
        self._current_hours = float(time_str.split(':')[2])

    @staticmethod
    def format_game_time(hours, minutes, seconds):
        return str(hours) + ':' + str(minutes) + ':' + str(seconds)

    @staticmethod
    def parse_game_time_str(game_time_str):
        return int(game_time_str.split(':')[0]), int(game_time_str.split(':')[1]), int(game_time_str.split(':')[2])

    @staticmethod
    def calculate_game_time_seconds(game_time_hours, game_time_minutes, game_time_seconds):
        return 3600 * game_time_hours + 60 * game_time_minutes + game_time_seconds

    def update_on_day(self, entity_id, target_time_str, is_repeat, method, *args, **kwargs):
        """
        每天的特定时间执行
        之后更正 entity的存在与否的问题, 如果不存在, 该entity的所有方法全部消失
        其实不存在这样的问题. 因为这个实例本身就是和avatar绑定在一起的, avatar消失了, 这个类自然也就没了. 什么定时任务啥的,
        也都没有了
        """
        hours, minutes, seconds = RoomTime.parse_game_time_str(target_time_str)
        target_time = RoomTime.calculate_game_time_seconds(hours, minutes, seconds)
        task = RoomTimeTask(entity_id, target_time, is_repeat, method, *args, **kwargs)
        self.task_manager.add_task(task)

    def add_time(self, entity, delay, method, *args, **kwargs):
        pass


class RoomTaskManager(object):

    def __init__(self):
        super(RoomTaskManager, self).__init__()
        self.timed_tasks = []

    def add_task(self, task):
        """
        :type task: RoomTimeTask
        """
        self.timed_tasks.append(task)

    def execute_task(self, pre_game_seconds, current_game_seconds):
        for task in self.timed_tasks[::-1]:
            if not task.exist():
                self.timed_tasks.remove(task)
                continue
            if not task.can_execute(pre_game_seconds, current_game_seconds):
                continue

            task.execute_task()
            if not task.is_repeat():
                self.timed_tasks.remove(task)


class RoomTimeTask(object):

    def __init__(self, entity_id, target_time, is_repeat, method, *args, **kwargs):
        super(RoomTimeTask, self).__init__()
        self._entity_id = entity_id
        self._target_time = target_time
        self._is_repeat = is_repeat
        self._method = method
        self._args = args
        self._kwargs = kwargs

    def exist(self):
        """
        判断该任务是否还存在:
            1. 如果有entity, 那么EntityManager判断该entity已经消失, 那么就把该任务消失
        """
        if self._entity_id is None:
            return True
        return True

    def is_repeat(self):
        return self._is_repeat

    def can_execute(self, pre_game_seconds, current_game_seconds):
        """
        根据时间来判断该任务是否能够执行
        """
        today_task = pre_game_seconds <= self._target_time <= current_game_seconds
        if today_task:
            return True

        yesterday_evening_not_execute_task = current_game_seconds < pre_game_seconds <= self._target_time
        today_morning_not_execute_task = self._target_time <= current_game_seconds < pre_game_seconds
        if yesterday_evening_not_execute_task or today_morning_not_execute_task:
            return True
        return False

    def execute_task(self):
        self._method(*self._args, **self._kwargs)


class TestClassOne(object):

    def __init__(self):
        super(TestClassOne, self).__init__()

    def my_func(self, event):
        print 'hello world'
        print event


event = {'1': 1, '2': 2}
one = TestClassOne()
room = RoomTime(1, '0:0:0')
room.update_on_day(None,
                   '0:0:5',
                   False,
                   one.my_func,
                   event)

while True:
    room.tick()
    time.sleep(1)
    print room.get_time()



# class TestClass(object):
#
#     def __init__(self):
#         super(TestClass, self).__init__()
#
#     def test_method(self):
#         test_room_test.update_on_day(None, '0:10:0', True, self.hello_world, 'hello world', 'my name is william')
#
#     def hello_world(self, str1, str2):
#         print 'test ', str1, str2
#
#
# test_room_test = RoomTime(1, '0:0:0')
# a = TestClass()
# a.test_method()
#
# while True:
#     test_room_test.tick()
#     time.sleep(1)
