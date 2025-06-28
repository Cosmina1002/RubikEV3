import socket
from scan import scan_all_faces
from cube_utils import convert_sensor_data_to_facelets, facelets_to_kociemba_string
from moves import apply_move_logic
from time import sleep

HOST = ''       # EV3 ascult ^c local
PORT = 12345    # Port folosit  ^yi de clientul de pe PC

def main():
    print("[EV3] Pornim scanarea cubului Rubik...")
    all_faces = scan_all_faces()

    if all_faces is None:
        print("[EROARE] Scanarea a esuat.")
        return

    facelets_lit = convert_sensor_data_to_facelets(all_faces)
    if facelets_lit is None:
        print("Eroare: Nu am putut converti datele scanate.")
        return

    kociemba_string = facelets_to_kociemba_string(facelets_lit)
    print("[EV3] String Rubik: {}".format(kociemba_string))

    # Socket server pe EV3
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print("[EV3] Asteptam conexiune pe portul {}...".format(PORT))

        conn, addr = s.accept()
        with conn:
            print("[EV3] Conectat la {}".format(addr))
            conn.sendall(kociemba_string.encode())

            data = conn.recv(1024)
            if not data:
                print("[EV3] Nu am primit mutari de la PC.")
                return

            moves = data.decode().split()
            print("[EV3] Mutari primite:", moves)

            for move in moves:
                print("[EV3] Executam mutarea: {}".format(move))
                apply_move_logic(move)
                sleep(0.2)

    print("[EV3] Rezolvare completa.")

if __name__ == "__main__":
    main()