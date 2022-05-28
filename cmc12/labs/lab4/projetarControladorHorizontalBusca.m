function controlador = projetarControladorHorizontalBusca(requisitosX,...
    requisitosTheta, planta)
% controlador = projetarControladorHorizontalBusca(requisitosX,
% requisitosTheta, planta) projeta o controlador horizontal com um 
% refinamento atraves de busca em grade para um melhor atendimento aos 
% requisitos. As entradas da funcao sao as structs requisitosX, 
% requisitosTheta e planta, que contem os requisitos da malha horizontal,
% os requisitos da malha de arfagem e os parametros da planta, 
% respectivamente. requisitosX e requisitosTheta sao da forma:
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
trs = linspace(0.8 * requisitosX.tr, 1.2 * requisitosX.tr, N);
Mps = linspace(0.8 * requisitosX.Mp, 1.2 * requisitosX.Mp, N);

tr = requisitosX.tr;
Mp = requisitosX.Mp;
g = planta.g;

best_cost = inf;
controladorTheta = projetarControladorArfagem(requisitosTheta, planta);

% Iterar sobre a grade de trs e Mps para determinar o par tr e Mp que
% melhor atende aos requisitos
for i = trs
    for j = Mps
        xi = -log(j)/sqrt(pi^2 + log(j)^2);
        wn = (pi - acos(xi))/(i*sqrt(1-xi^2));
        
        controladorX.Kd = 7*xi*wn/g;
        controladorX.Kp = wn^2*(1+10*xi^2)/g;
        controladorX.Ki = 5*xi*wn^3/g;
        dinamica = obterMalhaHorizontal(controladorX, controladorTheta, planta);
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

controlador.Kd = 7*xi*wn/g;
controlador.Kp = wn^2*(1+10*xi^2)/g;
controlador.Ki = 5*xi*wn^3/g;
end