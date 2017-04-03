# Imports as usual
from cocos.sprite import Sprite
from cocos.tiles import load
from cocos.layer import ScrollingManager, ScrollableLayer
from cocos.director import director
from cocos.scene import Scene
from cocos.actions import Driver
from pyglet.window import key

director.init(width=800,height=600,autoscale=False,resizable=False)
keeb = key.KeyStateHandler()
scroller = ScrollingManager()
class cardriver(Driver):
	def step(self,dt):
		self.target.rotation += (keeb[key.RIGHT]-keeb[key.LEFT])*100*dt
		self.target.acceleration = (keeb[key.UP]-keeb[key.DOWN])*500
		if keeb[key.SPACE]:
			self.target.speed-=self.target.speed/10

		super(cardriver,self).step(dt)
		scroller.set_focus(self.target.x,self.target.y)

class carlayer(ScrollableLayer):
	def __init__(self):
		super(carlayer,self).__init__()
		self.sprite = Sprite("assets/img/car.png")
		self.sprite.position=200,100
		self.sprite.max_forward_speed = 200
		self.sprite.max_reverse_speed = -100
		self.add(self.sprite)
		self.sprite.do(cardriver())

car_layer = carlayer()
map_layer = load("assets/road_map.tmx")["map0"]
scroller.add(map_layer)
scroller.add(car_layer)
scene=Scene(scroller)
director.window.push_handlers(keeb)
director.run(scene)

