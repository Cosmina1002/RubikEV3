
import socket
import kociemba

HOST = 'ev3dev.local'  
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[PC] Conectat la EV3")

        # 1. Primim stringul Kociemba de la EV3
        kociemba_string = s.recv(1024).decode()
        print("[PC] Am primit string: {}".format(kociemba_string))

        # 2. Calculam solutia cu Kociemba
        try:
            solution = kociemba.solve(kociemba_string)
            if solution:
                print("[PC] Solutie calculata: {}".format(solution))
                s.sendall(solution.encode())
            else:
                print("[PC] Cubul este deja rezolvat.")
                s.sendall(b'')
        except Exception as e:
            print("[PC] Eroare la kociemba.solve: {}".format(e))
            s.sendall(b'')

if __name__ == '__main__':
    main()

