

class Restaurante:
    
    def __inity__(self, nome, categoria):
        self.nome = nome 
        self.ativo = False        #self= eu mesmo ou objeto especifico 
        self.categoria = categoria
        self.avaliaçao = []
        self.cardapio = []

    def alternar_status(self):
        self.ativo = not 
        self.ativo 

    def mostrar_status(self):
        if self.ativo:
            return "Ativado"
        else:
            return "Desativado"
        
   



