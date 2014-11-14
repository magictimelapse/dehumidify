#!/usr/bin/env python
import json
import cv2
import numpy as np
from copy import deepcopy
class ReadLEDs(object):
    def __init__(self):
        self.counter = 0
        config = json.loads(open('settings.json').read())
        self._LEDcfg = config['LEDs']
        self._cam = cv2.VideoCapture(0) 
        templatesCfg = config['templates']
        self._templates = {}
        for key in templatesCfg:
            self._templates[key] = []
            for filename in templatesCfg[key]:
                self._templates[key].append(cv2.imread(filename))
        
    def matchTemplate(self,img, template,threshold=0.9):
        result = cv2.matchTemplate(img,template,cv2.TM_CCORR_NORMED)
        loc = np.where(result>=threshold)
        return loc
        

    def matchTemplates(self,img, templates, threshold=0.9):
        locs = []
        for template in templates:
            locs.append(self.matchTemplate(img,template))
        return locs

    def drawRectangles(self,img,key,locs):
        template = self._templates[key][0]
        th,tw = template.shape[:2]
        for loc in locs:
            for pt in zip(*loc[::-1]):
                if key == "ON":
                    color =(0,0,255)
                if key == "OFF":
                    color =(0,255,0)
                else:
                    color =(255,0,0)
                cv2.rectangle(img,pt,(pt[0] + tw, pt[1]+th),color,2)


    def readState2(self):
        for ii in range(10):
            tmp = self._cam.read()[1]
        img = self._cam.read()[1]
        
        self.counter = self.counter +1
        print "matching templates..."
        for key in self._templates:
            print "matching templates...",key
            templates =  self._templates[key]
            locs = self.matchTemplates(img,templates,0.75)
            #print key, locs
            print "draw rectangles..."
            img2 = deepcopy(img)
            self.drawRectangles(img2,key,locs)
            cv2.imwrite('tmp_{0}_{1:03d}.png'.format(key,self.counter),img2)
        print "writing: ",self.counter
        #cv2.imwrite('tmp_{0:03d}.png'.format(self.counter),img)

    def readState(self):
        for ii in range(10):
            tmp = self._cam.read()[1]
        img = self._cam.read()[1]
        for led in self._LEDcfg:
            x = self._LEDcfg[led]['x']
            y = self._LEDcfg[led]['y']
            colVal = [img.item(y,x,ii) for ii in range(3)]
            self._LEDcfg[led]['col'] = {}
            self._LEDcfg[led]['col']['r'] = colVal[2]
            self._LEDcfg[led]['col']['g'] = colVal[1]
            self._LEDcfg[led]['col']['b'] = colVal[0]
        return self._LEDcfg


if __name__ == "__main__":
    import time
    rl = ReadLEDs()
    while True:
        locs = rl.readState2()
        #for led in ledcfg:
        #    print led,
        #    print ledcfg[led]['col']
        time.sleep(1)
        
