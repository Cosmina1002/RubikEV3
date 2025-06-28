# RubikEV3- proiect de diploma

Acest repository contine codul sursa pentru un sistem robotic autonom realizat cu LEGO Mindstorms EV3, capabil sa scaneze si sa rezolve un cub Rubik 3x3. Proiectul include doua metode de rezolvare:

Algoritmul Kociemba (folder: "rubik_solver_project")
Algoritmul Genetic(folder: "GA")

Proiectul contine urmatoarele module si fisiere:

- "rubik_solver_project/" – codul pentru metoda Kociemba
- "GA/" – codul pentru metoda cu algoritm genetic
- "scan.py", "moves.py", "remap.py", "cube_utils.py"
- "main_ev3.py", "main_ev3_genetic.py" – aplicatia care ruleaza pe EV3
- "client_kociemba_solver.py", "client_genetic_solver.py" – aplicatiile client PC pentru fiecare metoda


## Adresa repository-ului

Repository-ul complet este disponibil la adresa:

https://github.com/Cosmina1002/RubikEV3

### Cerinte:

- Python 3.10+ instalat pe PC
- LEGO EV3 cu "ev3dev" instalat
- Conexiune retea TCP între EV3 și PC
- Biblioteca "kociemba" (doar pentru metoda 1):
  
  pip install kociemba

  #### Pentru metoda Kociemba
  Pe EV3: ruleaza main_ev3.py
  Pe PC: ruleaza client_kociemba_solver.py

  ##### Pentru metoda cu algoritm genetic
  Pe EV3: ruleaza main_ev3_genetic.py
  Pe PC: ruleaza client_genetic_solver.py
  
