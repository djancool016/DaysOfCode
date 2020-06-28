class FrontEnd:
    def __init__(self):
        self.frontend_lang = "HTML/CSS, JavaScript"
        # use super() method to avoid diamond problem
        super(FrontEnd,self).__init__()    
    def lang(self):
        print (f"i want to be FrontEnd Developer, at least i need to learn {self.frontend_lang}")

class BackEnd:
    def __init__(self):
        self.backend_lang = "PHP, SQL"
        super(BackEnd,self).__init__()  
    def lang(self):
        print (f"i want to be BackEnd Developer, at least i need to learn {self.backend_lang}")

class FullStack(FrontEnd, BackEnd):
    def __init__(self):
        super(FullStack,self).__init__()
    def lang(self):
        print (f"i want to be FullStack Developer, at least i need to learn {self.frontend_lang}, {self.backend_lang}")

me = FrontEnd()
me.lang()

me = BackEnd()
me.lang()

me = FullStack()
me.lang()

# output :
# i want to be FrontEnd Developer, at least i need to learn HTML/CSS, JavaScript
# i want to be BackEnd Developer, at least i need to learn PHP, SQL
# i want to be FullStack Developer, at least i need to learn HTML/CSS, JavaScript, PHP, SQL