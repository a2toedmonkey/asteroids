import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.colortime = 0
        self.color = (0,0,0)
        
    def draw(self, screen):        
        if self.colortime == 0:
            self.color = random.choices(range(256), k=3)
            self.colortime = ASTEROID_COLOR_TIME
        else:
            self.colortime -= 1
                
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        self.newangle = random.uniform(20,50)
        self.newvect1 = self.velocity.rotate(self.newangle)
        self.newvect2 = self.velocity.rotate(-self.newangle)
        self.newrad = self.radius - ASTEROID_MIN_RADIUS
        
        newAsteroid1 = Asteroid(self.position.x,self.position.y,self.newrad)
        newAsteroid1.velocity = self.newvect1
        newAsteroid2 = Asteroid(self.position.x,self.position.y,self.newrad)
        newAsteroid2.velocity = self.newvect2