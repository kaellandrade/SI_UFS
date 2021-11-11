def TwoTeams():
    casosDeTestes = int(input())
    while(casosDeTestes):
        frequencia = {}
        totalPessoas = int(input())
        arr = list(map(int, input().split()))
        casosDeTestes -= 1

        valoresIguais = 0
        valoresDiferentes = 0
        for integrante in arr:
            if(frequencia.get(integrante) == None):
                frequencia[integrante] = 1
                valoresDiferentes += 1
                valoresIguais = max(valoresIguais, frequencia[integrante])
            else:
                frequencia[integrante] += 1
                valoresIguais = max(valoresIguais, frequencia[integrante])
        if(valoresIguais == valoresDiferentes - 1):
            print(valoresIguais)
        else:
            valor1 = min(valoresIguais, valoresDiferentes-1)
            valor2 = min(valoresIguais-1, valoresDiferentes)
            print(max(valor1, valor2))


TwoTeams()
