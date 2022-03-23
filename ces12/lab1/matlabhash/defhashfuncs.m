% attention: the "1+" is there because matlab indexes start on 1, not in
% zero like in the theory.

mod1stChar29 = @(str) (1+mod( (str(1) - char(0)),29)); 
modsumchar29 = @(str) (1+mod( sum(str - char(0)),29)); 
mod1stChar30 = @(str) (1+mod( (str(1) - char(0)),30)); 
modsumchar30 = @(str) (1+mod( sum(str - char(0)),30)); 
modsumchar1k = @(str) (1+mod( sum(str - char(0)),997)); 
modprodchar1k = @(str) (1+mod( prodint(str - char(0),997),997)); 

multHash = @(k,m) (1+floor(m * ( (k*0.6180339887) - floor(k*0.6180339887) ) ) );

mult_m29 = @(str) ( multHash( sum(str - char(0)) ,29) );
mult_m1k = @(str) ( multHash( sum(str - char(0)) ,823) );
mult_m1k_prod = @(str) ( multHash( prodint(str - char(0),823) ,823) );

