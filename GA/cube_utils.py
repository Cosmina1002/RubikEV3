import copy

# map face symbols to center‐colors
SYMBOL_TO_COLOR = {
    'U': 'W',  # white
    'R': 'R',  # red
    'F': 'G',  # green
    'D': 'Y',  # yellow
    'L': 'O',  # orange
    'B': 'B',  # blue
}

# index ranges for each face in a 54‐length list
FACES = {
    'U': list(range(0, 9)),
    'R': list(range(9, 18)),
    'F': list(range(18, 27)),
    'D': list(range(27, 36)),
    'L': list(range(36, 45)),
    'B': list(range(45, 54)),
}

def rotate_face(face):
    return [
        face[6], face[3], face[0],
        face[7], face[4], face[1],
        face[8], face[5], face[2],
    ]

def rotate_face_ccw(face):
    return [
        face[2], face[5], face[8],
        face[1], face[4], face[7],
        face[0], face[3], face[6],
    ]

def move_U(c):
    cube = c[:]
    cube[0:9] = rotate_face(c[0:9])
    f, r, b, l = FACES['F'], FACES['R'], FACES['B'], FACES['L']
    tmp = [c[i] for i in f[0:3]]
    for i in range(3):
        cube[f[i]] = c[r[i]]
        cube[r[i]] = c[b[i]]
        cube[b[i]] = c[l[i]]
        cube[l[i]] = tmp[i]
    return cube

def move_U_prime(c): return move_U(move_U(move_U(c)))
def move_U2(c):      return move_U(move_U(c))

def move_R(c):
    cube = c[:]
    cube[9:18] = rotate_face(c[9:18])
    u, f, d, b = FACES['U'], FACES['F'], FACES['D'], FACES['B']
    idx = [2,5,8]
    tmp = [c[u[i]] for i in idx]
    for j,i in enumerate(idx):
        cube[u[i]]    = c[f[i]]
        cube[f[i]]    = c[d[i]]
        cube[d[i]]    = c[b[6-i]]
        cube[b[6-i]]  = tmp[j]
    return cube

def move_R_prime(c): return move_R(move_R(move_R(c)))
def move_R2(c):      return move_R(move_R(c))

def move_F(c):
    cube = c[:]
    cube[18:27] = rotate_face(c[18:27])
    u, r, d, l = FACES['U'], FACES['R'], FACES['D'], FACES['L']
    tmp = [c[u[i]] for i in [6,7,8]]
    cube[u[6]], cube[u[7]], cube[u[8]] = c[l[8]], c[l[5]], c[l[2]]
    cube[l[2]], cube[l[5]], cube[l[8]] = c[d[2]], c[d[1]], c[d[0]]
    cube[d[0]], cube[d[1]], cube[d[2]] = c[r[0]], c[r[3]], c[r[6]]
    cube[r[0]], cube[r[3]], cube[r[6]] = tmp
    return cube

def move_F_prime(c): return move_F(move_F(move_F(c)))
def move_F2(c):      return move_F(move_F(c))

def move_D(c): return move_U_prime(move_U_prime(move_U_prime(c)))
def move_D_prime(c): return move_U(c)
def move_D2(c):      return move_D(move_D(c))

def move_L(c): return move_R_prime(move_R_prime(move_R_prime(c)))
def move_L_prime(c): return move_R(c)
def move_L2(c):      return move_L(move_L(c))

def move_B(c): return move_F_prime(move_F_prime(move_F_prime(c)))
def move_B_prime(c): return move_F(c)
def move_B2(c):      return move_B(move_B(c))

# register all turns
MOVE_FUNCS = {
    'U': move_U,   "U'": move_U_prime, 'U2': move_U2,
    'R': move_R,   "R'": move_R_prime, 'R2': move_R2,
    'F': move_F,   "F'": move_F_prime, 'F2': move_F2,
    'D': move_D,   "D'": move_D_prime, 'D2': move_D2,
    'L': move_L,   "L'": move_L_prime, 'L2': move_L2,
    'B': move_B,   "B'": move_B_prime, 'B2': move_B2,
}

def apply_moves(cube, moves):
    for m in moves:
        cube = MOVE_FUNCS[m](cube)
    return cube

def fitness(cube):
    # number of wrong stickers
    wrong = 0
    for sym, idxs in FACES.items():
        target = SYMBOL_TO_COLOR[sym]
        wrong += sum(1 for i in idxs if cube[i] != target)
    return wrong

# for EV3 scanning conversion
def convert_sensor_data_to_facelets(all_faces):
    color_id_to_letter = {
        6: 'W', 5: 'R', 3: 'G',
        4: 'Y', 2: 'B', 1: 'O',
    }
    center_color_to_face = {
        'W': 'U', 'R': 'R', 'G': 'F',
        'Y': 'D', 'O': 'L', 'B': 'B',
    }
    labels = ['U','R','F','D','L','B']
    if all_faces is None or len(all_faces)!=6:
        return None
    facelets = {}
    for i, lab in enumerate(labels):
        raw = all_faces[i]
        facelets[lab] = [center_color_to_face[color_id_to_letter[c]] for c in raw]
    return facelets

def facelets_to_kociemba_string(facelets):
    order = ['U','R','F','D','L','B']
    return ''.join(''.join(facelets[f]) for f in order)
