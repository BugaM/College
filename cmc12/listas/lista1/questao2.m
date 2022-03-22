

x = 0:0.1:10;

r1 = (-1.4+sqrt(2.04)*1i)/2;
r2 = (-1.4-sqrt(2.04)*1i)/2;
C1 = r2/(r1-r2);
C2 = -r1/(r1-r2);
y = C1*exp(r1*x) +C2*exp(r2*x) +1;

plot(x,y)
hold on;
grid on;
xlabel ('Tempo (s)')
ylabel ('Posição (m)')
print -dpng -r400 questao2.png
