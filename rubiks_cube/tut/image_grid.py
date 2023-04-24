import pyglet


window = pyglet.window.Window()


personagem = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/creature-sheet.png')


pers_mov = pyglet.image.ImageGrid(personagem, 1, 4)
frame_1 = pers_mov[0]
frame_2 = pers_mov[1]
frame_3 = pers_mov[2]
frame_4 = pers_mov[3]


persgri = pyglet.image.TextureGrid(pers_mov)

@window.event
def on_draw():
    frame_1.blit(100,100)





pyglet.app.run()