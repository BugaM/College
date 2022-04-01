load('data.mat')
f = data.f; 
t = data.t;
v = data.v; 
[m, b] = identificarCruiseControl(f, t, v);

tau = 10;

Kp = m/tau - b;

% 2.3a

% bc = b;
% d=0;
% vr = 10;
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% hold on
% grid on
% ylim([0,32])
% 
% vr = 20;
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% 
% vr = 30;
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% 
% legend('v_r=10 m/s', 'v_r=20 m/s', 'v_r=30 m/s')
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)

% print -depsc2 2_3a.eps

%  2.3b

% vr = 10;
% bc = 0;
% d= 0;
% 
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% grid on;
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15);
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15);
% ylim([0, 6])
% 
% print -depsc2 2_3b.eps

%   2.3c

% vr = 10;
% bc = b;
% d=100;
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% hold on
% grid on
% ylim([0,32])
% 
% d = 200;
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% 
% d = 300;
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% 
% legend('v_r=10 m/s', 'v_r=20 m/s', 'v_r=30 m/s')
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)
% 
% print -depsc2 2_3c.eps


%   2.3d

% d = 0;
% bc = b;
% vr = 10;
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% grid on
% hold on
% ylim([0,12])
% 
% b = b + 10;
% out = sim('cruise_control_fechada.slx');
% plot(out.v.time, out.v.signals.values)
% 
% legend('Caso nominal', '\Delta b = 10 Ns/m')
% xlabel('Tempo ($s$)', Interpreter='latex', FontSize=15)
% ylabel('Velocidade ($m/s$)', Interpreter='latex', FontSize=15)
% print -depsc2 2_3d.eps


%  2.3e

% d = 0;
% bc = b;
% vr = 10;
% out = sim('cruise_control_fechada.slx');
% plot(out.u.time, out.u.signals.values)
% grid on
% hold on
% 
% fmax = 2000;
% st = 1e-3;
% ts = m/b* log(fmax/(fmax - b*vr));
% sz1 = fix(ts/st) +1;
% v1 = ones(sz1, 1)*fmax;
% v2 = ones(length(out.u.time) - sz1, 1)*b*vr;
% u2 = [v1; v2];
% plot(out.u.time, u2)
% xlim([0, 50])
% ylim([0, 2100])
% legend('Controle proporcional', 'Malha aberta')
% print -depsc2 2_3e.eps
