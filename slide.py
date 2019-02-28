class Slide:
	def __init__(self, idSlide, id1, id2, ListofTags):
		self.idSlide = idSlide
		self.id1 = id1
		self.id2 = id2
		self.ListofTags = ListofTags
	
	def damePrimera(self):
		return self.id1


	def dameSegunda(self):
		return self.id2

	def dameID(self):
		return self.idSlide


	def dameTags(self):
		return self.ListofTags
