import socket
import random
from cube_utils import SYMBOL_TO_COLOR, apply_moves, fitness

# --- Genetic Algorithm helpers ------------------

# Toate mutarile, inclusiv dublurile
MOVE_FUNCS = ['U', "U'", 'U2',
              'D', "D'", 'D2',
              'L', "L'", 'L2',
              'R', "R'", 'R2',
              'F', "F'", 'F2',
              'B', "B'", 'B2']

def random_sequence(length):
    return [random.choice(MOVE_FUNCS) for _ in range(length)]

def mutate(seq, rate=0.2):
    return [random.choice(MOVE_FUNCS) if random.random() < rate else m for m in seq]

def crossover(a, b):
    pt = random.randint(1, len(a) - 1)
    return a[:pt] + b[pt:]

def genetic_solve(scrambled, pop_size=120, seq_len=25, gens=500):
    """
    Returneaza (best_seq, best_fit), unde best_fit = 0 inseamna complet rezolvat.
    """
    pop = [random_sequence(seq_len) for _ in range(pop_size)]
    best_seq, best_fit = None, None

    for gen in range(gens):
        # ordonam dupa fitness crescator (0 = solutie perfecta)
        pop.sort(key=lambda s: fitness(apply_moves(scrambled[:], s)))
        candidate = pop[0]
        fit = fitness(apply_moves(scrambled[:], candidate))

        if best_fit is None or fit < best_fit:
            best_fit, best_seq = fit, candidate[:]
            print("[GEN {gen}] Nou best fitness: {fit} | {best_seq}")
            if fit == 0:
                print("Rezolvat complet la generatia {gen}")
                return best_seq, best_fit

        # reproductie
        survivors = pop[: pop_size // 4]
        while len(survivors) < pop_size:
            p1, p2 = random.sample(pop[: pop_size // 2], 2)
            child = mutate(crossover(p1, p2))
            survivors.append(child)
        pop = survivors

    print("NU s-a gasit rezolvare perfecta, best fitness={best_fit}")
    return best_seq, best_fit


# --- Main client loop ----------------------------

HOST = 'ev3dev.local'   # sau IP-ul EV3
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"[PC] Conectare la EV3 {HOST}:{PORT} ...")
        s.connect((HOST, PORT))

        data = s.recv(8192).decode().strip()
        print("[PC] String Rubik primit:", data)

        # Convertim URFDLB in culori W,R,G,Y,O,B
        scrambled = [ SYMBOL_TO_COLOR[ch] for ch in data ]
        print("[PC] Fitness initial cub:", fitness(scrambled))

        # ajustam lungimea cromozomului in functie de complexitatea scramble-ului
        scramble_moves = len(data) // 3   # estimam 1 mutare la ~3 caractere
        seq_len       = max(20, scramble_moves * 2)
        pop_size      = 200
        gens          = 2000

        solution, best_fit = genetic_solve(
            scrambled,
            pop_size=pop_size,
            seq_len=seq_len,
            gens=gens
        )

        if best_fit != 0:
            print("[PC] Nu trimit mutari deoarece nu s-a gasit solutie completa.")
            return

        # trimit doar daca am fit==0
        out = ' '.join(solution)
        print("[PC] Solutie gasita:", solution)
        s.sendall(out.encode())
        print("[PC] Trimis la EV3!")

if __name__ == '__main__':
    main()
