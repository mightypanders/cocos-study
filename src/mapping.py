from cocos.tiles import load
from cocos.layer import ScrollingManager
from cocos.director import director
from cocos.scene import Scene

director.init()
MapLayer = load("assets/mapmaking.tmx")["map0"]
scroller = ScrollingManager()
scroller.add(MapLayer)
director.run(Scene(scroller))