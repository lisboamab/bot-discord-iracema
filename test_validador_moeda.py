from moedas_validas import MoedasValidas

def test_validador_moeda():
    # Dado
    moedasvalidas = MoedasValidas

    # Quando
    resultado = moedasvalidas('USD').validadorDeMoeda

    # Então
    return resultado