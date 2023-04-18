# When sprites are collected into a batch,
# no guarantee is made about the order in which they will be drawn. 
# If you need to ensure some sprites are drawn before others 
# (for example, landscape tiles might be drawn before character sprites, 
# which might be drawn before some particle effect sprites), 
# use two or more OrderedGroup objects to specify the draw order:

import pyglet


batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

sprites = [pyglet.sprite.Sprite(image, batch=batch, group=background),
           pyglet.sprite.Sprite(image, batch=batch, group=background),
           pyglet.sprite.Sprite(image, batch=batch, group=foreground),
           pyglet.sprite.Sprite(image, batch=batch, group=foreground),
            ...]

@window.event
def on_draw():
    window.clear()
    batch.draw()