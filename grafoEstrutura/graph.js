class Grafo {
    constructor(NumeroVertices) {
        this.NumeroVertices = NumeroVertices;
        this.ListaAdj = new Map();
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
}

const G = new Grafo(3);
G.addVertice('A');
G.addVertice('B');
G.addVertice('C');



G.addAresta('A', 'B');
// G.addAresta('A', 'C');
// G.addAresta('B', 'C');





// G.removerAresta('A', 'B');
G.removerVertices('A');

G.imprimeGrafo();
