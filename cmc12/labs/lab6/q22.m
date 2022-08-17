planta = obterPlantaServoPosicao();
requisitos = obterRequisitos();
controladorPos = projetarControladorPosicaoAnalitico(requisitos.posicao, planta);
controladorCor = projetarControladorCorrenteOtimizacao(requisitos.corrente, planta);
avaliarMalhaPosicao(controladorPos, controladorCor, planta);