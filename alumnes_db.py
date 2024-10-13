from client import get_connection

def get_all_alumnes():
    try:
        connection = get_connection()
        
        cursor = connection.cursor()
        if cursor:
            print("Creat correctament.")
        else:
            print("No s'ha pogut crear.")
        
        cursor.execute("SELECT IdAlumne, IdAula, NomAlumne, Cicle, Curs, Grup FROM alumne")
        alumnes = cursor.fetchall()
        
        
        cursor.close()
        connection.close()
        
        return alumnes
    except Exception as e:
        print(f"Error al obtenir la llista en alumnes_db.py: {e}")
        raise
