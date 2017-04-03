import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite

class Actors(Layer):
	def __init__(self):
		super(Actors,self).__init__()
		self.actor = Sprite("img/player.png")
		self.actor.position= 320,240
		self.add(self.actor)

director.init()

director.run(scene.Scene(Actors()))
