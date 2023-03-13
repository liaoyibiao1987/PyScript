# -*- coding: utf-8 -*-  


a = 1  
b = 2  

print("方法一:")
import win32com
from win32com.client import Dispatch  
dll = Dispatch("ComToPython.Application")  
result = dll.Add(a, b)  
print("a + b = " + str(result))

#Application = win32com.client.Dispatch("PowerPoint.Application")
#Presentation = Application.Presentations.Add()
#Base = Presentation.Slides.Add(1, 12)
## Add an oval.  Shape 9 is an oval.
#oval = Base.Shapes.AddShape(9, 100, 100, 100, 100)
  
#print("方法二:")
#import comtypes.client  
#dll = comtypes.client.CreateObject('ComToPython.Application')  
#result = dll.Add(a, b)  
#print("a + b = " + str(result))


