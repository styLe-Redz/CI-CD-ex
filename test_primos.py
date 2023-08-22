from es_primo import function_es_primo

def test_es_primo():
    assert function_es_primo(2) == True
    assert function_es_primo(3) == True
    assert function_es_primo(5) == True
    assert function_es_primo(4) == False
    assert function_es_primo(9) == False
    assert function_es_primo(11) == True
    assert function_es_primo(15) == False

def test_numeros_negativos():
    assert function_es_primo(-7) == False
    assert function_es_primo(-2) == False

def test_numeros_pequenos():
    assert function_es_primo(0) == False
    assert function_es_primo(1) == False
