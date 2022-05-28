requisitos.tr = 1.0;
requisitos.Mp = 0.1;

m = planta.m;
Kp = controlador.Kp;
Ki = controlador.Ki;
Kd = controlador.Kd;

planta = obterPlantaMulticoptero();

controlador = projetarControladorVerticalAnalitico(requisitos, planta);

s = tf('s');
malhaPreFiltro = obterMalhaVertical(controlador, planta);
malhaSemPreFiltro = ( Kd*s^2 + Kp*s + Ki)/(m*s^3 + Kd*s^2 + Kp*s + Ki);


t = 0:1e-3:10;

pre = step(malhaPreFiltro, t);
semPre = step(malhaSemPreFiltro, t);
figure;
plot(t, pre, 'LineWidth', 2)
hold on
plot(t, semPre, 'LineWidth', 2)
grid on;
legend('Pre Filtro', 'Sem Pre Filtro');
xlabel('Tempo (s)', 'FontSize', 14);
ylabel('Z (m)', 'FontSize', 14);
