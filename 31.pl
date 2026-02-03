% Check if a character is a vowel
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel('A').
vowel('E').
vowel('I').
vowel('O').
vowel('U').

% Count vowels in a list of characters
count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.

count_vowels([H|T], Count) :-
    \+ vowel(H),
    count_vowels(T, Count).

% Main predicate to use with a string
vowel_count(String, Count) :-
    string_chars(String, CharList),
    count_vowels(CharList, Count).
