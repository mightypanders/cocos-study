import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director

class hw(Layer):
	def __init__(self):
		super(hw,self).__init__()
		hw_label=Label("Hello World",font_size=32,anchor_x='center',anchor_y='center')
		hw_label.position=320,240
		self.add(hw_label)

director.init()
director.run(scene.Scene(hw()))