import Grafo from './graph.js';










const G = new Grafo(6);
G.addAresta(5, 0);
G.addAresta(5, 2);
G.addAresta(2, 1);
G.addAresta(1, 0);
G.addAresta(3, 1);
G.addAresta(3, 4);
G.addAresta(4, 1);


G.imprimeGrafo();