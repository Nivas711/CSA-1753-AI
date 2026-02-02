disease(diabates).
disease(hypertension).
disease(obesity).
diet(diabates,low_sugar).
diet(diabates,high_fiber_food).
diet(hypertension, low_salt).
diet(hypertension, fruits_and_vegetables).
diet(obesity,low_fat).
diet(obesity,high_protein_food).
suggest_diet(Disease,Food):-
    disease(Disease),
    diet(Disease,Food).


