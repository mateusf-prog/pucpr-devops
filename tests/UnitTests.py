import pytest
import CalculadoraImc

def test_imc_abaixo_peso():
    assert round(CalculadoraImc.calcular_imc(50, 1.80), 2) < 18.5
