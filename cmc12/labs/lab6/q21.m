planta = obterPlantaServoPosicao();
requisitos = obterRequisitos();
controlador = projetarControladorCorrenteAnalitico(requisitos.corrente, planta);
avaliarMalhaCorrente(controlador,planta)