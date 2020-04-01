import rhinoscriptsyntax as rs
import math 
import random as rnd


class cell(object):
    
    
    def __init__(self, ID, POS, STATE, ZMAX):
        
        
        self.list = []
        self.ID = ID
        self.pos = POS
        self.state = STATE
        self.zmax = ZMAX
        self.list.append(self.state)
        
        
    def live(self,point01, point02, point03,point04,point05,point06,point07,point08,k):
        
        
        allState = point01.list[k]+point02.list[k]+point03.list[k]+point03.list[k]+point04.list[k]+point05.list[k]+point06.list[k]+point07.list[k]+point08.list[k]
        
        
        
        
        if self.list[k] ==1:
            if allState >= 4:
                newState = 0
            elif allState <= 1:
                newState = 0
            else:
                newState = 1
                rs.AddPoint(self.pos)

        else:
            if allState == 3:
                newState = 1
                rs.AddPoint(self.pos)
            else:
                newState = 0
        
        
        self.state = newState
        self.list.append(self.state)

        
        
        
        self.pos = (self.pos[0], self.pos[1], self.pos[2]+1)

    
    
    
        
        
def main():
    
    
    imax = rs.GetInteger('Enter X Value', 40)
    jmax = rs.GetInteger('Enter Y Value', 6)
    zmax = rs.GetInteger('Enter Z Value', 150)
    
    
    pointPopulation = []
    point = {}
    rs.EnableRedraw(False)
    for i in range(imax):
        for j in range(jmax):
            x = i
            y = j
            z = 0
            
            
            pointID = rs.AddPoint(x, y, z)
            pointPos = rs.PointCoordinates(pointID)
            #pointID = [i,j]
            pointState = rnd.random()
            if pointState >0.5:
                secondState = 1
            else:
                secondState = 0
                
                
            pointState = secondState
            point[(i,j)] = cell(pointID, pointPos, pointState,zmax)
            if pointState <= 0.5:
                rs.DeleteObject(pointID)
                
    rs.EnableRedraw(True)
    for k in range(zmax):
        rs.EnableRedraw(False)
        for i in range(imax):
            for j in range(jmax):
                
                if i == 0:
                    iminus1 = imax-1
                if i > 0:
                    iminus1 = i - 1
                
                if i == imax-1:
                    iplus1 = 0
                if i < imax-1:
                    iplus1 = i + 1
                    
                
                if j == 0:
                    jminus1 = jmax-1
                if j > 0:
                    jminus1 = j - 1
                    
                if j == jmax-1:
                    jplus1 = 0
                if j < jmax -1:
                    jplus1 = j + 1 
                    
                
                
                point[(i,j)].live(point[(iminus1,jminus1)],point[(iminus1,j)],
                point[(iminus1,jplus1)],point[(i,jplus1)], point[(iplus1,jplus1)],
                point[(iplus1,j)], point[(iplus1,jminus1)], point[(i,jminus1)],k)                    
        rs.EnableRedraw(True)
        
        

main()