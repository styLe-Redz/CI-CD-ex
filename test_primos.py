import pytest
from CI-CD-ex es_primo

def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(5) == True
    assert es_primo(4) == False
    assert es_primo(9) == False
    assert es_primo(11) == True
    assert es_primo(15) == False

def test_numeros_negativos():
    assert es_primo(-7) == False
    assert es_primo(-2) == False

def test_numeros_pequenos():
    assert es_primo(0) == False
    assert es_primo(1) == False

if __name__ == "__main__":
    pytest.main()