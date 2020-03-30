#-*- coding:utf-8 -*-

import maya.cmds as mc

def create():
	crvList = []
	crvList.append(mc.curve(p=[(-1.2480000000000002, -4.992000000000001, 0.0), (-1.2480000000000002, -1.2480000000000002, 0.0), (-4.992000000000001, -1.2480000000000002, 0.0), (-4.992000000000001, 1.2480000000000002, 0.0), (-1.2480000000000002, 1.2480000000000002, 0.0), (-1.2480000000000002, 4.992000000000001, 0.0), (1.2480000000000002, 4.992000000000001, 0.0), (1.2480000000000002, 1.2480000000000002, 0.0), (4.992000000000001, 1.2480000000000002, 0.0), (4.992000000000001, -1.2480000000000002, 0.0), (1.2480000000000002, -1.2480000000000002, 0.0), (1.2480000000000002, -4.992000000000001, 0.0), (-1.2480000000000002, -4.992000000000001, 0.0)], d=1, per=0, k=[0.0, 4.8, 9.6, 12.8, 17.6, 22.4, 25.6, 30.4, 35.2, 38.4, 43.2, 48.0, 51.2]))
	em = mc.group(n='plus', em=1)
	mc.select(crvList)
	for curve in crvList:
		mc.makeIdentity(curve, a=1, t=1, r=1, s=1, n=0, pn=1)
		mc.xform(curve, ws=1, piv=(0,0,0))
		shapeNode = mc.listRelatives(curve, s=1)
		shapeNode = mc.rename(shapeNode, '{0}Shape'.format(em))
		mc.parent(shapeNode, em, r=1, s=1)
		mc.delete(curve)
	mc.select(em)
	return em