# -*- coding: utf-8 -*-


import time
# from common.EntityManager import EntityManager


class RoomTime(object):

	def __init__(self , rate , start_time='00:00:00' , start_days='1'):
		"""

        :type rate: float
        :type start_time: str
        """
		super(RoomTime , self).__init__()
		# 现实世界过一秒, 游戏里面过几秒
		self._rate = rate

		self._current_days = int(start_days)
		self._current_hours = int(start_time.split(':')[0])
		self._current_minutes = int(start_time.split(':')[1])
		self._current_seconds = int(start_time.split(':')[2])

		# 新加入,用时间戳来代替 天时分秒
		self._start_game_time = 86400 * self._current_days + 3600 * self._current_hours + 60 * self._current_minutes + self._current_seconds
		self._current_game_time = None
		self._start_real_time = time.time()

		self._pre_real_time = time.time()
		self._pre_game_time = RoomTime.calculate_game_time_seconds(self._current_hours , self._current_minutes ,
																   self._current_seconds)
		self.task_manager = RoomTaskManager()

	def tick(self):
		self._current_game_time = self._start_game_time + (time.time() - self._start_real_time) * self._rate
		self.task_manager.execute_task(self._current_game_time)

	# def tick(self):
	# 	self._current_seconds += (time.time() - self._pre_real_time) * self._rate
	#
	# 	if self._current_seconds >= 60:
	# 		self._current_minutes += int(self._current_seconds / 60)
	# 		self._current_seconds %= 60
	#
	# 	if self._current_minutes >= 60:
	# 		self._current_hours += int(self._current_minutes / 60)
	# 		self._current_minutes %= 60
	#
	# 	if self._current_hours >= 24:
	# 		self._current_days += int(self._current_hours / 24)
	# 		self._current_hours %= 24
	#
	# 	self._pre_real_time = time.time()
	#
	# 	current_game_seconds = RoomTime.calculate_game_time_seconds(self._current_hours,
	# 																self._current_minutes,
	# 																self._current_seconds)
	# 	self.task_manager.execute_task(self._pre_game_time, current_game_seconds)
	#
	# 	self._pre_game_time = current_game_seconds

	def set_rate(self , rate):
		self._rate = rate

	def get_rate(self):
		return self._rate

	def update_on_day(self , entity_id , target_time_str , is_repeat , method , *args , **kwargs):
		# 注册定时任务
		if len(target_time_str.split(':')) == 2:
			target_time_str += ':00'
		hours , minutes , seconds = RoomTime.parse_game_time_str(target_time_str)
		target_time = RoomTime.calculate_game_time_seconds(hours , minutes , seconds)
		task = RoomTimeTask(entity_id , target_time , is_repeat , method , *args , **kwargs)
		self.task_manager.add_task(task)

	def add_delay(self , entity_id , delay , is_repeat , method , *args , **kwargs):
		# 注册延时任务
		game_delay = delay * self._rate
		target_time = self._current_hours * 3600 + self._current_minutes * 60 + self._current_seconds + game_delay
		task = RoomTimeTask(entity_id , target_time , is_repeat , method , *args , **kwargs)
		self.task_manager.add_task(task)

	def clear_room_task(self):
		# 清空任务列表
		self.task_manager.timed_tasks = []

	def should_execute_add_npc_task_right_now(self , start_time_str , end_time_str):
		# 判断添加npc的事件是否应该立即执行
		start_time = RoomTime.calculate_game_time_seconds(*RoomTime.parse_game_time_str(start_time_str))
		end_time = RoomTime.calculate_game_time_seconds(*RoomTime.parse_game_time_str(end_time_str))
		current_time = RoomTime.calculate_game_time_seconds(*RoomTime.parse_game_time_str(self.get_time()))
		if start_time <= current_time <= end_time:
			return True
		return False

	def should_execute_pq_task_right_now(self , start_time_str , end_time_str):
		return self.should_execute_add_npc_task_right_now(start_time_str , end_time_str)

	def should_execute_add_monster_right_now(self , start_time_str):
		# 判断添加monster的事件是否应该立即执行
		start_time = RoomTime.calculate_game_time_seconds(*RoomTime.parse_game_time_str(start_time_str))
		current_time = RoomTime.calculate_game_time_seconds(*RoomTime.parse_game_time_str(self.get_time()))
		if current_time >= start_time:
			return True
		return False

	def get_init_time_str(self):
		"""这个是为了dungeon中向center同步时间而写的     dd:hh:mm:ss"""
		return str(self._current_days) + ':' + str(self._current_hours) + ':' + str(self._current_minutes) + ':' + \
			   str(int(self._current_seconds))

	def get_time(self):
		self._current_seconds = self._current_game_time % 60
		self._current_minutes = (self._current_game_time - self._current_game_time) % 3600
		self._current_hours = (self._current_game_time - self._current_game_time - self._current_minutes) % 86400
		self._current_days = self._current_game_time / 86400
		print int(self._current_days), ':', int(self._current_hours), ':', int(self._current_hours), ':', int(self._current_seconds)
		# return RoomTime.format_game_time(int(self._current_hours) , int(self._current_minutes) ,
		# 								 int(self._current_seconds))

	def get_time2(self):
		self._current_seconds = self._current_game_time

		if self._current_seconds >= 60:
			self._current_minutes = int(self._current_seconds / 60)
			self._current_seconds %= 60

		if self._current_minutes >= 60:
			self._current_hours = int(self._current_minutes / 60)
			self._current_minutes %= 60

		if self._current_hours >= 24:
			self._current_days = int(self._current_hours / 24)
			self._current_hours %= 24
		print str(self._current_days) + ':' + RoomTime.format_game_time(int(self._current_hours) , int(self._current_minutes) ,
										 int(self._current_seconds))

	# 目前先不支持直接设置时间
	def set_time(self , time_str):
		pass
		# self._current_seconds = float(time_str.split(':')[2])
		# self._current_minutes = float(time_str.split(':')[1])
		# self._current_hours = float(time_str.split(':')[0])

	@staticmethod
	def format_game_time(hours , minutes , seconds):
		return str(hours) + ':' + str(minutes) + ':' + str(seconds)

	# 传入时分秒字符串, 返回时间戳
	@staticmethod
	def parse_game_time_str(game_time_str):
		return int(game_time_str.split(':')[0]) , int(game_time_str.split(':')[1]) , int(game_time_str.split(':')[2])

	# 传入时分秒数字, 返回时间戳
	@staticmethod
	def calculate_game_time_seconds(game_time_hours , game_time_minutes , game_time_seconds):
		return 3600 * game_time_hours + 60 * game_time_minutes + game_time_seconds


