class Abastecer:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel, formaPagamento):
        self._tipoCombustivel = str(tipoCombustivel)
        self._valorLitro = float(valorLitro)
        self._quantidadeCombustivel = int(quantidadeCombustivel)
        self._formaPagamento = str(formaPagamento)

    def total_a_pagar(self):
        total = self._valorLitro * self._quantidadeCombustivel
        return total






