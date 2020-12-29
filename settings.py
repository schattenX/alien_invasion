#settings.py

class Settings():
	"""存储Alien Invasion的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 675
		self.bg_color = (230, 230, 230)