{- Dos slides "aula13-14 Gloss" os exercícios tapete de Sierpinsky e curva de Koch
 Todos os exercícios dos slides "aula15 polimorfismoETypeClasses"
-}

--aula13-14 gloss

--aula15 polimorfismoETypeClasses

{- 1º Considere a seguinte função:

shift ((x,y), z) = (x, (y, z))
Qual é o seu tipo mais geral?

R- shift :: ((a,b), c) -> (a, (b, c))
-}
shift :: ((a,b),c) -> (a, (b,c))
shift ((x, y), z) = (x, (y, z))


{-2º Considere a seguinte função:

zip' [] ps = []
zip' ps [] = []
zip' (p:ps) (q:qs) = (p, q) : zip' ps qs

O que ela calcula? Qual é seu tipo mais geral?

R - A função zip' cria uma lista de tuplas com pares de elementos correspondentes
    exmplo:
    zip' [1..6] "mikael"
    >> [(1,'m'),(2,'i'),(3,'k'),(4,'a'),(5,'e'),(6,'l')]

   tipo mais geral [a] -> [b] -> [(a,b)]

-}
zip' :: [a] -> [b] -> [(a,b)]
zip' [] ps = []
zip' ps [] = []
zip' (p:ps) (q:qs) = (p, q) : zip' ps qs

{-3º
Defina uma função numEqual que pegue uma lista xs de items e
um item x e retorne o número de vezes que x ocorre dentro de xs.
Qual é o tipo da sua função? Como poderia usar numEqual para
definir elem?

R - Minha função é do tipo Eq a => a -> [a] -> Int
    elem iria verificar a contagem de numEqual, ou seja,
    se for maior ou igual a 1 será True, caso contrário retorna False.


-}
numEqual :: Eq a => a -> [a] -> Int -- A função permite qualquer tipo, desde que os tipos permitam a comparação (==).
numEqual _ [] = 0
numEqual x (y:ys)
    | x == y = 1 + numEqual x ys
    | otherwise =  numEqual x ys

elem' :: Ord a => a -> [a] -> Bool
elem' x xs
    | (numEqual x xs) >= 1 = True -- Para ser True o elemento deve aparecer PELO MENOS UMA VEZ.
    |otherwise             = False

{-4º
Defina a função oneLookupFirst que pega uma lista de pares e
um item. Digamos que o tipo dos pares é (a, b), e que o tipo do
item é a. A função retorna a segunda componente do primeiro par
cuja primeira componente é igual ao item. Qual é o tipo mais geral da
função?
R -
  Eq a => a -> [(a,b)] -> b

Defina a função oneLookupSecond que retorna a primeira
componente do primeiro par cuja segunda componente é igual ao
item.
Qual é o tipo mais geral da função?
R -
  Eq b => b -> [(a,b)] -> a
-}
oneLookupFirst :: Eq a => a -> [(a,b)] -> b
oneLookupFirst _ [] = error "Elemento não encontrado, ou lista vazia!"
oneLookupFirst x (y:ys)
   | x == fst(y) = snd (y)
   | otherwise = oneLookupFirst x (ys)

oneLookupSecond :: Eq b => b -> [(a,b)] -> a
oneLookupSecond _ [] = error "Elemento não encontrado, ou lista vazia!"
oneLookupSecond x (y:ys)
   | x == snd(y) = fst (y)
   | otherwise = oneLookupSecond x (ys)

{-5º Considere a seguinte função
misterio y x = [ show z | z <- x, elem z y ]
Qual é eu seu tipo mais geral?
R -
    misterio recebe duas listas. E retorna uma terceira lista com seus elementos convertidos
    em string. A nova lista (z) irá receber apenas valores que está contido nas duas listas.

    tipo geral é misterio :: (Eq a, Show a) => [a] -> [a] -> [String]

-}
misterio :: (Eq a, Show a) => [a] -> [a] -> [String]
misterio y x = [ show z | z <- x, elem z y ]
--Teste Git
