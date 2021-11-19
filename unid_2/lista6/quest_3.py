# TODO: Estruturação da ideia
# 1. Ordenar as coordenadas por extremo de Y (EX_BOTTOM, EX_TOP) e coloque em uma extrutura T
# 2. Varrer os segmentos de cima para baixo
# 3. Se encontrar um ponto EX_TOP ele pode conter um segmento contido, então guarde esse ponto em V.
# 4. Se encontrar um ponto EX_BOTTOM, verifique se o mesmo contém contém a mesma coordenada X 
# dos segmentos guardados e sua coordenada Y está entre o range. Se sim, contamos uma intersecão e removemos
# o segmento com EX_BOTTOM das candidatas.
# Repitir os passos 3 e 4 enquanto T não estiver vazio.