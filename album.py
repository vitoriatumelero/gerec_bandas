class Album:
    def __init__(self, titulo, ano, lf):
        self.titulo= titulo
        self.ano=ano
        self.lf=lf
    def mostrar_info(self):
        print(f'Titulo: {self.titulo}, ano: {self.ano}, lf: {self.lf}')


        