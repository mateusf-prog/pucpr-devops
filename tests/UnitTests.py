import pytest
import calcular_imc

def test_imc_abaixo_peso():
    assert round(calcular_imc(50, 1.80), 2) < 18.5
