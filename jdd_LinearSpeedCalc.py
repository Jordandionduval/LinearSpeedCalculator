#-----------------------------Tested for Maya 2022+-----------------------------#
#
#             jdd_LinearSpeedCalculator
#             v1.0.0, last modified 23/02/23
# 
# MIT License
# Copyright (c) 2023 Jordan Dion-Duval
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
#----------------------------------INSTALLATION---------------------------------#
# 1. Copy the "jdd_outlinerBuddy.py" to your Maya scripts directory:
#     > MyDocuments\Maya\scripts\
# 2. Then, within maya, use the following text as a python script to run the tool:
#    (without the apostrophes)
'''
import jdd_LinearSpeedCalculator as scpt
scpt.UI()
'''
# 3.(Optional) Alternatively, the text can be saved in the custom shelf using
# maya's script editor. This makes the script a small button in your current shelf
# so it can easily be accessed later.
#--------------------------------------------------------------------------------#

import maya.cmds as cmds
import math

class WspeedCalc(object):
	
	def __init__(self):
		
		self.window = "WspeedCalc"
		self.title = "Linear Speed Calculator"
		self.size = (200, 275)
			
		#focus if window open #WIP
		#if cmds.window(self.window, exists = True):
		#	cmds.showWindow()
		if cmds.window(self.window, exists = True):
			cmds.deleteUI(self.window, window=True)
			print('\nRestarting instance of '+self.title+'...\n')

		else:
			print('\nLaunching a new instance of '+self.title+'...\n')
	
		#create new window
		self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
		
		#create UI
		cmds.columnLayout(adj = False)
		cmds.separator(style='out', h=5)
		cmds.text(l=" Finds the distance between two keys")
		cmds.text(l=" translation divided by the duration.")
		cmds.text(l="\n      Only works with 2 linear keys.")
		cmds.separator(style='in', h=5)
		cmds.text(l="Start Keyframe")
		self.keyStart = cmds.intField(v=0, min=0, cc = self.updateKeyStart, w=self.size[0])
		cmds.text(l="End Keyframe")
		self.keyEnd = cmds.intField(v=30, min=0, cc = self.updateKeyEnd, w=self.size[0])
		cmds.text(l="Framerate (FPS)")
		self.FPS = cmds.floatField(v=30, min=0, cc = self.updateFPS, w=self.size[0])
		cmds.separator(style='none', h=5)
		cmds.text(l="Result:")
		self.result = cmds.textField(ed=False, tx="Run command to see your results!", w=self.size[0])
		cmds.separator(style='none', h=5)
		self.buttonGetSpeed = cmds.button(l = "Get Speed", command = self.getSpeed, w=self.size[0])
		cmds.setParent('..')
		
		#display new window
		cmds.showWindow()
	
	#Update values
	def updateKeyStart(self, *args):
		res = cmds.intField(self.keyStart, query = True, v = True)
		return res
	def updateKeyEnd(self, *args):
		res = cmds.intField(self.keyEnd, query = True, v = True)
		return res
	def updateFPS(self, *args):
		res = cmds.floatField(self.FPS, query = True, v = True)
		return res
		
	#Code
	def distance(self, v1, v2):
		x1=v1[0]
		x2=v2[0]
		y1=v1[1]
		y2=v2[1]
		z1=v1[2]
		z2=v2[2]

		res=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)+math.pow(y2-y1,2))

		return res

	def getSpeed(self, *args):
		selection=cmds.ls(sl=True, sn=True)
		fps=self.updateFPS()
			
		fBegin=self.updateKeyStart()
		fEnd=self.updateKeyEnd()
		
		pBegin=cmds.keyframe(str(selection[0])+'.translate', q=True, time=(fBegin, fBegin), vc=True)
		pEnd=cmds.keyframe(str(selection[0])+'.translate', q=True, time=(fEnd, fEnd), vc=True)

		duration = (fEnd-fBegin)/fps
		try:
		    distance=self.distance(pBegin, pEnd)
		except TypeError:
		    raise TypeError("No controller selected")
		
		res=round(distance/duration,2)
		resText=str(res)+" unit/s"
		cmds.textField(self.result, e=True, tx=str(res)+" unit/s")
		print(resText)
		return res
		
def UI():
	WspeedCalc()
UI()