class RoomTaskManager(object):

	def __init__(self):
		super(RoomTaskManager , self).__init__()
		self.timed_tasks = []

	def add_task(self , task):
		"""
		:type task: RoomTimeTask
		"""
		self.timed_tasks.append(task)

	def execute_task(self , current_game_time):
		for task in self.timed_tasks[::-1]:
			if not task.exist():
				self.timed_tasks.remove(task)
				continue
			if not task.can_execute(current_game_time):
				continue

			task.execute_task()
			if not task.is_repeat():
				self.timed_tasks.remove(task)
			else:
				task.repeat_next_day()
				self.timed_tasks.append(task)

# def execute_task(self, pre_game_seconds, current_game_seconds):
# 	for task in self.timed_tasks[::-1]:
# 		if not task.exist():
# 			self.timed_tasks.remove(task)
# 			continue
# 		if not task.can_execute(pre_game_seconds, current_game_seconds):
# 			continue
#
# 		task.execute_task()
# 		if not task.is_repeat():
# 			self.timed_tasks.remove(task)


class RoomTimeTask(object):

	def __init__(self , entity_id , target_time , is_repeat , method , *args , **kwargs):
		"""
		:type target_time: int
		"""
		super(RoomTimeTask , self).__init__()
		self._entity_id = entity_id
		# 时间戳
		self._target_time = target_time
		self._is_repeat = is_repeat
		self._method = method
		self._args = args
		self._kwargs = kwargs

	def exist(self):
		# 判断该任务是否还存在:
		if self._entity_id is None:
			return True
		# if not EntityManager.hasentity(self._entity_id):
		# 	return False
		return True

	def is_repeat(self):
		return self._is_repeat

	def can_execute(self , current_game_time):
		"""
		根据时间来判断该任务是否能够执行
		:type current_game_time: int
		"""
		return current_game_time >= self._target_time

	def repeat_next_day(self):
		self._target_time += 86400

	# def can_execute(self, pre_game_seconds, current_game_seconds):
	#     # 根据时间来判断该任务是否能够执行
	# 	today_task = pre_game_seconds <= self._target_time <= current_game_seconds
	# 	if today_task:
	# 		return True
	#
	# 	yesterday_evening_not_execute_task = self._target_time >= pre_game_seconds > current_game_seconds
	# 	today_morning_not_execute_task = self._target_time <= current_game_seconds < pre_game_seconds
	# 	if yesterday_evening_not_execute_task or today_morning_not_execute_task:
	# 		return True
	# 	return False

	def execute_task(self):
		self._method(*self._args , **self._kwargs)


room_time = RoomTime(30, '0:0:0', 1)

print room_time.__class__.__name__
# while True:
# 	room_time.tick()
# 	room_time.get_time2()
# 	time.sleep(1)
