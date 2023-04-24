import pyglet
from pyglet.window import key

window = pyglet.window.Window()


personagem = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/creature-sheet.png')


pers_mov = pyglet.image.ImageGrid(personagem, 1, 4)
frame_1 = pers_mov[0]
frame_2 = pers_mov[1]
frame_3 = pers_mov[2]
frame_4 = pers_mov[3]


animation = pyglet.image.load_animation('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/creature.gif')
bin = pyglet.image.atlas.TextureBin()
animation.add_to_texture_bin(bin)
sprite = pyglet.sprite.Sprite(img=animation, x=100, y=100)

persgri = pyglet.image.TextureGrid(pers_mov)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        sprite.x -= 1
    elif symbol == key.RIGHT:
        sprite.x += 10
    elif symbol == key.ENTER:
        print('The enter key was pressed.')



pyglet.app.run()