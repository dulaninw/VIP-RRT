
import random 
import math 
import pygame

class RRTMap:
    def __init__(self, start,goal, MapDimensions, obsdim, obsnum):

        self.start = start
        self.goal = goal 
        self.MapDimensions = MapDimensions
        self.Maph,self.Mapw = self.MapDimensions

        # window settings
        self.MapWindowName = 'RRT path planning'
        pygame.display.set_caption(self.MapWindownName)
        self.map = pygame.display.set_mode((self.Mapw,self.Maph))
        self.map.fill((255,255,255))
        self.nodeRad = 0
        self.nodeThickness = 0
        self.edgeThickness = 1

        self.obstacles = []
        self.obsdim = obsdim 
        self.obNumber = obsnum 

        self.grey = (70,70,70)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.Red = (255,0,0)
        self.white = (255,255,255)
    
    
    def drawMap(self, obstacles):
        pygame.draw.circle(self.map, self.Green,self.start,self.nodeRad+5,0)
        pygame.draw.circle(self.map,self.Green,self.start,self.nodeRad+20,1)
        self.drawObs(obstacles)

    def drawPath(self):
        pass

    
    def drawObs(self,obstacles):
        obstacleList = obstacles.copy()
        while (len(obstacleList) > 0):
            obstacle = obstacleList.pop(0)
            pygame.draw.rect(self.map,self.gray,obstacle)





class RRTGraph:
    def __init__(self, start, goal ,MapDimensions,obsdim,obsnum):
        (x,y) = start
        self.start = start
        self.goal = goal 
        self.goalFlag = False
        self.maph.selfmapw = MapDimensions

        # initialize the tree
        self.x = []
        self.y = []
        self.parent = []
        self.x.append(x)
        self.parent.append(0)

        # the obstacles
        self.obstacles = []
        self.obsDim = obsdim 
        self.obsNum = obsnum

        # path
        self.goalstate = None
        self.path = []

    def makeRandomRect(self):
        uppercornerx = int(random.uniform(0,self.mapw-self.obsDim))
        uppercornery = int(random.uniform(0,self.maph-self.obsDim))

        return (uppercornerx, uppercornery)
    def makeobs(self):
        obs = []
        for i in range(0,self.obsNum):
            rectang = None
            startgoalcol = True
            while startgoalcol:
                upper = self.makeRandomRect()
                rectang = pygame.Rect(upper,self(self.obsDim,self.obsDim))
                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal):
                    startgoalcol = True
                else: 
                    startgoalcol = False
                obs.append(rectang)
        self.obstacles = obs.copy()
        return obs

        




        



