import pygame
def main():
    pygame.init()
    size=width,heght=800,800
    screen=pygame.display.set_mode(size)
    clock=pygame.time.Clock()
    run=True
    bg=(0,0,0)
    blue=(0,0,255)
    red=(255,0,0)
    green=(0,255,0)
    white=(255,255,255)
    points=[]
    colours=[blue,red,green,white]
    radius=15
    pressed=pygame.key.get_pressed()
    screen.fill(bg)
    color=bg
    start_pos=None
    rect=False
    circle=False
    pen=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
            i=0
            for col in colours:
                pygame.draw.rect(screen,col,pygame.Rect(i,0,50,50))
                i+=50
            pygame.draw.circle(screen,(100,100,100),(275,25),25)

            if circle:
                pygame.draw.cirlce(screen,(186,186,194),(275,25),25)
            else:
                pygame.draw.circle(screen,(100,100,100),(275,25),25)

            if rect:
                pygame.draw.rect(screen,(80,80,80),pygame.Rect(201,0,50,50))
            else:
                pygame.draw.rect(screen,(100,100,100),pygame.Rect(201,0,50,50))

            

            coor=pygame.mouse.get_pos()
            if coor[0]>0 and coor[1]>0 and coor[0]<=50 and coor[1]<=50:
                if pygame.mouse.get_pressed()[0]:
                    color=blue
                    pen=True
                    rect=False
                    circle=False
            if coor[0]>50 and coor[1]>0 and coor[0]<=100 and coor[1]<=50:
                if pygame.mouse.get_pressed()[0]:
                    color=red
                    pen=True
                    rect=False
                    circle=False
            if coor[0]>100 and coor[1]>0 and coor[0]<=150 and coor[1]<=50:
                if pygame.mouse.get_pressed()[0]:
                    color=green
                    pen=True
                    rect=False
                    circle=False
            if coor[0]>150 and coor[1]>0 and coor[0]<=200 and coor[1]<=50:
                if pygame.mouse.get_pressed()[0]:   
                    color=bg
                    pen=True
                    rect=False
                    circle=False

            if coor[0]>200 and coor[1]>0 and coor[0]<=250 and coor[1]<=50:
                if pygame.mouse.get_presseed()[0]:
                    rect=not rect
                    circle=False
                    pen=False

            if coor[0]>250 and coor[1]>0 and coor[0]<=300 and coor[1]<=50:
                if pygame.mouse.get_pressed()[0]:
                    rect=False
                    circle=True
                    pen=False

            if event.type==pygame.MOUSEBUTTONDOWN and rect and coor[1]>50:
                if start_pos is None:
                    start_pos=event.pos
                else:
                    end_pos=event.pos
                    width=end_pos[0]-start_pos[0]
                    height=end_pos[1]-start_pos[1]
                    pygame.draw.rect(screen,color,(start_pos,(width,height)))
                    start_pos=None
            
            if event.type==pygame.MOUSEBUTTONDOWN and circle and coor[1]>50:
                if start_pos is None:
                    start_pos=event.pos
                else:
                    end_pos=event.pos
                    width=end_pos[0]-start_pos[0]
                    height=end_pos[1]-start_pos[1]
                    pygame.draw.circle(screen,color,(start_pos[0]+width/2,start_pos[1]+height/2),min(width,height)/2)
            
            if event.type==pygame.MOUSEMOTION:
                position=event.pos
                points=points+[position]
                points=points[-2:]
                if pygame.mouse.get_pressed()[0] and coor[1]>50 and pen:
                    line(screen,points[0],points[1],radius,color)

            if event.type==pygame.KEYDOWN and (event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT):
                pressed=pygame.key.get_pressed()
                if pressed[pygame.K_RIGHT] and radius <=50:
                    radius=min(50,radius+1)
                if pressed[pygame.K_LEFT] and radius>0:
                    radius=max(50,radius-1)

        pygame.display.flip()
        clock.tick(60)

def line(screen,start,end,radius,colors):
    dx=abs(start[0]-end[0])
    dy=abs(start[1]-end[1])
    iteration=max(dx,dy)

    for i in range(iteration):
        progress=1.0*i/iteration
        aprogress=1-progress
        x=int(aprogress*start[0]+progress*end[0])
        y=int(aprogress*start[1]+progress*end[1])
        pygame.draw.circle(screen,colors,(x,y),radius)

main()