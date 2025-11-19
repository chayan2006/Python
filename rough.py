class xyz: 
	def __init__(self):
	   print("hello")
class abc(xyz):
	def __init__(self):
		print("hi")
ol = abc()

class xyz:
	def sum(self):
		print("sum parent")
class abc(xyz):
	def sum(self):
		print("sub parents")
		
ol = abc()
ol.sum()
class Car:
	def setenginemodel(self,engine)
		self.engine = engine 
		
    def getenginemodel(self ):
	     print(self.engine)
		 
class Honda(Car):
	
class xyz:
		def __init__(self):
			print("num parents")
class abc(xyz):
		def __init__(self ):
			super(). __init__()
			print("sum child")