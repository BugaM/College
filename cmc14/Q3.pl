
% Se A divide B
divides(A,B) :- R is B mod A, R = 0.


% primeTest(_, 1).
% primeTest(A, B) :-  not(divides(B, A)), S is B - 1, primeTest(A, S).
% isPrime(X) :- X < 2,!,false.
% isPrime(X) :- S is floor(sqrt(X)) , primeTest(X,S).

% Se S for maior que limite, numero eh primo
primeTest(_,S,L) :- S > L.
% Recursao que ve se numero é primo vendo se numeros de B a L o dividem
primeTest(A, B, L) :- not(divides(B, A)), S is B + 1, primeTest(A, S, L).
% Condicao para completude
isPrime(X) :- X < 2,!,false.
% Teste de primo que usa limitante de divisores igual a raiz de X
isPrime(X) :- L is floor(sqrt(X)) , primeTest(X,2,L).