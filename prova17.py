class BombaCombustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self):
        dinheiro_abastecer = float(input('Digite o valor que você deseja pagar pra abastecer: '))
        litros_tanque = dinheiro_abastecer / self.valorLitro
        self.quantidadeCombustivel -= litros_tanque
        if litros_tanque > self.quantidadeCombustivel:
            return 'Não a quantidade de litros suficiente para a operação'
        return f'Foi abastecido no tanque do veículo {litros_tanque} litros!'

    def abastecerPorLitro(self):
        litros_abastecer = float(input('Digite quantos litros você deseja abastecer o carro: '))
        valor_total = litros_abastecer * self.valorLitro
        self.quantidadeCombustivel -= litros_abastecer
        if litros_abastecer > self.quantidadeCombustivel:
            return 'Não a quantidade de litros suficiente pela operação' 
        return f'O valor a ser pago é de {valor_total} reais'

    def alterarValor(self):
        novo_valor = float(input('Digite o novo valor do litro: '))
        self.valorLitro = novo_valor
        return 'Novo valor foi alterado!'

    def alterarCombustivel(self):
        novo_combustivel = input('Digite qual o novo combustível: ')
        self.tipoCombustivel = novo_combustivel
        return 'Novo combustível alterado!'

    def alterarQuantidadeCombustivel(self):
        if self.quantidadeCombustivel == 0:
            return 'Não há combustível no tanque!'
        return f'A quantidade restande de combustível é {self.quantidadeCombustivel} litros'
    
bomba = BombaCombustivel('Gasolina',3,300)

# print(bomba.abastecerPorValor())
# print(bomba.alterarQuantidadeCombustivel())
# print(bomba.abastecerPorLitro())
# print(bomba.alterarQuantidadeCombustivel())
# print(bomba.alterarValor())
# print(bomba.abastecerPorValor())
# print(bomba.alterarQuantidadeCombustivel())
print(bomba.alterarCombustivel())