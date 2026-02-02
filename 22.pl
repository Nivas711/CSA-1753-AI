bird(sparrow).
bird(eagle).
bird(penguin).
can_fly(eagle).
can_fly(sparrow).
can_fly(Bird) :-
    bird(Bird),
    \+ cannot_fly(Bird).


