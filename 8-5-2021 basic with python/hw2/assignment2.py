# Name: Phasit Sangklub
# ID: 6201012610061
# Assignment 2 : OOP
# ====================================
from math import pi,inf

class POSE:
	def __init__(self, x,y,angle):
		self._x = x
		self._y = y
		self._angle = angle

	def print_pose(self):
		print("x : " + str(self._x) + " y : " + str(self._y) +" angle : "+ str(self._angle))



class TwoWheelRobot(POSE):	

	def __init__(self,x = 0,y = 0,angle = 0,wl = 0,wr = 0):
		super().__init__(x,y,round(angle,3))
		self._wl = wl 
		self._wr = wr
		self._vl = 0
		self._vr = 0
		self._v = 0
		self._icr = {"omega" : 0,"robot rotation" : 0}
		self._CASTER_DIAMETER = 0.02
		self._CASTER_RADIUS = self._CASTER_DIAMETER / 2
		self._ROBOT_DIAMETER = 0.08
		self._ROBOT_RADIUS = self._ROBOT_DIAMETER / 2
		self.cal_parameter()
	
	def cal_parameter(self):
		self._vl = round(self._CASTER_RADIUS  * self._wl * 2 * pi / 60, 3)
		self._vr = round(self._CASTER_RADIUS  * self._wr * 2 * pi / 60, 3)
		self._v = round((self._vr + self._vl) / 2, 3)
		omega = round((self._vr - self._vl) / self._ROBOT_DIAMETER, 3)
		try :
			rot_r = round(self._ROBOT_DIAMETER / 2 * (self._vr + self._vl) / (self._vr - self._vl), 3)
		except ZeroDivisionError as e:
			rot_r = inf
			# print(str(e)+ ". Straight motion" +str(self._vl)+" "+str(self._vr))
		self._icr = {"omega" : omega,"robot rotation" : rot_r}


	def set_pose(self,x,y,angle):
		self._x = x
		self._y = y
		self._angle = angle

	def set_wheel_speed(self,wl,wr):
		self._wl = wl
		self._wr = wr
		
	def get_vl(self):
		return self._vl 

	def get_vr(self):
		return self._vr 

	def get_v(self):
		return self._v 

	def get_icr(self):
		return self._icr
	
	def __str__(self):
		return "".join("(x,y,angle) : (" + str(self._x) + "," +str(self._y) + "," +str(self._angle) + ")\t" +
				"(wl,wr) : (" + str(self._wl) + "," +str(self._wr) + ")\t" +
				"(vl,vr,icr) : (" + str(self._vl) + "," +str(self._vr) + "," +str(self._icr) + ")" )
				


if __name__ == "__main__":

	case_list = [[0,0,pi/2,10,10],
				 [0,0,pi/2,10,-10],
				 [0.5,0.5,pi/2,10,20]]	
			

	for index,data in enumerate(case_list):
		obj = TwoWheelRobot(data[0],data[1],data[2],
							data[3],data[4])
		print("case " + str(index+1) + " : " + str(obj))


