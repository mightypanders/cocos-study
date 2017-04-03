from _ast import In

from cocos import scene
from cocos.layer import Layer, ColorLayer
from cocos.director import director
from cocos.sprite import Sprite
from cocos.actions import *
from cocos.audio.pygame.mixer import Sound
from cocos.audio.pygame import mixer
from pyglet.window.key import symbol_string

class Audio(Sound):
	def __init__(self,filename):
		super(Audio,self).__init__(filename)

class InputLayer(ColorLayer):
	is_event_handler = True
	def __init__(self,x=320,y=240,trippy=False):
		super(InputLayer,self).__init__(46,204,113,1000)
		self.trippy=trippy
		self.sprite=Sprite("img/player.png")
		self.sprite.position=x,y
		self.sprite.opacity=0
		self.add(self.sprite)
		self.sprite.do(FadeIn(1))

		if self.trippy:
			self.bg_music = Audio("aud/LatinIndustriesSlow.ogg")
			self.do((Liquid(duration=15)*100+Waves(duration=15)*100))
		else:
			self.bg_music = Audio("aud/LatinIndustries.ogg")

		self.bg_music.set_volume(.2)
		self.bg_music.play(-1)

	def on_key_press(self,key,modifiers):
		move_left = MoveBy((-50,0),.5)
		move_up = MoveBy((0,50),.5)

		if symbol_string(key)=="LEFT":
			self.sprite.do(move_left)
		elif symbol_string(key)=="RIGHT":
			self.sprite.do(Reverse(move_left))
		elif symbol_string(key)=="UP":
			self.sprite.do(move_up)
		elif symbol_string(key)=="DOWN":
			self.sprite.do(Reverse(move_up))
		elif symbol_string(key)=="SPACE":
			self.bg_music.stop()
			coordinates=self.sprite.position
			if self.trippy:
				self.do(FadeOutTRTiles(grid=(16,12),duration=1))
				director.replace(scene.Scene(InputLayer(coordinates[0],coordinates[1])))
			else:
				self.stop()
				director.replace(scene.Scene(InputLayer(coordinates[0],coordinates[1],True)))
mixer.init()
director.init()
director.run(scene.Scene(InputLayer()))