import glfw
from OpenGL.GL import *
import numpy as np
import math

global clock
clock=90

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_LINE_LOOP)
    angle=np.linspace(0,330,12)
    angle=angle*np.pi/180
    m=np.cos(angle)
    n=np.sin(angle)
      
    for i in range(0,12):
        glVertex2f(m[i],n[i])
    glEnd()
    drawLine()

def drawLine():
    global clock
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(math.cos(clock*(np.pi/180)),math.sin(clock*(np.pi/180)))
    glEnd()

def key_callback(window,key,scancode,action,mods):
    global clock

    if key==glfw.KEY_1:
        if action==glfw.PRESS:
            clock=60
    if key==glfw.KEY_2:
        if action==glfw.PRESS:
            clock=30
    if key==glfw.KEY_3:
        if action==glfw.PRESS:
            clock=0
    if key==glfw.KEY_4:
        if action==glfw.PRESS:
            clock=-30
    if key==glfw.KEY_5:
        if action==glfw.PRESS:
            clock=-60
    if key==glfw.KEY_6:
        if action==glfw.PRESS:
            clock=-90
    if key==glfw.KEY_7:
        if action==glfw.PRESS:
            clock=-120
    if key==glfw.KEY_8:
        if action==glfw.PRESS:
            clock=-150
    if key==glfw.KEY_9:
        if action==glfw.PRESS:
            clock=180
    if key==glfw.KEY_0:
        if action==glfw.PRESS:
            clock=150
    if key==glfw.KEY_Q:
        if action==glfw.PRESS:
            clock=120
    if key==glfw.KEY_W:
        if action==glfw.PRESS:
            clock=90

def main():

    if not glfw.init():
        return
   
    window = glfw.create_window(480,480,"2019048586", None,None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window,key_callback)


    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        # Poll events
        glfw.poll_events()


        render()


        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()