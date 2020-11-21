import pyglet
from pyglet.window import key
from pyglet.gl import *

from game import resources, player, draw

main_batch = pyglet.graphics.Batch()

# home_background.png is 2457 x 1397
width = 2457 // 2
height = 1397 // 2
window = pyglet.window.Window(width, height)
resources.home_background.width = width
resources.home_background.height = height

main_player = player.Player(0, width, x=400, y=300, batch=main_batch)
window.push_handlers(main_player)

# Use this to accomodate holding down keys
pressed_keys = []
# Which way the player is facing
facingRight = True


def update(dt):
    main_player.update(dt)


@window.event
def on_draw():
    window.cleasr()
    # Scale pixel art as per: https://gamedev.stackexchange.com/a/57114
    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glEnable(GL_BLEND)  # From https://stackoverflow.com/a/46048254/13697995
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    resources.home_background.blit(0, 0)
    draw.draw_resource_amounts(
        height, main_player.toilet_paper, main_player.pills)
    resources.TV.blit(width - 300, height - 200)
    resources.news_phone.blit(width - 300, height - 200)
    main_batch.draw()


# 120 FPS
pyglet.clock.schedule_interval(update, 1 / 120.0)
pyglet.app.run()
