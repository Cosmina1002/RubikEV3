import socket, time
from scan import scan_all_faces
from cube_utils import convert_sensor_data_to_facelets, facelets_to_kociemba_string
from moves import apply_move_logic

HOST, PORT = '', 12345

def main():
    print("[EV3] Generating scan for GA...")
    faces = scan_all_faces()
    facelets = convert_sensor_data_to_facelets(faces)
    cube_str = facelets_to_kociemba_string(facelets)
    print(f"[EV3] cube string ({len(cube_str)}): {cube_str}")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print("[EV3] awaiting PC connection...")
    conn, _ = s.accept()

    print("[EV3] connected, sending cube...")
    conn.sendall(cube_str.encode())

    data = conn.recv(8192).decode().split()
    print(f"[EV3] received {len(data)} moves, executing...")
    for m in data:
        apply_move_logic(m)
        time.sleep(0.2)

    conn.close()
    print("[EV3] DONE")

if __name__ == "__main__":
    main()
