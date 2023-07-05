class Artigo:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def getArtigo(self):
        return f"Titulo: {self.titulo} |  Autor: {self.autor}"
    
class Edicao:
    def __init__ (self, numero, volume, data):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.artigos = []

    def add_novoArtigo(self, artigo):
        self.artigos.append(artigo)

    def getEdicao(self):
        return f"Edição número:  {str(self.numero)}  |   Volume:  {str(self.volume)} | Data {str(self.data)}"
    
    def showArtigo(self):
        for artigo in self.artigos:
            print(artigo.getArtigo())

    def getNumeroArtigo(self):
        return len(self.artigos)
    
    def __getDelArtigo__(self, titulo):
        for artigo in self.artigos:
            if artigo.titulo == titulo:
                self.artigos.remove(artigo)

    
class Revista:
   
    def __init__(self, titulo, issn, periodicidade):
        self.titulo = titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = []

    def add_edicaoNova(self, edicao):
        self.edicoes.append(edicao)
    
    def PublicacaoDaEdicao(self,edicao):
        NumArtigos = edicao.NumArtigos()
        if (NumArtigos >= 10 and NumArtigos <= 15):
            return " A edição foi lançada com sucesso !!!."
        else:
            return "Erro. É preciso de 10 a 15 artigos para a edição ser lançada !!!"
    def ShowEdicao(self):
        for edicao in self.edicoes:
            print(edicao.getEdicao())
        