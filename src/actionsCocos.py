import cocos
from cocos.actions import *
from cocos.sprite import *
from cocos.layer import *



class Actions(ColorLayer):
	def __init__(self):
		super(Actions,self).__init__(52,152,219,1000)
		self.sprite = Sprite("img/player.png")
		self.sprite.position=320,240
		self.fade_in()
		self.move_left()
		self.rotate_antiClock()

	def fade_in(self):
		fade_action = FadeIn(2)
		self.sprite.opacity=0
		self.add(self.sprite,z=1)
		self.sprite.do(fade_action)

	def move_left(self):
		left = MoveBy((-150,0),2)
		self.sprite.do(left)

	def rotate_antiClock(self):
		rot = RotateBy(90,2)
		self.sprite.do(rot)

director.init()
director.run(cocos.scene.Scene(Actions()))