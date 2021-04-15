export default class Grafo {
    constructor(NumeroVertices) {
        this.NumeroVertices = NumeroVertices;
        this.ListaAdj = new Map();

        for (let i = 1; i <= NumeroVertices; i++)
            this.ListaAdj.set(i, []);
    }

    encontraCicloEuler() {
        let [Tot_V_grau_Impar, Vertice_Impar] = [0, 0]; // armazena o total de vértice de grau ímpar e captura um desses vértices

        for (const vertice of this.ListaAdj) { // Verificando os graus dos vértices
            let Graus_verticeAtual = vertice[1].length;
            if (this.eImpar(Graus_verticeAtual)) {
                Tot_V_grau_Impar++;
                Vertice_Impar = vertice[0];
            }
        }
        if (Tot_V_grau_Impar === 0) { // há um caminho euleriano (TODOS VÉRTICES tem grau par )

            console.log(`Ciclo Euleriano: ${this.imprimirCiclo(1)}`) // imprime o ciclo euleriano a partir do vertice 1

        } else if (Tot_V_grau_Impar === 2) {
            console.log(`Caminho Euleriano: ${this.imprimirCiclo(Vertice_Impar)}`) // imprime o ciclo euleriano a partir do vertice impar
        } else {
            console.log('Ops! Não há um ciclo Euleriano');
        }
    }

    imprimirCiclo(vertice) {
        const cicloEuler = [];
        const caminhoAtual = [];

        caminhoAtual.push(vertice);

        while (caminhoAtual.length != 0) { // Enquanto o caminho atual contiver elemento
            let v = caminhoAtual[caminhoAtual.length - 1]; // pegando o topo da pilha
            if (this.ListaAdj.get(v).length === 0) {
                cicloEuler.push(v);
                caminhoAtual.pop();
            } else {
                caminhoAtual.push(this.ListaAdj.get(v)[0]);
                this.removerAresta(v, this.ListaAdj.get(v)[0])
            }

        }
        return cicloEuler;
    }

    /**
     * Adiciona um vértice ao grafo com a lista de adjacência vazia;
     */
    addVertice(v) {
        this.ListaAdj.set(v, []);
    }

    /**
     * Remove um vértice recebido e todas suas conexões
     */
    removerVertices(v) {
        for (const Vertice of this.ListaAdj.keys()) {
            // Atualiza os valores da tabela Hash filtrando os vértices difertente de v
            this.ListaAdj.set(Vertice, this.ListaAdj.get(Vertice).filter(x => x != v));
        }
        if (this.ListaAdj.delete(v)) this.NumeroVertices--; // por fim Remove o vértice diminue a quantidade de vértice;

    }

    /**
     * Cria uma conexão entre o vértice v1 e v2
     */
    addAresta(v1, v2) {
        this.ListaAdj.get(v1).push(v2);
        this.ListaAdj.get(v2).push(v1);
    }
    /**
     * Remove uma aresta
     */

    removerAresta(v1, v2) {
        let listV1 = this.ListaAdj.get(v1);
        let listV2 = this.ListaAdj.get(v2);

        if (listV1 && listV2 != undefined) { // Verifica se esses dois vértices existe
            let indexV1 = listV1.indexOf(v2);
            let indexV2 = listV2.indexOf(v1);

            if (indexV1 > -1 && indexV2 > -1) {
                listV1.splice(indexV1, 1);
                listV2.splice(indexV2, 1);
            }
        }

    }

    imprimeGrafo() {
        for (const Vertice of this.ListaAdj.keys()) {
            let value = this.ListaAdj.get(Vertice);
            let StringList = `[${Vertice}] : ${value.map(x => `${x} -> `).join('')}NULL`;
            console.log(StringList);
        }
    }

    eImpar(n) {
        return n % 2 == 1;
    }
}
const G = new Grafo(3);
G.addAresta(1, 2);
G.addAresta(2, 3);


/*
const G2 = new Grafo(4);
G2.addAresta(1, 2);
G2.addAresta(2, 3);
G2.addAresta(3, 4);
G2.addAresta(4, 2);
*/

G.imprimeGrafo();
G.encontraCicloEuler();