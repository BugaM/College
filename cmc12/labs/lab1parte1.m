load('data.mat')
f = data.f; 
t = data.t;
v = data.v; 
[m, b] = identificarCruiseControl(f, t, v);
e = exp(1);

figure;
scatter(t,v, 'o','filled')
hold on
v_model = f/b *(1-e.^(-t.*b/m));
plot(t,v_model, LineWidth=2)
legend('experimento','modelo')
xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)

print -depsc2 2_1.eps