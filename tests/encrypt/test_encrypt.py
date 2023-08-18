from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    "Se key não possuir o tipo correto, lançar exceção"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("oi", "oi")
    "Se message não possuir o tipo correto, lançar exceção"
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 3)
    assert encrypt_message("umafrase", 9) == "esarfamu"
    assert encrypt_message("umafase", 4) == "esa_famu"
    assert encrypt_message("umafas", 3) == "amu_saf"
