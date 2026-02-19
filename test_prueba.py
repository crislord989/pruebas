from primos import es_primo

def test_numero_primo():
    assert es_primo(4) == True
    assert es_primo(13) == True
    assert es_primo(2) == True

def test_numero_no_primo():
    assert es_primo(10) == False
    assert es_primo(4) == False
    assert es_primo(1) == False
    assert es_primo(0) == False
    assert es_primo(-5) == False
