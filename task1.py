from graph import *

def eye(x,y,pupil_color,eyelid_size,eyelid_color,orientation): #is right , so orientation=-1, is left , so orientation=1
    microsize_const=1.5

    penColor(eyelid_color[0],eyelid_color[1],eyelid_color[2])
    penSize(eyelid_size/2)
    brushColor(pupil_color[0],pupil_color[1],pupil_color[2])
    circle(x, y, eyelid_size-eyelid_size/4)
    penColor(0,0,0)
    penSize(eyelid_size/2)
    #polygon([(x-eyelid_size/2,y-eyelid_size*microsize_const), (x+eyelid_size/microsize_const,y-eyelid_size), (x+eyelid_size/microsize_const,y-eyelid_size-eyelid_size/4)])
    polygon([(x-orientation*(eyelid_size/2),y-eyelid_size*microsize_const), (x+orientation*(eyelid_size/microsize_const),y-eyelid_size)])


penColor("white")
brushColor("green")
circle(200, 200, 150)
eye(270,180,[255,0,0],20,[255,0,255],-1)
eye(150,180,[255,0,0],20,[255,0,255],1)

brushColor(0,0,0)
brushColor(0,0,0)

rectangle(170, 300, 270, 300)
rectangle(205, 200, 210, 210)

run()

#отдать и исправить капельку!!! к понедельнику!!
