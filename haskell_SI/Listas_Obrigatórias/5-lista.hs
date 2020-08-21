import Data.Char
-- import Data.List
{-
Todos os exercícios nos slides
"aula15-16-17 FuncoesComoArgumentos.pdf"
e no arquivo "aula18-19 AltaOrdem.hs"
-}

{-1º Qual é o tipo mais geral de filter?
    R- (a->Bool) -> [a] -> [a]
-}
---------------------------------------------

{-2ºResolva os problemas 1 e 4 da
primeira prova sem usar nem
compreensões e nem recursão
-}
notDigit :: Char -> Bool
notDigit c = not (isDigit c)

separaDigitos :: String -> (String, String)
separaDigitos [] = ([],[])
separaDigitos xs = (filter isDigit xs, filter notDigit xs)

{-3º Defina length usando map e sum
-}

length' :: [a] -> Int
length' xs = sum (map forOne xs)
    where
      forOne x = 1

{-4º Considere a função
addUp ns = filter greaterOne (map e ns)
    where
        greaterOne n = n>1
        e n = n+1
Como pode redefinir addUp de tal forma que seja feito o filter antes
do map, como em
-}
addUp :: (Num a, Ord a)=>[a] -> [a]
addUp ns = map fun1 (filter fun2 ns)
    where
        fun2 n = n>0 -- Basta eu comparar com menos um elemento antes de aplicar +1
        fun1 n = n+1

{-5º Qual é o o efeito de
map e (map e ns)
Pode concluir algo geral sobre propriedades de map f (map g ns)
onde f e g são funções arbitrárias?
    R - Será plicado map duas vezes.
        Por exemlo: map addOne [1,2,3] = [2,3,4]  map addOne [2,3,4] = [3,4,5]
        Logo, pode-se concluir que eu posso modificar resultados que foram passados para
        uma determinada função.
-}

{- 6º Defina funções que tomem uma lista, ns, e
Retorne a lista consistindo dos quadrados dos inteiros em ns
Retorne a soma dos quadrados dos itens em ns
-}

quadrados_int :: [Int] -> [Int]
quadrados_int ns = map (\x->x*x) ns

sumquad_int :: [Int] -> Int
sumquad_int ns = sum (map (\x->x*x) ns)

maioreszero :: [Int] -> Bool
maioreszero ns = and(map (\x->x>0) ns)

{-7º Defina funções para
Calcular o menor valor de uma função f aplicada de 0 até n
Verificar se os valores de f aplicados de 0 até n são todos iguais
Verificar se todos os valores de f aplicados de 0 até n são maiores que 0
Verificar se os valores de f aplicados de 0 até n estão em ordem crescente
-}

calcmenor :: (Int -> Int) -> Int -> Int
calcmenor f n = foldr min 0 (map f [0..n])

todosiguais :: (Int -> Int) -> Int -> Bool
todosiguais f n = and(map(== head listamodificada) listamodificada) -- Verifico a vabeça da lista por todos elementos da lista
    where
      listamodificada = map f [0..n]

todosmaioreszero :: (Int -> Int) -> Int -> Bool
todosmaioreszero f n =  and(map maiorzero (map f [0..n]))
    where
      maiorzero x = x > 0

{-8º Defina uma função p que receba uma lista de strings strs e
uma lista de caracteres cs e retorne um string contendo cada
string em str acrescido, ao fim dele, o correspondente
caractere da lista cs.
Por exemplo

p ["Penso", "logo", "existo"] [',', ' ', '.'] = "Penso,logo existo."
-}

-- Unta tupla será usada em map para juntar dois elementos da tupla e retorna uma lista.
juntatupla :: (String,Char) -> String
juntatupla xs = fst xs ++ [snd xs]

p :: [String] -> [Char] -> String
p xss xs = concat (map juntatupla pares) -- Como o resultado é uma lista, uso concat para concatenar tudo
    where
      pares = zip xss xs -- pares é uma lista de tuplas ("penso",',')

