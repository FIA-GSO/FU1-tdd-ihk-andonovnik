def berechne_note(punkte: int, max_punkte: int):
    if not isinstance(punkte, (int, float)) or not isinstance(max_punkte, (int, float)):
        raise ValueError("Es müssen Zahlen sein.")
    if punkte < 0 or punkte > max_punkte:
        raise ValueError("Die Punkte müssen zwischen 0 und den maximalen Punkten liegen.")
    if max_punkte <= 0:
        raise ValueError("Die maximalen Punkte müssen größer als 0 sein.")
    
    prozent = (punkte / max_punkte) * 100
    
    return prozent
    
def berechne_note_prozent(prozent: int):
    if not isinstance(prozent, (int, float)):
        raise ValueError("Es muss eine Zahl sein.")
    if prozent < 0 or prozent > 100:
        raise ValueError("Die Prozentzahl muss zwischen 0 und 100 liegen.")
    
    if prozent >= 92:
        return 'sehr gut'
    elif prozent >= 81:
        return 'gut'
    elif prozent >= 67:
        return 'befriedigend'
    elif prozent >= 50:
        return 'ausreichend'
    elif prozent >= 30:
        return 'mangelhaft'
    else:
        return 'ungenügend'