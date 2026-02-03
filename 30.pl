% ---- Facts ----
fact(sunny).
fact(weekend).

% ---- Rules ----
go_beach :- fact(sunny), fact(weekend).
wear_sunglasses :- fact(sunny).
relax :- go_beach.

% ---- Askable Goals ----
can_do(X) :- X.
