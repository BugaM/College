% ---------------
% Primeiro, vamos fazer a logica de duas listas invertidas

%Inversao de lista vazia e lista unitaria
invert([],[]).
invert([E],[E]).

% Se lista T é inversa de R, entao H concatenado 
% com T é inversa de R concatenado com H
invert([H|T],X) :- invert(T,R), append(R,[H],X).

% Uma lista é palindromo se for igual a seu inverso
palindromo(L) :- invert(L,L).
