from banda import Banda
from musico import Musico
from instrumento import Guitarra, Bateria
from album import Album

# Criando instrumentos
guitarra = Guitarra('Fender Stratocaster', 'Cordas', 6)
bateria = Bateria('Yamaha Stage Custom', 'Percussão', 5)

# Criando músicos com instrumentos
musico1 = Musico('John', guitarra)
musico2 = Musico('Ringo', bateria)

# Criando banda e adicionando músicos
banda = Banda('The Beatles')
banda.adicionar_musico(musico1)
banda.adicionar_musico(musico2)
minha_banda = Banda("Minha Banda")

# Exibindo informações da banda
banda.mostrar_musicos()

#exibir album
album= Album('Faixa', '2013', 'faixas')
album.mostrar_info()


# Criando álbuns
album1 = Album("Álbum 1", 2021, ["Faixa 1", "Faixa 2"])
album2 = Album("Álbum 2", 2022, ["Faixa 1", "Faixa 2", "Faixa 3"])

# Adicionando álbuns à banda
minha_banda.adicionar_album(album1)
minha_banda.adicionar_album(album2)
# Exibindo os álbuns da banda
minha_banda.mostrar_albuns()
