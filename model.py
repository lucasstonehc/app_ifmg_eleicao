class Model(object):
     
    def __init__(self, _datetimeOfCollect, _datetimeOfPostPublication, _text, _comment, _like, _share, _tag, _view):
        self.datetimeOfCollect = _datetimeOfCollect
        self.datetimeOfPostPublication = _datetimeOfPostPublication
        self.text = _text
        self.comment = _comment
        self.like = _like
        self.share = _share
        self.tag = _tag
        self.view = _view
    
    
    def getModelObject(self):
        return "Data_de_Coleta: "+ str(self.datetimeOfCollect) + "\nData_do_Poste: "+ str(self.datetimeOfPostPublication) + "\nTexto: " + str(self.text) +"\nComentario: "+str(self.comment) +"\nLikes: "+ str(self.like) +"\nCompartilhamentos: " +str(self.share) + "\nTags: "+str(self.tag) + "\nVisualizações: "+str(self.view) + "\n"
                    
