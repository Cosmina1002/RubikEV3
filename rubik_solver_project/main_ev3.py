import socket
from scan import scan_all_faces
from cube_utils import convert_sensor_data_to_facelets, facelets_to_kociemba_string
from moves import apply_move_logic
from time import sleep

HOST = ''
PORT = 12345

def main():
    print("[EV3] Pornim scanarea cubului Rubik...")
    all_faces = scan_all_faces()

    if all_faces is None:
        print("[EV3] Eroare: scanarea a esuat.")
        return

    facelets_lit = convert_sensor_data_to_facelets(all_faces)
    if facelets_lit is None:
        print("[EV3] Eroare: conversia la litere Rubik a esuat.")
        return

    kociemba_string = facelets_to_kociemba_string(facelets_lit)
    #bucata in plus
    print("[DEBUG] String Rubik generat:", kociemba_string)
    print("[DEBUG] Lungime:", len(kociemba_string))
    print("[DEBUG] Frecventa litere:", {ch: kociemba_string.count(ch) for ch in "URFDLB"})
    #bucata in plus
    print("[EV3] String Rubik: {}".format(kociemba_string))

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
            print("[EV3] Mutari primite: {}".format(moves))

            for move in moves:
                print("[EV3] Executam mutarea: {}".format(move))
                apply_move_logic(move)
                sleep(0.2)

    print("[EV3] Rezolvare completa.")

if __name__ == '__main__':
    main()
