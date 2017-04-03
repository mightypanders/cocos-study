
import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite

from pyglet.window.key import symbol_string

class keebinput(Layer):
	is_event_handler = True
	def __init__(self):
		super(keebinput,self).__init__()
		self.label=Label("Keys: ",font_size=32)
		self.label.position=320,240
		self.keys_being_pressed = set()
		self.update_text()
		self.add(self.label)

	def update_text(self):
		key_names=[symbol_string(k) for k in self.keys_being_pressed]
		text_for_labels="Keys: "+", ".join(key_names)
		self.label.element.text=text_for_labels

	def on_key_press(self,key,modif):
		self.keys_being_pressed.add(key)
		self.update_text()

	def on_key_release(self,key,modif):
		self.keys_being_pressed.remove(key)
		self.update_text()

director.init()
director.run(scene.Scene(keebinput()))