import os
import datetime

class FileGenerator(object): #Class que irá atender ao armazenamento e manipulação de arquivos
	
	def __init__(self, name):

		self.path = os.path.dirname(os.path.abspath(__file__))
		self.candidate_name = name
		self.create_date_name = "Facebook-"+datetime.datetime.now().strftime('%d-%m-%Y')
		self.create_str = "Facebook-"+self.candidate_name+"-"+datetime.datetime.now().strftime('%d-%m-%Y')+".txt"

		os.system("mkdir "+self.create_date_name)
		self.file_path = self.path+"\\"+self.create_date_name+"\\"

		os.system("copy NUL "+self.file_path+self.create_str)
		#os.system("copy NUL "+self.create_date_name) # tenho q realizar a verificação de criação(arquivos e pastas)


	def write(self, text):
		day_file = open(self.file_path+self.create_str,"a+") 
			
		day_file.write(text)	
			
