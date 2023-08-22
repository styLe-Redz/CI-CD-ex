from es_primo import function_es_primo

def test_es_primo():
    assert function_es_primo(2) 
    assert function_es_primo(3)
    assert function_es_primo(5) 
    assert not function_es_primo(4) 
    assert not function_es_primo(9) 
    assert function_es_primo(11)
    assert not function_es_primo(15) 

