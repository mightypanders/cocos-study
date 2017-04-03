import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.actions import *
from cocos.director import director
from cocos.sprite import Sprite
from pyglet.window.key import symbol_string

class InputExample(Layer):
	is_event_handler = True
	def __init__(self):
		super(InputExample,self).__init__()
		self.sprite = Sprite("img/player.png")
		self.sprite.position =320,240
		self.sprite.opacity = 0
		self.add(self.sprite)
		self.sprite.do(FadeIn(2))

	def on_mouse_press(self,x,y,buttons,modif):
		if buttons ==1:
			self.sprite.do(Jump(50,0,1,1))

	def on_key_press(self,key,modif):
		move_left =MoveBy((-50,0),.5)
		if symbol_string(key)== "LEFT":
			self.sprite.do(move_left)

		if symbol_string(key)=="RIGHT":
			self.sprite.do(Reverse(move_left))
director.init()
director.run(scene.Scene(InputExample()))