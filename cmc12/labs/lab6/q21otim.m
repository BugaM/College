planta = obterPlantaServoPosicao();
requisitos = obterRequisitos();
controlador = projetarControladorCorrenteOtimizacao(requisitos.corrente, planta);
avaliarMalhaCorrente(controlador,planta)