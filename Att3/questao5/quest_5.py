#! /usr/bin/python3
'''
Classe responsável por gerar os dados fictícios para os n municípios.
Os dados gerados será uma array, onde cada elemento do array representa um
município. Dentro de cada município temos vários cadastros, sendo cada cadastro
representado por uma tupla. Exemplo:
[
    [(CPF, NOME, DATA_NASCIMENTO, MUNICIPIO, ESTADO, VACINA, DATA_DOSES),
    (CPF, NOME, DATA_NASCIMENTO, MUNICIPIO, ESTADO, VACINA, DATA_DOSES)....],

    [(CPF, NOME, DATA_NASCIMENTO, MUNICIPIO, ESTADO, VACINA, DATA_DOSES),
    (CPF, NOME, DATA_NASCIMENTO, MUNICIPIO, ESTADO, VACINA, DATA_DOSES)....]
]
'''

from math import ceil, floor
import uuid
from random import random
from municipios import municipios
from pessoas import pessoas

class GeneratorDataBase:
    def __init__(self, n: int, k: int) -> None:
        self.TOTAL_MUNICIPIOS = n
        self.MAXIMO_PESSOA_POR_MUNI = k

        self.cadastroGerado = [

        ]
    '''
    Gera um numero de cpf
    '''
    @property
    def geradorCpf(self) -> int:
        return int(f'{uuid.uuid4().int}'[0:11])

    @property
    def gerarCadastroGeral(self):
        for municipio in range(0, self.TOTAL_MUNICIPIOS):
            N_PESSOAS = ceil(random()*self.MAXIMO_PESSOA_POR_MUNI)

            pessoasPorMunicipio = []
            for _ in range(0, N_PESSOAS):
                pessoa_n = pessoas.pop()
                pessoa_n["cpf"] = self.geradorCpf
                pessoa_n["municipio"] = municipios[municipio]
                pessoasPorMunicipio.append(
                    (
                        pessoa_n.get("cpf"),
                        pessoa_n.get("nome"),
                        pessoa_n.get("dataNascimento"),
                        pessoa_n.get("municipio"),
                        pessoa_n.get("estado"),
                        pessoa_n.get("vacina"),
                        pessoa_n.get("dataDose")

                    )
                )
            try:
                self.cadastroGerado.append(pessoasPorMunicipio)
            except(UnboundLocalError):
                print('Devemos gerar dados para pelo menos um cidadão!')
                return
        return self.cadastroGerado

    def __str__(self) -> str:
        string = ''
        for i in range(0, len(self.cadastroGerado)):
            string += f'{i} -> {str(self.cadastroGerado[i])}\n'
        return string


data = GeneratorDataBase(3, 2)
data.gerarCadastroGeral
print(data)
