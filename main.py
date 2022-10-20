from __future__ import annotations
import pygame, random
from point import Point
import numpy as np

WHITE=(255,255,255)
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
custom_color_1=(10,145,80)
custom_color_2=(204,255,153)

LEFT=1
RIGHT=3 
RANGE=50

class Main: 

    def __init__(self):
        self.screen_w = 600
        self.screen_h = 600
        self.initial_point =Point(np.inf,np.inf,None)
        self.end_point =Point(np.inf,np.inf,None)
        self.allpoints=[]
        self.RRT_end=False

        pygame.init()
    
    def loop(self):

        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))

        time = pygame.time.Clock()
        running = True
        
        while running:
            
            self.screen.fill(custom_color_2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == LEFT:
                        self.RRT_end = False
                        x,y=pygame.mouse.get_pos()
                        self.initial_point=Point(x,y,None)
                        self.allpoints=[self.initial_point]
                        
                        
                    if event.button == RIGHT:
                        #pygame.draw.line(self.screen,BLUE,(50,60),(120,190),2)
                        self.RRT_end = False
                        x,y=pygame.mouse.get_pos()
                        self.end_point=Point(x,y,None)

                if event.type == pygame.KEYDOWN:
                    running = False
                
            self.draw()
                
            if self.initial_point.x != np.inf and self.end_point.x != np.inf and not self.RRT_end :
                self.RRT()
                
            if self.RRT_end:
                red_point=self.end_point
                while red_point!=None:
                    red_point.draw(self.screen,RED)
                    red_point=red_point.prevp
                    
                

            pygame.display.update()
            pygame.display.flip()
            time.tick(200)
    
    def draw(self):
        if self.initial_point != None:
            self.initial_point.select(self.screen,BLUE)
            
        if self.end_point != None:
            self.end_point.select(self.screen,RED)

        for point in self.allpoints:
            point.draw(self.screen)


    def RRT(self):
        p=Point(random.randint(0,self.screen_w),random.randint(0,self.screen_h),None)
        nearest=Point(np.inf,np.inf,None)
    
        for eleman in self.allpoints:
            if p.dist(eleman) <= RANGE and p.dist(nearest)>p.dist(eleman):
                nearest=eleman
            #print(p.dist(eleman) <= RANGE and p.dist(nearest)>p.dist(eleman))
        
        if nearest.x==np.inf:
            return
        p.prevp=nearest
        nearest.setnext(p)
        self.allpoints.append(p)
        
        
        if p.dist(self.end_point)<RANGE:
            self.RRT_end=True
            self.end_point.prevp=p
            self.allpoints.append(self.end_point)
            
app= Main()
app.loop()        