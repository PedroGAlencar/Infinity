class Elevador:
    def __init__(self):
        self.totalCapacidade = 7
        self.atualCapacidade = 0
        self.totalAndar = 11
        self.atualAndar = 0

    def subir(self):
        if self.atualAndar < self.totalAndar -1:
            self.atualAndar += 1
            return f'Subindo para o andar {self.atualAndar}'
        else:
            return f'Você está no andar mais alto!'

    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            return f'Descendo para o andar {self.atualAndar}'
    
    def entrar(self):
       if self.atualCapacidade < self.totalCapacidade:
           self.atualCapacidade += 1
           return 'Entrando uma pessoa!'
       else:
           return 'O elevador está cheio'

    def sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            return 'Saindo uma pessoa'
        else:
            return 'Não tem ninguém'
            
elevador = Elevador()

print(elevador.sair())
print(elevador.subir())
print(elevador.entrar())
print(elevador.subir())
print(elevador.entrar())
print(elevador.subir())
print(elevador.entrar())
print(elevador.subir())
print(elevador.entrar())
print(elevador.subir())
print(elevador.entrar())
print(elevador.subir())
print(elevador.entrar())
print(elevador.subir())
print(elevador.entrar())
print(elevador.subir())
print(elevador.entrar())
print(elevador.descer())
print(elevador.sair())

            

