#!/usr/bin/env python3

from typing import List, Iterable, Tuple;
from itertools import permutations;
from graph import Graph;

cidades: Graph[str] = Graph([
    "Aracaju",
    "Heliópolis",
    "Estância",
    "Lagarto",
    "Maceió"
])
cidades.add_edge_by_vertices('Aracaju', 'Heliópolis', 67)
cidades.add_edge_by_vertices('Aracaju', "Estância", 46)
cidades.add_edge_by_vertices('Aracaju', "Lagarto", 55)
cidades.add_edge_by_vertices('Aracaju', "Maceió", 75)


cidades.add_edge_by_vertices('Heliópolis', "Estância", 91)
cidades.add_edge_by_vertices('Heliópolis', "Lagarto", 122)
cidades.add_edge_by_vertices('Heliópolis', "Maceió", 153)

cidades.add_edge_by_vertices('Estância', "Lagarto", 98)
cidades.add_edge_by_vertices('Estância', "Maceió", 65)

cidades.add_edge_by_vertices('Lagarto', "Maceió", 40)

'''
Recebe um grafo e retorna uma tupla contendo o caminho do caixeiro juntamente
com sua disttância. ([...], distancia);
PS: Essa é uma abordagem simples do problema, pois utiliza permutações.
'''
def caixeiroIngenuo(G: Graph) -> List[str]:
    vt_cities: Iterable[str] = G._vertices
    city_permutations: Iterable[Tuple[str, ...]] = permutations(vt_cities)
    tsp_paths: List[Tuple[str, ...]] = [c + (c[0],) for c in city_permutations]

    global best_path;
    min_dist: int = float('inf');

    for path in tsp_paths:
        distance: int = 0
        last: str = path[0]
        for next in path[1:]:
            distance += G.get_weight_with_vertex(last, next);
            last = next
        if(distance < min_dist):
            min_dist = distance
            best_path = (path, distance);
    return best_path;


print(caixeiroIngenuo(cidades))
