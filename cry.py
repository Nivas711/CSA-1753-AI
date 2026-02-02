from itertools import permutations

letters = ('S','E','N','D','M','O','R','Y')
digits = range(10)

for perm in permutations(digits, len(letters)):
    S,E,N,D,M,O,R,Y = perm
    
    # Leading digits cannot be zero
    if S == 0 or M == 0:
        continue
    
    send  = 1000*S + 100*E + 10*N + D
    more  = 1000*M + 100*O + 10*R + E
    money = 10000*M + 1000*O + 100*N + 10*E + Y
    
    if send + more == money:
        print(f"S={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}")
        print(f"{send} + {more} = {money}")
        break
