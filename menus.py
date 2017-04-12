from cocos.audio.pygame import mixer
from cocos.audio.pygame.mixer import Sound
from cocos.director import director
from cocos.menu import Menu, CENTER, MenuItem, shake, shake_back
from cocos.scene import Scene
from pyglet.app import exit

class Audio(Sound):
	def __init__(self,audiofile):
		super(Audio,self).__init__(audiofile)


class audioMenu(Menu):
	def __init__(self):
		super(audioMenu,self).__init__("AUDIO CONTROL")
		self.menu_valign=CENTER
		self.menu_halign=CENTER

		menu_items={
			(MenuItem("Play/Pause",self.play_music)),
			(MenuItem("Vol UP",self.vol_UP)),
			(MenuItem("Vol DOWN",self.vol_DOWN)),
			(MenuItem("Exit",self.on_quit))
		}

		#self.song = Audio("aud/LatinIndustries.ogg")
		self.create_menu(menu_items)
		self.is_playing=False
	def play_music(self):
		if self.is_playing:
			self.song.stop()
			self.is_playing=False
		elif not self.is_playing:
			self.song.play(-1)
			self.is_playing=True
	def vol_UP(self):
		volume=self.song.get_volume()
		self.song.set_volume(volume+.1)
	def vol_DOWN(self):
		volume = self.song.get_volume()
		self.song.set_volume(volume-.1)
	def on_quit(self):
		exit()

mixer.init()
director.init()
director.run(Scene(audioMenu()))