/**
 * 1. Implementação de funções básicas para manipulação de grafos: 
 * Criar grafo, inserir arestas, inserir vértices, remover arestas, remover vértices. 
 * Implementação do algoritmo de Hierholzer para determinação de uma cadeia euleriana fechada. 
 * Pelo menos três grafos distintos devem ser testados e a cadeia euleriana encontrada para cada grafo deve ser exibida.
 */

/**
 * Estrutura de uma grafo G=(0,0) modelado com lista de adjacência; 
 */
class Grafo {
    constructor() {
        this.NumeroVertices = 0;
        this.NumArestas = 0;
        this.ListaAdj = new Map();
    }

    /**
     * Verifica se há um ciclo Euleriano
     */
    encontraCicloEuler() {
        let Tot_V_grau_Impar = 0; // armazena o total de vértice de grau ímpar e captura um desses vértices

        for (const vertice of this.ListaAdj) { // Verificando os graus dos vértices
            let Graus_verticeAtual = vertice[1].length;
            if (this.eImpar(Graus_verticeAtual))
                Tot_V_grau_Impar++;
        }
        if (Tot_V_grau_Impar === 0)  // há um caminho euleriano (TODOS VÉRTICES tem grau par )
            console.log(`Ciclo Euleriano: ${this.imprimirCiclo(this.ListaAdj.keys().next().value)} 😃`) // imprime o ciclo euleriano a partir do primeiro vértice passado na criação do grafo
        else
            console.log('Ops! Não há um ciclo Euleriano 😞');

    }

    imprimirCiclo(vertice) {
        const cicloEuler = []; // armazena o ciclo Euleriano;
        const caminhoAtual = []; // Armazena os vértices percorridos;

        caminhoAtual.push(vertice);

        while (caminhoAtual.length != 0) { // Enquanto o caminho atual contiver elemento
            let v = caminhoAtual[caminhoAtual.length - 1]; // pegando o topo da pilha
            if (this.ListaAdj.get(v).length === 0) { // Verifica se há elementos adjacentes a V
                cicloEuler.push(v);
                caminhoAtual.pop();
            } else {
                caminhoAtual.push(this.ListaAdj.get(v)[0]); // captura o primeiro elemento da lista adjacente a V 
                this.removerAresta(v, this.ListaAdj.get(v)[0]) // em seguinda remove a aresta percorrida;
            }

        }
        return cicloEuler.join('-');
    }

    /**
     * Adiciona um vértice ao grafo com a lista de adjacência vazia;
     */
    addVertice(v) {
        if (!this.ListaAdj.has(v)) { // verifica se o vertice ja foi add
            this.ListaAdj.set(v, []);
            this.NumeroVertices++;
        }
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
     * Cria uma conexão entre o vértice v1 e v2, ou seja cria uma aresta
     */
    addAresta(v1, v2) {
        try {
            this.ListaAdj.get(v1).push(v2);
            this.ListaAdj.get(v2).push(v1);
            this.NumArestas++;
        } catch (e) {
            console.log(`(${v1}, ${v2}) é uma aresta inválida!`)
        }
    }

    /**
     * Remove uma aresta caso exista
     */
    removerAresta(v1, v2) {
        let listV1 = this.ListaAdj.get(v1);
        let listV2 = this.ListaAdj.get(v2);
        try {
            let indexV1 = listV1.indexOf(v2);
            let indexV2 = listV2.indexOf(v1);

            if (indexV1 > -1 && indexV2 > -1) {
                listV1.splice(indexV1, 1);
                listV2.splice(indexV2, 1);
                this.NumArestas--;
            } else {
                console.log(`Aresta (${v1}, ${v2}) não existe`);
            }
        } catch (e) {
            console.log(`(${v1}, ${v2}) vértices inválidos`);
        }

    }
    imprimeGrafo() {
        console.log(`Lista ADJ do Grafo G = (${this.NumeroVertices}, ${this.NumArestas})\n`)

        for (const Vertice of this.ListaAdj.keys()) {
            let value = this.ListaAdj.get(Vertice);
            let StringList = `[${Vertice}] : ${value.map(x => `${x} -> `).join('')} ❌`;
            console.log(StringList);
        }
    }

    eImpar(n) {
        return n % 2 === 1;
    }
}
const G = new Grafo();

G.addVertice('F');
G.addVertice('A');
G.addVertice('B');
G.addVertice('C');
G.addVertice('D');
G.addVertice('E');

G.addAresta('A', 'F');
G.addAresta('A', 'B');
G.addAresta('B', 'E');
G.addAresta('E', 'D');
G.addAresta('D', 'B');
G.addAresta('C', 'B');
G.addAresta('F', 'C');











G.imprimeGrafo();
G.encontraCicloEuler();
