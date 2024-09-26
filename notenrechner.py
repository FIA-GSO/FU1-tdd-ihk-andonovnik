def berechne_note(punkte: int):
    if not isinstance(punkte, (int, float)):
        raise ValueError("Es muss eine Zahl sein.")
    if punkte < 0 or punkte > 100:
        raise ValueError("Die Punkte können nicht unter 0 oder über 100 sein.")
    
    if punkte >= 92 and punkte <= 100:
        return 'sehr gut'
    elif punkte >= 81:
        return 'gut'
    elif punkte >= 67:
        return 'befriedigend'
    elif punkte >= 50:
        return 'ausreichend'
    elif punkte >= 30:
        return 'mangelhaft'
    elif punkte <= 29 and punkte >= 0:
        return 'ungenügend'