import pytest
import CalculadoraImc

def test_imc_abaixo_peso():
    assert round(CalculadoraImc.calcular_imc(50, 1.80), 2) < 18.5

def test_imc_peso_normal():
    assert 18.5 <= round(CalculadoraImc.calcular_imc(70, 1.75), 2) < 25

def test_imc_sobrepeso():
    assert 25 <= round(CalculadoraImc.calcular_imc(85, 1.75), 2) < 30

def test_imc_obesidade():
    assert round(CalculadoraImc.calcular_imc(95, 1.60), 2) >= 30

def test_imc_zero_altura():
    with pytest.raises(ZeroDivisionError):
        CalculadoraImc.calcular_imc(70, 0)

