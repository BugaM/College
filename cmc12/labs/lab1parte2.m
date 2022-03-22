

load('data.mat')
f = data.f; 
t = data.t;
v = data.v; 
[m, b] = identificarCruiseControl(f, t, v);

u.time = (0:0.1:1000)';
u.signals.values = ones(length(u.time), 1)*b*10;
u.signals.dimensions = 1;

out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values)
hold on

u.signals.values = ones(length(u.time), 1)*b*20;
out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values)

u.signals.values = ones(length(u.time), 1)*b*30;
out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values)

legend('v_r=10 m/s', 'v_r=20 m/s', 'v_r=30 m/s')
xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)

print -depsc2 2_2a.eps