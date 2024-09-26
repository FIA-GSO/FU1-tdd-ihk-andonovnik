import pytest
from notenrechner import berechne_note, berechne_note_prozent

## Punkte und maximale Punkte eingabe
# Positivtests
def test_berechne_note__1():
    # Arrange
    punkte = 100
    max_punkte = 100
    soll_ergebnis = 100

    # Act
    ist_ergebnis = berechne_note(punkte, max_punkte)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_berechne_note__3():
    # Arrange
    punkte = 60
    max_punkte = 80
    soll_ergebnis = 75

    # Act
    ist_ergebnis = berechne_note(punkte, max_punkte)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_berechne_note__6():
    # Arrange
    punkte = 0
    max_punkte = 6
    soll_ergebnis = 0

    # Act
    ist_ergebnis = berechne_note(punkte, max_punkte)

    # Assert
    assert ist_ergebnis == soll_ergebnis

# Negativtests
def test_berechne_note__ueber_max_pkt():
    # Arrange
    punkte = 101
    max_punkte = 100

    # Act
    with pytest.raises(ValueError):
        berechne_note(punkte, max_punkte)

def test_berechne_note__unter_0_pkt():
    # Arrange
    punkte = -1
    max_punkte = 50

    # Act
    with pytest.raises(ValueError):
        berechne_note(punkte, max_punkte)

def test_berechne_note__type_error_punkte():
    # Arrange
    punkte = 'test'
    max_punkte = 100

    # Act
    with pytest.raises(ValueError):
        berechne_note(punkte, max_punkte)

def test_berechne_note__type_error_max_punkte():
    # Arrange
    punkte = 20
    max_punkte = 'test'

    # Act
    with pytest.raises(ValueError):
        berechne_note(punkte, max_punkte)

def test_berechne_note__max_punkte_0():
    # Arrange
    punkte = 50
    max_punkte = 0

    # Act
    with pytest.raises(ValueError):
        berechne_note(punkte, max_punkte)

def test_berechne_note__max_punkte_negativ():
    # Arrange
    punkte = 50
    max_punkte = -100

    # Act
    with pytest.raises(ValueError):
        berechne_note(punkte, max_punkte)

## Prozentwerteingabe
# Positivtests
def test_berechne_note_prozent__1():
    # Arrange
    prozent = 100
    soll_ergebnis = 'sehr gut'

    # Act
    ist_ergebnis = berechne_note_prozent(prozent)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_berechne_note_prozent__2():
    # Arrange
    prozent = 91
    soll_ergebnis = 'gut'

    # Act
    ist_ergebnis = berechne_note_prozent(prozent)

    # Assert
    assert ist_ergebnis == soll_ergebnis

def test_berechne_note_prozent__6():
    # Arrange
    prozent = 0
    soll_ergebnis = 'ungenügend'

    # Act
    ist_ergebnis = berechne_note_prozent(prozent)

    # Assert
    assert ist_ergebnis == soll_ergebnis

# Negativtests
def test_berechne_note_prozent__ueber_100():
    # Arrange
    prozent = 101

    # Act
    with pytest.raises(ValueError):
        berechne_note_prozent(prozent)

def test_berechne_note_prozent__unter_0():
    # Arrange
    prozent = -1

    # Act
    with pytest.raises(ValueError):
        berechne_note_prozent(prozent)

def test_berechne_note_prozent__type_error():
    # Arrange
    prozent = 'test'

    # Act
    with pytest.raises(ValueError):
        berechne_note_prozent(prozent)
