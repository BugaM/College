

load('data.mat')
f = data.f; 
t = data.t;
v = data.v; 
[m, b] = identificarCruiseControl(f, t, v);

u.time = (0:0.1:100)';
u.signals.dimensions = 1;

%2.2a

% d=0;
% u.signals.values = ones(length(u.time), 1)*b*10;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% hold on
% grid on
% ylim([0,32])
% 
% u.signals.values = ones(length(u.time), 1)*b*20;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% 
% u.signals.values = ones(length(u.time), 1)*b*30;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% 
% legend('v_r=10 m/s', 'v_r=20 m/s', 'v_r=30 m/s')
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)
% 
% print -depsc2 2_2a.eps


% 2.2b

% d=0;
% vr = 10;
% fmax = 2000;
% st = 0.1;
% ts = m/b* log(fmax/(fmax - b*vr));
% sz1 = fix(ts/st) +1;
% v1 = ones(sz1, 1)*fmax;
% v2 = ones(length(u.time) - sz1, 1)*b*vr;
% u.signals.values = [v1; v2];
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% ylim([0,12]);
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)
% grid on;
% print -depsc2 2_2b.eps

% 2.2c

% u.signals.values = ones(length(u.time), 1)*b*10;
% d = 100;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% ylim([0,17])
% hold on
% grid on
% 
% d = 200;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% 
% d = 300;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% 
% legend('d=100 N', 'd=200 N', 'd=300 N')
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)
% print -depsc2 2_2c.eps

% 2.2d

% d = 0;
% u.signals.values = ones(length(u.time), 1)*b*10;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% grid on
% hold on
% ylim([0,12])
% 
% m = m + 100;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% 
% legend('Caso nominal', 'Passageiro 100kg')
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)
% print -depsc2 2_2d.eps

% 2.2e

% d = 0;
% u.signals.values = ones(length(u.time), 1)*b*10;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% grid on
% hold on
% 
% u.signals.values = ones(length(u.time), 1)*b*10;
% b = b + 10;
% out = sim('cruise_control_aberta.slx');
% plot(out.v.time, out.v.signals.values)
% legend('Caso nominal', '\Delta b = 10 Ns/m')
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)
% print -depsc2 2_2e.eps

