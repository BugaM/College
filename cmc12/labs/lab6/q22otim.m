planta = obterPlantaServoPosicao();
requisitos = obterRequisitos();
controladorCor = projetarControladorCorrenteOtimizacao(requisitos.corrente, planta);
controladorPos = projetarControladorPosicaoOtimizacao(requisitos.posicao, controladorCor, planta);

avaliarMalhaPosicao(controladorPos, controladorCor, planta);
