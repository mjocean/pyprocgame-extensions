import procgame.game
from procgame import dmd
from procgame.dmd import layers

#     ____                                          ____                
#    / __ \_________  ____ _________  __________   / __ )____ ______    
#   / /_/ / ___/ __ \/ __ `/ ___/ _ \/ ___/ ___/  / __  / __ `/ ___/    
#  / ____/ /  / /_/ / /_/ / /  /  __(__  |__  )  / /_/ / /_/ / /        
# /_/   /_/   \____/\__, /_/   \___/____/____/  /_____/\__,_/_/         
#                  /____/                                               
#                 (as a PyProcGame DMD Layer)
#
#
# EXAMPLE USAGE (with hdDMD color): 
#	progbar = dmd_progress_bar.ProgressBar(400, 50, 1, border_width=8, x=None, y=180, ext_color=(128, 128, 196), int_color=(128, 16, 16), bar_color=(64, 255, 64))
#	self.layer = progbar
#	progbar.setPercentage(0.8)
#
#
# EXAMPLE USAGE (with regular DMD): 
#	progbar = dmd_progress_bar.ProgressBar(100, 20, 1, border_width=1, x=None, y=None, ext_color=8, int_color=2, bar_color=12)
#	self.layer = progbar
#	progbar.setPercentage(0.8)


class ProgressBar(layers.FrameLayer):
	"""
	A helper that encapsulates the creation of a progressBar
	"""
	barLayer = None
	width = None
	height = None
	border_width = 0
	int_color = None
	ext_color = None
	bar_color = None

	def __init__(self, width, height, percentage, border_width = 4, x = None, y = None, ext_color = (155,120,255), int_color =  (128,25,20), bar_color = (128,255,0)):
		if(x is None):
			x = (480 - width)/2
		if(y is None):
			y = (240 - height)/2

		self.width = width
		self.height = height
		self.border_width = border_width

		self.ext_color = ext_color
		self.bar_color = bar_color
		self.int_color = int_color

		self.frame = dmd.Frame(width=width, height=height)
		self.frame.fill_rect(0, 0, width, height, ext_color)
		self.frame.fill_rect(border_width, border_width, width-(2*border_width), height-(2*border_width), int_color)
		self.frame.fill_rect(border_width, border_width, ((width-(2*border_width)) * percentage), height-(2*border_width), bar_color)
		
		(self.target_x_offset, self.target_y_offset) = (x,y)

	def setPercentage(self,percentage):
		self.frame.fill_rect(0, 0, self.width, self.height, self.ext_color)
		self.frame.fill_rect(self.border_width, self.border_width, self.width-(2*self.border_width), self.height-(2*self.border_width), self.int_color)
		self.frame.fill_rect(self.border_width, self.border_width, ((self.width-(2*self.border_width)) * percentage), self.height-(2*self.border_width), self.bar_color)
