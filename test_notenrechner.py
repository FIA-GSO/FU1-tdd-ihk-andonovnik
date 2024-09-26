import pytest
from notenrechner import berechne_note

# Positivtests
def test_berechne_note__1():
    # Arrange
    testwert = 100
    soll_ergebnis = 'sehr gut'

    # Act
    ist_ergebnis = berechne_note(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_berechne_note__3():
    # Arrange
    testwert = 79
    soll_ergebnis = 'befriedigend'

    # Act
    ist_ergebnis = berechne_note(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_berechne_note__6():
    # Arrange
    testwert = 0
    soll_ergebnis = 'ungenügend'

    # Act
    ist_ergebnis = berechne_note(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

# Negativtests
def test_berechne_note__ueber_100_pkt():
    # Arrange
    testwert = 101

    # Act
    with pytest.raises(ValueError):
        berechne_note(testwert)

def test_berechne_note__unter_0_pkt():
    # Arrange
    testwert = -1

    # Act
    with pytest.raises(ValueError):
        berechne_note(testwert)

def test_berechne_note__type_error():
    # Arrange
    testwert = 'test'

    # Act
    with pytest.raises(ValueError):
        berechne_note(testwert)