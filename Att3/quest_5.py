#!python3
from MinHeap import MinHeap
from dados_ordenados import cadastro
from datetime import date


class AppGestaoVacina:
    '''
        Aplicativo de gestaão de vacina para o estado de Sergipe-Se.
    '''

    def __init__(self, n_m_municipios) -> None:
        self.dadosUnificados = self.k_merge(n_m_municipios)
        self.Pessoas_Por_idades = {} #TabelaHash do tipo IDADE : QTD_VACINADOS

        #Contabilizando as pessoas vacinadas por idade.
        for pessoa in self.dadosUnificados:
            data_nascimento = pessoa[2]
            ano = int(data_nascimento.split('/')[2])
            idade = self.getIdade(ano) #idade do cidadão

            if(self.Pessoas_Por_idades.get(idade) != None): #Já existe essa idade na tabela Hash
                self.Pessoas_Por_idades[idade] += 1 #Então incremente +1 vacinado.
            else:
                self.Pessoas_Por_idades[idade] = 1 #Primeira idade encontrada até agora.

    def estaVacinado(self, pessoa):
        '''
            Verifica se a pessoa está totalmente imune. (com duas doses)
            TODO: implementar a lógica.
        '''
        return True
    
    def getIdade(self, dataNasci):
        anoHoje = date.today().year
        idade =  anoHoje - dataNasci
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
            # Se existir elemeto no array do elemento que acabou de serremovido
            if (arrays[index]):
                minHeap.insert((arrays[index].pop(0), index))

        return arrOrd


    # def isSorted(res, key=lambda x: x):
    #     '''
    #     Testa se realmente os dados estão ordenados por CPF.
    #     '''
    #     for i in range(1, len(res)):
    #         if(key(res[i-1]) >= key(res[i])):
    #             return False
    #     return True


appGestor = AppGestaoVacina(cadastro)
# print(appGestor.dadosUnificados)
print(appGestor.Pessoas_Por_idades)
# print(isSorted(dados_unificados, lambda x: x[0]))
# print(dados_unificados)
