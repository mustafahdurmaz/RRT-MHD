from __future__ import annotations
import pygame

WHITE=(255,255,255)
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
custom_color_1=(10,145,80)
custom_color_2=(204,255,153)

class Point:
    def __init__(self,x,y,prevp:Point):
        self.x=x
        self.y=y
        self.prevp=prevp
        self.nextpoints:list[Point] = []

    def setnext(self,nextp:Point):
        self.nextpoints.append(nextp)
    
    def dist(self,a:Point) -> float:
        return ((a.x-self.x)**2 + (a.y-self.y)**2)**0.5

    def draw(self,surface,color=custom_color_1):
        if self.prevp != None:
            pygame.draw.line(surface,color,(self.x,self.y),(self.prevp.x,self.prevp.y),2)
            pygame.draw.circle(surface,BLACK,(self.x,self.y),3,0)

    def select(self,surface,color):
        pygame.draw.circle(surface,color,(self.x,self.y),4,1)