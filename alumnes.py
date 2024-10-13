def format_all_alumnes(alumnes):
    if alumnes is None or len(alumnes) == 0:
        return []
    
    formatted = []
    for alumne in alumnes:
        formatted.append({
            "IdAlumne": alumne[0],
            "IdAula": alumne[1],
            "NomAlumne": alumne[2],
            "Cicle": alumne[3],
            "Curs": alumne[4],
            "Grup": alumne[5],
        })
    
    return formatted
