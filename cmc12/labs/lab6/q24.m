planta = obterPlantaServoPosicao();
controlador = load("controlador.mat").controlador;

simularRespostaDegrau(controlador, planta)