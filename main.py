from banda import Banda
from musico import Musico
from instrumento import Guitarra, Bateria

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

# Exibindo informações da banda
banda.mostrar_musicos()