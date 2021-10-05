#!python3
from MinHeap import MinHeap
from dados_ordenados import cadastro
from datetime import date, datetime


class AppGestaoVacina:
    '''
        Aplicativo de gestaão de vacina para o estado de Sergipe-Se.
    '''

    def __init__(self, n_m_municipios) -> None:
        self.dadosUnificados = self.k_merge(n_m_municipios)
        self.Pessoas_Por_idades = {}  # TabelaHash do tipo IDADE : QTD_VACINADOS
        self.todasIdades = []
        self.frequenciaIdades = []
        self.contabilizaVacinados()
        self.painelConulta()

    def painelConulta(self):
        print(f'***Olá, seja bem vindo(a)!***')
        print(f'O que deseja fazer?')
        print(f'Total vacinados.... [digite 1]')
        print(f'Vacinados por faixa [digite 2]')
        print(f'Para finalizar..... [digite 3]\n')
        resposta = 1
        while(resposta != 3):
            try:
                resposta = int(input())
                if(resposta == 1):
                    print(f'Total vacinados até agora: {self.frequenciaIdades[-1]}')
                elif(resposta == 2):
                    idadeMin = int(input('Digite a idade mínima [entre 1 e 100]: ')) -1
                    idadeMax = int(input('Digite a idade máxima [entre 1 e 100]: '))
                    total = self.frequenciaIdades[idadeMax] - self.frequenciaIdades[idadeMin] 
                    print(f'Entre {idadeMin+1} e {idadeMax} temos {total} vacinados!')

                elif(resposta == 3):
                    resposta = 3 # para o while.
                else:
                    print(f'Opção inválida tente novamente!')
            except(Exception):
                print('Ops! Algo deu errado verifica se está digitando valores válidos!')


        
       
    def contabilizaVacinados(self):
        '''Contabiliza vacinados por idade.'''
        for pessoa in self.dadosUnificados:
            data_nascimento = pessoa[2]
            ano = int(data_nascimento.split('/')[2])
            idade = self.getIdade(ano)  # idade do cidadão

            if(self.estaVacinado(pessoa)):
                self.todasIdades.append(idade)
                if(self.Pessoas_Por_idades.get(idade) != None):  # Já existe essa idade na tabela Hash
                    # Então incremente +1 vacinado.
                    self.Pessoas_Por_idades[idade] += 1
                else:
                    # Primeira idade encontrada até agora.
                    self.Pessoas_Por_idades[idade] = 1

        self.frequenciaIdades = self.contSort(self.todasIdades)


    def estaVacinado(self, pessoa):
        '''
            Recebe uma pessoa e verifica se a mesma tomou as duas doses.
            TODO: implementar a lógica.
        '''

        date_format = '%d/%m/%Y'
        
        dataDose1String = pessoa[6]
        dataDose2String = pessoa[7]

        dose1 = datetime.strptime(dataDose1String, date_format)
        dose2 = datetime.strptime(dataDose2String, date_format)

        deltaDose1 = datetime.now() - dose1
        deltaDose2 = datetime.now() - dose2
        
        if(deltaDose1.days >=0 and deltaDose2.days >=0): #Tomou as duas doses?
            return True
        else:
            return False
            
    def getIdade(self, dataNasci):
        '''
        Recebe uma datade nascimento e retorna a idade da pessoa.
        '''
        anoHoje = date.today().year
        idade = anoHoje - dataNasci
        return idade

    def k_merge(self, arrays):
        minHeap = MinHeap()  # Criando meu MinHeap
        arrOrd = []

        for i in range(len(arrays)):
            # Vamos armazenar no Heap uma tupla do tipo (primeiro_valor, index_do_seu_array)
            minHeap.insert((arrays[i].pop(0), i))

        while(minHeap.current_size):
            tupla = minHeap.heap_extract_min()

            elemento = tupla[0]  # Extraindo o valor
            index = tupla[1]  # Extraindo o index
            arrOrd.append(elemento)
            # Se existir elemeto no array do elemento que acabou de ser removido
            if (arrays[index]):
                minHeap.insert((arrays[index].pop(0), index))

        return arrOrd

    def contSort(self, listaIdades: list) -> list:
        C = [0] * 200

        for elemento in listaIdades:
            C[elemento] += 1

        for i in range(1, len(C)):
            C[i] = C[i] + C[i-1]

        return C


appGestor = AppGestaoVacina(cadastro)
print(appGestor.Pessoas_Por_idades)
print(appGestor.frequenciaIdades)

# print(len(appGestor.dadosUnificados))
# print(dados_unificados)