{-9º
Estabeleça o tipo e defina uma função twice que aceita
uma função e um valor e aplica esta função duas vezes.
Por exemplo, a função twice aplicada as entradas
double e a 7 produzirá 28 como resultado
 -}
twice :: (a->a) -> a -> a
twice fun n = fun(fun(n))

{-10º
Defina o tipo e defina a função iter tal que
iter n f x = f (f (f ... (f x)...)
-}
iter' :: Int -> (a->a) -> (a->a)
iter' n f = foldr (.) id lista
    where
      lista = map g [1..n]
      g _ = f

-- Calcule a soma dos quadrados dos números naturais 1 até n usando map e foldr
somaquad :: Int -> Int
somaquad n = foldr (+) 0 (map (\x->x*x) [1..n])

-- Defina uma função que dê a soma dos quadrados dos inteiros positivos de uma lista de inteiros
somaint :: [Int] -> Int
somaint xs = foldr (+) 0 (map (\x->x*x) (filter(\x->x>=0) xs))

-- Usando foldr defina as funções unzip, last e init
init' :: [a]->[a]
init' xs = foldr (++) [] listanova
    where
      listanova = reverse (drop 1 (reverse (map (\x->[x]) xs)))

--O que calcula a seguinte função misterio xs = foldr (++) [] (map sing xs) where sing x = [x]
{-
Recebe uma lista, o map transforma cada elemento da lista em uma lista unitária, depois são concatenados
todos os elementos com foldr (++), veja o exemplo a baixo:

[1,2,3,4,5] map irá transformar em [[1],[2],[3],[4],[5]]
depois foldr irá concatenar todos  [[1]++[2]++[3]++[4]++[5]]
Retornando a lista original [1,2,3,4,5]
-}

{-
●Defina uma função filterFirst :: (a -> Bool) -> [a] -> [a]
tal que filterFirst p xs remova o primeiro elemento de xs que não
satisfaz a propriedade p.
-}

filterFirst :: (a->Bool) -> [a] -> [a]
filterFirst p (x:xs)
    | not (p x) = xs
    | otherwise = (x:xs)

{-
● Defina filterLast :: (a -> Bool) -> [a] -> [a]
que remove a última ocorrência de um elemento de uma lista que não
satisfaz a propriedade.
-}

filterLast :: (a -> Bool) -> [a] -> [a]
filterLast p (x:y:xs) = (x:y:(takeWhile p xs))

{-
●Defina a função switchMap que aplica de forma alternada duas
funções aos elementos de uma lista. Por exemplo
switchMap addOne addTen [1,2,3,4] ↝  [2,12,4,14]
-}

switchMap :: (Int->Int) -> (Int->Int) -> [Int] -> [Int]
switchMap fun1 fun2 xs = merge((map fun1 pares), (map fun2 impares))
    where
      impares = pegaIndexImpar xs
      pares = pegaIndexPar xs

{-
●Defina funções
split :: [a] -> ([a], [a])
merge :: ([a], [a]) -> [a]
tal que split divide em duas listas, pegando alternadamente,
enquanto merge intercala as duas listas. Por exemplo
split [1,2,3,4,5] -> ([1,3,5], [2,4])
merge ([1,3,5], [2,4]) -> [1,2,3,4,5]

-}

pegaIndexImpar :: [a] -> [a]
pegaIndexImpar [] = []
pegaIndexImpar [x] = []
pegaIndexImpar (x:y:xs) = (y:pegaIndexImpar xs)

pegaIndexPar :: [a] -> [a]
pegaIndexPar [] = []
pegaIndexPar [x] = [x]
pegaIndexPar (x:y:xs) = (x:pegaIndexPar xs)

split :: [a] -> ([a],[a])
split xs = (pegaIndexPar xs, pegaIndexImpar xs)

merge :: ([Int],[Int]) ->[Int]
merge ([],[]) = []
merge (xs,[]) = xs
merge ([],ys) = ys
merge ((x:xs),(y:ys)) = x:y:(merge (xs,ys))

{-Defina as funções takeWhile e dropWhile
Quais são seus tipos mais gerais?
-}

takeWhile' :: (a->Bool) -> [a] -> [a]
takeWhile' fun [] = []
takeWhile' fun (x:xs)
   | fun x = x:takeWhile' fun xs
   | otherwise = []

dropWhile' :: (a->Bool) -> [a] -> [a]
dropWhile' fun [] = []
dropWhile' fun (x:xs)
   | fun x = dropWhile' fun xs
   | otherwise = (x:xs)

-- Qual é o tipo mais geral de twice?
--twice :: (Int->Int)->(Int->Int)

-- 11.3 do livro Haskell: the craft

--Qual é o tipo do operador de aplicação $?
--($) :: (a->b) -> a -> b

{- Considerando que id é a função identidade, explique qual é
o comportamento de cada expressão
id $ f -- É o mesmo que id (f), ou seja id recebe a função como argumento.
f $ id -- Id é uma função atuando como argumento da função f.
id ($) -- id é a conposição da função ($).
-}

{- Defina a generalização de twice iter :: Int -> (a -> a) -> (a -> a) tal que
iter n f é a composição de f com f, n vezes.
-}
iter :: Int -> (a->a) -> (a->a)
iter n f = foldr (.) id lista
    where
      lista = map (\_ -> f) [1..n]
{- Usando iter, defina a função pot2 :: Int -> Int
tal que pot2 n = 2^n
-}

pot2 :: Int -> Int
pot2 n = (iter n doble) 1
    where
      doble x = x*2

--11.7, 11.8, 11.9 e 11.10 do livro Haskell: the craft 3ed

{- Usando ranges, map e expressões lambda, defina replicate
replicate :: int -> a -> [a] tal que replicate n x devolva uma lista formada por n x's.
-}

replicate' :: Int -> a -> [a]
replicate' n x = map (\x->x) (take n (repeat x))

{-
O que representa a seguinte expressão?
filter (> 0) . map (+ 1)

Cria uma função composta por map e filter.
Essa função irá adcionar +1 a cada elemento da lista
e depois com irá filtrar os maiores que 0.
-}

{- Usando combinadores estudados(map, foldr, filter, etc), aplicação parcial,
composição e expressões lambda, escreva definições para as funções
do exemplo do banco de dados de uma biblioteca (Seção 5.7 do livro)
-}

type Persson  = String
type Book     = String
type Database = [(Persson, Book)]

exampleBase :: Database
exampleBase = [ ("Alice", "Tintin"), ("Anna", "Little women"), ("Alice", "Asterix"), ("Rory", "Tintin") ]

books :: Database -> Persson -> [Book]
books exampleBase findpersson =  map (\(a,b)->b) $ filter (\(pessoa,livro)-> pessoa == findpersson) exampleBase

--5.28
borrowers :: Database -> Book -> [Persson]
borrowers exampleBase2 findbook = map (\(a,b)->a) $ filter (\(pessoa,livro)-> livro == findbook) exampleBase2

--Retorna se alguém pegou o livro pesquisado.
borrowed :: Database -> Book -> Bool
borrowed exampleBase3 findbook2 = or (map (\(pessoa,livro)->livro==findbook2) exampleBase3)

-- Função que retorna quantos livros a pessoa está devendo.
numBorroed :: Database -> Persson -> Int
numBorroed exampleBase4 findpersson = foldr (+) 0 (map(\(a,b) -> 1) $ filter (\(pessoa, livro) -> pessoa == findpersson) exampleBase)


returnLoan :: Database -> Persson -> Book -> Database
returnLoan dBase pers bk = filter (\(pessoa,livro) -> (pessoa /= pers) || (livro /= bk)) dBase
