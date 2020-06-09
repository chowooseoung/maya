import maya.api.OpenMayaUI as om
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mel
import pprint
import os
import sys

mel.eval('''commandPort -name "localhost:7001" -sourceType "mel" -echoOutput;''')