:- dynamic fact/1.

% ---- Initial Facts ----
fact(sunny).
fact(weekend).

% ---- Rules (IF condition THEN conclusion) ----
rule(go_beach) :- fact(sunny), fact(weekend).
rule(wear_sunglasses) :- fact(sunny).
rule(relax) :- fact(go_beach).

% ---- Forward Chaining Engine ----
forward_chain :-
    rule(NewFact),
    \+ fact(NewFact),
    assertz(fact(NewFact)),
    write('Derived: '), write(NewFact), nl,
    forward_chain.

forward_chain.

% ---- Show All Known Facts ----
show_facts :-
    fact(F),
    write(F), nl,
    fail.
show_facts.
