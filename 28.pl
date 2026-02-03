% ---- Known Symptoms ----
symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(runny_nose).
symptom(body_pain).
symptom(fatigue).
symptom(nausea).
symptom(vomiting).

% ---- Disease Rules (ONLY FOUR) ----
disease(flu) :-
    has(fever),
    has(cough),
    has(body_pain),
    has(fatigue).

disease(common_cold) :-
    has(runny_nose),
    has(sore_throat),
    has(cough).

disease(migraine) :-
    has(headache),
    has(nausea),
    has(vomiting).

disease(food_poisoning) :-
    has(vomiting),
    has(nausea).

% ---- Store Patient Symptoms ----
:- dynamic has/1.

add_symptom(S) :-
    symptom(S),
    assertz(has(S)).

clear_symptoms :-
    retractall(has(_)).

% ---- Diagnosis ----
diagnose(Disease) :-
    disease(Disease).

diagnose_all :-
    disease(D),
    write('Possible disease: '), write(D), nl,
    fail.
diagnose_all.
