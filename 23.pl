parent(john,mary).
parent(john,tom).
parent(susan,mary).
parent(susan,tom).
parent(tom,peter).
male(john).
male(tom).
male(peter).
female(mary).
female(susan).
father(F,C):-parent(F,C),male(F).
mother(M,C):-parent(M,C),female(M).
grandparent(G,C):-
    parent(G,P),
    parent(P,C).


