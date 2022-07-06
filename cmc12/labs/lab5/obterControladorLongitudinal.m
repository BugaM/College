function controlador = obterControladorLongitudidenTfnal()
% controlador = obterControladorLongitudinal() retorna uma struct com os
% parametros do controlador longitudinal:
% controlador.Kph: ganho proporcional do controlador de altitude.
% controlador.Kph: ganho derivativo do controlador de altitude.
% controlador.Kph: ganho proporcional do controlador de altitude.
% controlador.Kdh: ganho proporcional do controlador de altitude.
% controlador.a: parametro a do filtro usado no termo PD.

controlador.Kph = 0.00099888;
controlador.Kdh = 0.00099888*0.6;
controlador.Ktheta = 7.0286;
controlador.Kq = 7.0286*0.28;
controlador.a = 9*controlador.Kph/controlador.Kdh;

end