def convert_sensor_data_to_facelets(all_faces):

    color_id_to_letter = {
        6: 'W',  # alb
        5: 'R',  # rosu
        3: 'G',  # verde
        4: 'Y',  # galben
        2: 'B',  # albastru
        1: 'O',  # portocaliu
    }

    center_color_to_face = {
        'W': 'U',  
        'R': 'R',  
        'G': 'F', 
        'Y': 'D',  
        'O': 'L',  
        'B': 'B',  
    }

    face_labels = ['U', 'R', 'F', 'D', 'L', 'B']

    if all_faces is None:
        print("[EROARE] Lista all_faces este None (scanare esuata)")
        return None

    if len(all_faces) != 6:
        print("[EROARE] Nu am primit toate cele 6 fete scanate (primit: {})".format(len(all_faces)))
        return None
    for i, face in enumerate(all_faces):
        if face is None or len(face) != 9:
            print("[EROARE] Fata {} este invalida: {}".format(i, face))
            return None

    # Convertim fiecare patratel in litera Rubik corespunzatoare pozitiei centrului
    facelets_lit = {}
    for i, label in enumerate(face_labels):
        raw_face = all_faces[i]
        converted = []
        for code in raw_face:
            color_letter = color_id_to_letter.get(code, '?')
            face_letter = center_color_to_face.get(color_letter, '?')
            converted.append(face_letter)
        facelets_lit[label] = converted

    return facelets_lit

def facelets_to_kociemba_string(facelets_lit):
    """
    Construieste un string de 54 de caractere pentru algoritmul Kociemba din dictul cu URFDLB
    """
    face_order = ['U', 'R', 'F', 'D', 'L', 'B']
    result = ''
    for face in face_order:
        result += ''.join(facelets_lit[face])
    return result