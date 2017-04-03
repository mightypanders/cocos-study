from cocos.sprite import Sprite
from cocos.tiles import load
from cocos.mapcolliders import RectMapCollider
from cocos.layer import ScrollingManager, ScrollableLayer, ColorLayer
from cocos.director import director
from cocos.scene import Scene
from cocos.actions import Action
from pyglet.window import key

director.init(width=700,height=500,autoscale=False)
scroller = ScrollingManager()
keyboard=key.KeyStateHandler()
director.window.push_handlers(keyboard)
map_layer=load("assets/platformer_map.xml")["map0"]

class GameAction(Action, RectMapCollider):
	def start(self):
		self.target.velocity=0,0
		self.on_ground=True

	def step(self, dt):
		dx=self.target.velocity[0]
		dy=self.target.velocity[1]
		dx = (keyboard[key.RIGHT]-keyboard[key.LEFT])*250*dt
		if self.on_ground and keyboard[key.SPACE]:
			dy=1500
		dy -= 1500 *dt
		last_rect = self.target.get_rect()
		new_rect = last_rect.copy()
		new_rect.x += dx
		new_rect.y += dy*dt
		self.target.velocity = self.collide_map(map_layer,last_rect,new_rect,dy,dx)
		self.on_ground = bool(new_rect.y == last_rect.y)
		self.target.position = new_rect.center
		scroller.set_focus(*new_rect.center)

class SpriteLayer(ScrollableLayer):
	def __init__(self):
		super(SpriteLayer,self).__init__()
		self.sprite = Sprite ("assets/img/grossini.png")
		self.add(self.sprite)
		self.sprite.do(GameAction())

sprite_layer=SpriteLayer()
start = map_layer.find_cells(player_start=True)[0]
rec=sprite_layer.sprite.get_rect()
rec.midbottom=start.midbottom
sprite_layer.sprite.position = rec.center
scroller.add(map_layer,z=0)
scroller.add(sprite_layer,z=1)
bg_color = ColorLayer(52,152,219,1000)
scene=Scene()
scene.add(scroller,z=1)
scene.add(bg_color)
director.run(scene)