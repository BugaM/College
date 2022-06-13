function questao5()
s = tf('s');
Gprime = 10/(s*(s+1)*(s+2));
Q = 1/(1/Gprime +s);
rlocus(Q)