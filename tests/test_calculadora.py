from app.calculadora import somar, subtrair, calcular_desconto, multiplicar


def test_somar():
    resultado = somar(2, 3)
    assert resultado == 5


def test_subtrair():
    resultado = subtrair(5, 3)
    assert resultado == 2


def test_calcular_desconto():
    resultado = calcular_desconto(100, 10)
    assert resultado == 90


def test_multiplicar():
    resultado = multiplicar(4, 5)
    assert resultado == 20
