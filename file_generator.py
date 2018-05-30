#gerador de arquivos
import os
import datetime


class FileGenerator(object):

	def __init__(self):

		os.system("mkdir files")

		self.path = os.path.dirname(os.path.abspath(__file__))#criar os arquivos no diretório atual + pasta 

		self.create_date_name = "create_date_"+datetime.datetime.now().strftime('%d-%m-%Y')+".txt" 

		os.system("touch "+self.create_date_name) # tenho q realizar a verificação de criação(arquivos e pastas)

	def write_file(self, text):
		
		if  self.create_date_name != "":
			day_file = open(self.path+"\\"+self.create_date_name,"r+")	
			day_file.write(text)	

