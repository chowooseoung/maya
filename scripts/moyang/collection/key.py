#-*- coding:utf-8 -*-

import maya.cmds as mc

def create():
	crvList = []
	crvList.append(mc.curve(p=[(-0.26596036, -4.621960930000001, 0.0), (0.28929414000000003, -4.621960930000001, 0.0), (0.28929414000000003, -3.9153824200000003, 0.0), (1.1980475099999999, -3.9153824200000003, 0.0), (1.1980475099999999, -3.0299681300000003, 0.0), (0.28929414000000003, -3.0299681300000003, 0.0), (0.28929414000000003, -2.94987188, 0.0), (1.1980475099999999, -2.94987188, 0.0), (1.1980475099999999, -2.0644581200000003, 0.0), (0.28929414000000003, -2.0644581200000003, 0.0), (0.28483101000000005, 2.61148861, 0.0), (0.8442862900000001, 2.67001333, 0.0), (1.2470242800000002, 2.80128214, 0.0), (1.57075782, 3.07105744, 0.0), (1.7370267700000002, 3.4596391300000002, 0.0), (1.77974954, 3.8808614, 0.0), (1.7370267700000002, 4.302072010000001, 0.0), (1.57075782, 4.69066907, 0.0), (1.2470242800000002, 4.9604189299999994, 0.0), (0.8442862900000001, 5.0917349100000004, 0.0), (0.42427401000000003, 5.1501796, 0.0), (0.0, 5.164915720000001, 0.0), (0.0, 4.67053331, 0.0), (0.30215618, 4.66147084, 0.0), (0.6012775800000001, 4.62552836, 0.0), (0.8880960900000001, 4.5447712, 0.0), (1.11865033, 4.37887908, 0.0), (1.2370624000000001, 4.139897840000001, 0.0), (1.26748864, 3.88086034, 0.0), (1.2370624000000001, 3.62181542, 0.0), (1.11865033, 3.38284372, 0.0), (0.8880960900000001, 3.21693623, 0.0), (0.6012775800000001, 3.1362076900000004, 0.0), (0.30215618, 3.10021592, 0.0), (0.0, 3.0914083800000003, 0.0), (-0.30215618, 3.10021592, 0.0), (-0.6012775800000001, 3.1362076900000004, 0.0), (-0.8880960900000001, 3.21693623, 0.0), (-1.11865033, 3.38284372, 0.0), (-1.2370624000000001, 3.62181542, 0.0), (-1.26748864, 3.88086034, 0.0), (-1.2370624000000001, 4.139897840000001, 0.0), (-1.11865033, 4.37887908, 0.0), (-0.8880960900000001, 4.5447712, 0.0), (-0.6012775800000001, 4.62552836, 0.0), (-0.30215618, 4.66147084, 0.0), (0.0, 4.67053331, 0.0), (0.0, 5.164915720000001, 0.0), (-0.42427401000000003, 5.1501796, 0.0), (-0.8442862900000001, 5.0917349100000004, 0.0), (-1.2470242800000002, 4.9604189299999994, 0.0), (-1.57075782, 4.69066907, 0.0), (-1.7370267700000002, 4.302072010000001, 0.0), (-1.77974954, 3.8808614, 0.0), (-1.7370267700000002, 3.4596391300000002, 0.0), (-1.57075782, 3.07105744, 0.0), (-1.2470242800000002, 2.80128214, 0.0), (-0.8442862900000001, 2.67001333, 0.0), (-0.26457070000000005, 2.61148861, 0.0), (-0.26596036, -4.621960930000001, 0.0)], d=1, per=0, k=[0.0, 1.04765, 2.380817, 4.095446, 5.766038, 7.480667, 7.631793, 9.346421, 11.017014, 12.731643, 21.554187, 22.615522, 23.41475, 24.209854, 25.007325, 25.806161, 26.604975, 27.402473, 28.197547, 28.996802, 29.796914, 30.597913, 31.53071, 32.101072, 32.669511, 33.231721, 33.767635, 34.270858, 34.762969, 35.255093, 35.7583, 36.294231, 36.856426, 37.424877, 37.995225, 38.565573, 39.134023, 39.696218, 40.232149, 40.735357, 41.22748, 41.719591, 42.222815, 42.758728, 43.320938, 43.889377, 44.45974, 45.392536, 46.193535, 46.993647, 47.792903, 48.587976, 49.385474, 50.184288, 50.983124, 51.780595, 52.575699, 53.374927, 54.474289, 68.122307]))
	em = mc.group(n='key', em=1)
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