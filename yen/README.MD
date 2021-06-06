https://blogs.reed.edu/compbio/2018/06/01/yens-k-shortest-paths/
https://handwiki.org/wiki/Yen%27s_algorithm
https://courses.cs.vt.edu/cs6824/2014-spring/lectures/lecture-09-k-shortest-paths.pdf
https://dl-acm-org.ez20.periodicos.capes.gov.br/doi/pdf/10.1145/321707.321712
https://www.ams.org/journals/qam/1970-27-04/S0033-569X-1970-0253822-7/S0033-569X-1970-0253822-7.pdf

# Atividade
Implementação do algoritmo de Yen para determinar os k caminhos mais curtos sem loops. Um relatório contendo 4-6 páginas deve ser feito contendo: descrição do algoritmo, exemplo ilustrativo, três grafos a serem testados (com representação grafica), resultados obtidos para cada grafo. O k a ser considerado deve pertencer ao intervalo [3,5] e ao menos dois valores devem ser testados para cada grafo.

# Anotações
O algoritmo pode ser dividido em duas partes, determinando o primeiro k-caminho mais curto ,
e, em seguida, determinar todos os outros k- caminhos mais curtos.

Presume-se que o contêiner A manterá o caminho mais curto k , enquanto o contêiner B, manterá os k- caminhos mais curtos potenciais . Para determinar A(1) , o caminho mais curto da fonte ao coletor, qualquer algoritmo de caminho mais curto eficiente pode ser usado. 


function YenKSP(Graph, source, sink, K):
   // Determine the shortest path from the source to the sink.
   A[0] = Dijkstra(Graph, source, sink);
   // Initialize the set to store the potential kth shortest path.
   B = [];
   
   for k from 1 to K:
       // The spur node ranges from the first node to the next to last node in the previous k-shortest path.
       for i from 0 to size(A[k − 1]) − 2:
           
           // Spur node is retrieved from the previous k-shortest path, k − 1.
           spurNode = A[k-1].node(i);
           // The sequence of nodes from the source to the spur node of the previous k-shortest path.
           rootPath = A[k-1].nodes(0, i);
           
           for each path p in A:
               if rootPath == p.nodes(0, i):
                   // Remove the links that are part of the previous shortest paths which share the same root path.
                   remove p.edge(i,i + 1) from Graph;
           
           for each node rootPathNode in rootPath except spurNode:
               remove rootPathNode from Graph;
           
           // Calculate the spur path from the spur node to the sink.
           spurPath = Dijkstra(Graph, spurNode, sink);
           
           // Entire path is made up of the root path and spur path.
           totalPath = rootPath + spurPath;
           // Add the potential k-shortest path to the heap.
           if (totalPath not in B):
               B.append(totalPath);
           
           // Add back the edges and nodes that were removed from the graph.
           restore edges to Graph;
           restore nodes in rootPath to Graph;
                   
       if B is empty:
           // This handles the case of there being no spur paths, or no spur paths left.
           // This could happen if the spur paths have already been exhausted (added to A), 
           // or there are no spur paths at all - such as when both the source and sink vertices 
           // lie along a "dead end".
           break;
       // Sort the potential k-shortest paths by cost.
       B.sort();
       // Add the lowest cost path becomes the k-shortest path.
       A[k] = B[0];
       // In fact we should rather use shift since we are removing the first element
       B.pop();
   
   return A;