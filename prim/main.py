#!/usr/bin/env python3
from __future__ import annotations;
from vertex import Vertex;
from graph import Graph;
from random_graph import random_graph;
from prim import prim;

if (__name__ == '__main__'):
    g1: Graph[Vertex] = random_graph(4)
    
    print(g1);
    print(prim(g1))