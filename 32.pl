% ---- Simple Fact Matching ----
likes(john, pizza).
likes(mary, pasta).
likes(sam, pizza).

% Query example:
% ?- likes(john, X).

% ---- Structure Pattern Matching ----
person(name(john), age(25)).
person(name(mary), age(30)).

get_name(person(name(N), age(_)), N).
get_age(person(name(_), age(A)), A).

% ---- List Pattern Matching ----
first_element([H|_], H).
second_element([_,S|_], S).
last_element([X], X).
last_element([_|T], X) :- last_element(T, X).

% ---- Pattern Matching with Conditions ----
adult(person(name(N), age(A))) :-
    A >= 18,
    write(N), write(' is an adult'), nl.
