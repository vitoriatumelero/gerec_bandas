from musico import Musico
from album import Album
class Banda:
   def __init__(self, nome):
      self.nome = nome
      self.musicos = []
      self.albuns=[]
   def adicionar_musico(self, musico):
      self.musicos.append(musico)
   def mostrar_musicos(self):
       print(f'Banda: {self.nome}')
       for musico in self.musicos: 
         musico.mostrar_info()
   def adicionar_album(self, album):
        self.albuns.append(album)

   def mostrar_albuns(self):
        if not self.albuns:
            print(f'A banda {self.nome} não possui álbuns cadastrados.')
        else:
            print(f'Álbuns da banda {self.nome}:')
            for album in self.albuns:
                print(f' - {album.titulo} ({album.ano})')
