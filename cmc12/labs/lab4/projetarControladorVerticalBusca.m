function controlador = projetarControladorVerticalBusca(requisitos, planta)
% controlador = projetarControladorVerticalBusca(requisitos, planta) 
% projeta o controlador vertical com um refinamento atraves de busca em 
% grade para um melhor atendimento aos requisitos. As entradas da funcao 
% sao as structs requisitos e planta, que contem os requisitos e os 
% parametros da planta, respectivamente. Os requisitos sao:
% requisitos.tr: tempo de subidade de 0 a 100%.
% requisitos.Mp: sobressinal.
% A planta eh dada por:
% planta.m: massa.
% planta.J: inercia.
% planta.l: distancia entre os rotores.
% planta.g: aceleracao da gravidade.
% A saida da funcao eh a struct controlador com:
% controlador.Kp: ganho proporcional.
% controlador.Ki: ganho integrativo.
% controlador.Kd: ganho derivativo.

% Numero de valores de cada parametro usados na grade
N = 20;

% Gerando os valores na grade
trs = linspace(0.8 * requisitos.tr, 1.2 * requisitos.tr, N);
Mps = linspace(0.8 * requisitos.Mp, 1.2 * requisitos.Mp, N);


m = planta.m;
tr = requisitos.tr;
Mp = requisitos.Mp;

best_cost = inf;

% Iterar sobre a grade de trs e Mps para determinar o par tr e Mp que
% melhor atende aos requisitos
for i = trs
    for j = Mps
        xi = -log(j)/sqrt(pi^2 + log(j)^2);
        wn = (pi - acos(xi))/(i*sqrt(1-xi^2));
        
        controlador.Kd = m*7*xi*wn;
        controlador.Kp = m*wn^2*(1+10*xi^2);
        controlador.Ki = m*5*xi*wn^3;
        dinamica = obterMalhaVertical(controlador, planta);
        info = stepinfo(dinamica, 'RiseTimeLimits', [0, 1]);
        real_Mp = info.Overshoot/100;
        real_tr = info.RiseTime;
        cost = abs(tr - real_tr)/abs(tr) + abs(Mp - real_Mp)/abs(Mp);
        if cost < best_cost
            best_cost = cost;
            best_tr = i;
            best_Mp = j;
        end

    end
end

xi = -log(best_Mp)/sqrt(pi^2 + log(best_Mp)^2);
wn = (pi - acos(xi))/(best_tr*sqrt(1-xi^2));

controlador.Kd = m*7*xi*wn;
controlador.Kp = m*wn^2*(1+10*xi^2);
controlador.Ki = m*5*xi*wn^3;
end