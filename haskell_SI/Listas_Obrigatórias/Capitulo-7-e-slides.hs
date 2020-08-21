import Data.Char
--Todos os exercícios dos slides "aula08 RecursoPrimitiva" e "aula10 RecursaoGeral".
--Adicionalmente, os exercícios do livro do 7.8 a 7.26, exceto os exercícios 7.11, 7.15, 7.21, 7.22 e 7.23.

------------------AULA 08--------------------

--8.1--------Multiplica Sem *----------------
multiplica :: Integer -> Integer -> Integer
multiplica 0 n = 0
multiplica m n = multiplica(n-1)  m + m
--------------------------------------------

--8.2-----Recebe n e devola 2ˆn------------
eleven :: Integer -> Integer
eleven 0 = 1
eleven n = 2 * eleven(n-1)
--------------------------------------------

--8.3-----Recebe m e n devolve mˆn----------
potMN::Int->Int->Int
potMN m n
    | n == 0 && m == 0 = 0
    | n == 0 = 1
    | m == 0 = 0
    | otherwise = m*potMN m (n-1)
-------------------------------------------

--8.4-----Calcule: 0! + 1! + 2! + ...+ n!--
somaFatorial::Int->Int
somaFatorial n
    | n == 0 = 1
    | n == 1 = 1
    |otherwise = n + 1 + somaFatorial (n-1)
-------------------------------------------

--8.5-calcule 2ˆ0 + 2ˆ1 + 2ˆ2 + ... + 2ˆn--
somaPot::Integer->Integer
somaPot n
    |n == 0 = 1
    |otherwise = eleven n + somaPot (n-1)
------------------------------------------

--8.6
--X

--8.7
--X

--8.8
--X

--8.9-------------------------------------
{-
Raiz quadrada inteira de n (o maior natural
cujo quadrado é menor ou igual a n)
-}

raizQI :: Int -> Int
raizQI 0 = 0
raizQI n
    | (r+1)^2 == n = r + 1
    | otherwise = r
    where
        r = raizQI ( n-1 )
--------------------------------------------------


--1-Produto dos elementos de uma lista de inteiros
prodInt :: [Int] -> Int
prodInt [] = 0
prodInt (x:xs) = x * prodInt (xs)
-----------------------------------------------

--2------Elimina os números pares--------------
filtra :: [Int] -> [Int]
filtra [ ] = [ ]
filtra (x:xs)
    |((mod x 2) == 0) = filtra xs
    |otherwise = x: filtra xs
-----------------------------------------------

--3-Verificar se um string é formado somente por caracteres alfanuméricos
verAlfaNum :: String -> Bool
verAlfaNum [] = False
verAlfaNum (s:st)
    | isAlphaNum s == elem s (s:st) = True
    | otherwise = verAlfaNum st
--------------------------------------------

--4--Eliminar a primeira ocorrência de um dado elemento-------
returnF :: Int -> [Int] -> [Int]
returnF x [] = []
returnF x (n:ns)
 | x == n = ns
 | otherwise = n: returnF x ns
-------------------------------------------------------

--5-Eliminar todas as ocorrências de um dado elemento.--
delAll :: Int -> [Int] -> [Int]
delAll z [] = []
delAll z (n:ns)
 | z == n = delAll z ns
 | otherwise = n: (delAll z ns)
----------------------------------------------------

--6---------Inverter um string----------------------
invertString :: String -> String
invertString [ ] = [ ]
invertString (x:xs) = invertString xs ++ [x]
-------------------------------------------

{-8.11----------------------------------------------------------
A função or aplica o operador ou lógico || a todos os elementos
de uma lista.
-}-------------------------------------------------------------
or2 :: [Bool] -> Bool
or2 [] = False
or2 (x:xs) = x || or2 xs
-----------------------------------------------------------------

------------------AULA 10--------------------------

-- 10.1----------------------------------------------------------
{-- Definir propriedades da função maior e testar com
quickCheck--}

maior :: [Int] -> Int
maior [x] = x
maior (x:xs) = max x (menor xs)

prop_maior :: [Int] -> Bool
prop_maior [] = False
prop_maior (x:xs)
    | max x (maior xs) == maximum (x:xs) = True
    | otherwise = False
----------------------------------------------------------------

-- 10.2---------------------------------------------------------
{-- Definir uma função menor para calcular o menor de uma
lista de inteiros --}
menor :: [Int] -> Int
menor [x] = x
menor (x:xs) = min x (menor xs)
---------------------------------------------------------------

-- 10.3--------------------------------------------------------
{-- Definir propriedades da função menor e testar com
quickCheck --}
prop_menor :: [Int] -> Bool
prop_menor [] = False
prop_menor (x:xs)
  | min x (menor xs) == minimum (x:xs) = True
  | otherwise = False
-------------------------------------------------------------

-- 10.4---Filtra Posições Pares-------------------------------
filtraPosicoesPares :: [Int] -> [Int]
filtraPosicoesPares [ ] = []
filtraPosicoesPares [x] = []
filtraPosicoesPares (x1:x2:xs) = x2 : filtraPosicoesPares(xs)
--------------------------------------------------------------

-- 10.5---Filtra Posições Impares-----------------------------
filtraPosicoesImpares :: [Int] -> [Int]
filtraPosicoesImpares [ ] = [ ]
filtraPosicoesImpares [x] = [x]
filtraPosicoesImpares (x1:x2:xs) = x1 : filtraPosicoesImpares (xs)





-- ++++++++++++++Exercícios do Livro+++++++++++++++++++++++++++

--7.8--------------------------------------
elenNum :: Integer -> [Integer] -> Integer
elenNum y [ ] = 0
elenNum y (x:xs)
    | y == x = 1 + elenNum y xs
    |otherwise = elenNum y xs
-------------------------------------------

-- 7.9------------------------------------
unique :: [Integer] -> [Integer]
unique [ ] = [ ]
-- unique [b] = [b]
unique (x:xs)
    | (elem x xs) = unique xs
    | otherwise   = x:unique xs
-----------------------------------------

-- 7.10----------------------------------
propUniqueNum :: Integer -> [Integer] -> Bool
propUniqueNum n ls
    |(elenNum n (unique ls)) == 1 || (elenNum n (unique ls)) == 0 = True
    |otherwise = False

--7.12----------------------------------
myMax :: [Integer] -> Integer
myMax [] = error "Lista Vazia"
myMax (x:xs) = go x xs
  where
    go m [] = m
    go m (y:ys)
        | m > y    = go m ys
        |otherwise =  go y ys

myMin :: [Integer] -> Integer
myMin [] = error "Lista Vazia"
myMin (x:xs) = go x xs
  where
    go m [] = m
    go m (y:ys)
        | m < y    = go m ys
        |otherwise =  go y ys



iSort :: [Integer] -> [Integer]
iSort [] = []
iSort (x:xs) = ins x (iSort xs)

ins :: Integer -> [Integer] -> [Integer]
ins x [] = [x]
ins x (y:ys)
   | x <= y = remove (x:(y:ys))
   |otherwise = y : ins x ys

-- 7.13-----------------------------------
--X

--7.14------------------------------------
isSorted :: [Integer] -> Bool
isSorted (x:xs) = head (iSort(x:xs)) == myMin (x:xs)
------------------------------------------

--7.16------------------------------------
remove :: [Integer] -> [Integer]
remove [x] = [x]
remove [ ] = [ ]
remove (x:xs)
    | (elenNum x xs < 1) = x : remove xs -- Usando a função elenNum para não retorna elementos repetidos
    | otherwise  = remove (xs)
------------------------------------------

--7.17------------------------------------
qSort :: [Int] -> [Int]
qSort [] = []
qSort (x:xs)
    = qSort [ y | y<-xs, y > x ] ++ [x] ++ qSort [ y | y<-xs, y < x ]
------------------------------------------

--7.18-------------------------------------------
sublist :: Eq a => [a] -> [a] -> Bool
sublist [] _ = True
sublist _ [] = False
sublist (x:xs) (y:ys)
    | x == y && sublist xs ys = True
    | sublist (x:xs) ys = True
    | otherwise = False

subs :: Eq a => [a] -> [a] -> Bool
subs [] _ = True
subs _ [] = False
subs (x:xs) (y:ys)
    | x == y && xs == [] = True
    | ys == [] && xs /= [] = False
    | x == y && x1 == y1 && subs x1s y1s = True
    | subs (x:xs) ys = True
    | otherwise = False
    where
    (x1:x1s) = xs
    (y1:y1s) = ys
---------------------------------------------------

--7.20---------------------------------------------
mytake :: Int -> [a] -> [a]
mytake 0 _  = []
mytake _ [] = []
mytake n (a:as) = a: mytake (n-1) as

mydrop :: Int -> [a] -> [a]
mydrop _ [ ]  = [ ]
mydrop n (a:as)
    |n > 0  = mydrop (n-1) as
    |otherwise = (a:as)

mysplitAt :: Int -> [a] -> ([a],[a])
mysplitAt _ [ ]    = ([],[])
mysplitAt n (a:as)
    | n > 0 = (mytake n (a:as), mydrop n (a:as))
    |otherwise = ([],(a:as))
------------------------------------------------

--Testes para mydrop e mysplitAt---------------
prop_mydrop ::  Int -> [Int] -> Bool
prop_mydrop n ls
    |(mydrop n ls) == (drop n ls) = True
    |otherwise = False

prop_mysplitAt ::  Int -> [Int] -> Bool
prop_mysplitAt n ls
    |(mysplitAt n ls) == (splitAt n ls) = True
    |otherwise = False
-----------------------------------------------

--7.25-----------------------------------------
my_sublist :: Eq a => [a] -> [a] -> Bool
my_sublist [] [] = True
my_sublist _ [] = False
my_sublist [] _ = True
my_sublist (x:xs) (y:ys)
    |(x == y)  = my_sublist xs ys
    |otherwise = my_sublist (x:xs) ys

my_subsequence :: Eq a => [a]->[a]->Bool
my_subsequence [] [] = True
my_subsequence [] _  = True
my_subsequence _ []  = False
my_subsequence (x:xs) (y:ys)
    |(x == y) = my_subsequence xs ys
    |(x /= y) = my_subsequence (x:xs) ys
    |otherwise = my_subsequence (y:ys) xs
---------------------------------------------

--7.26---------------------------------------
prop_sublist :: [Char] -> [Char] -> Bool
prop_sublist x y = (my_sublist x y)

prop_subsequence :: [Char] -> [Char] -> Bool
prop_subsequence x y = (my_subsequence x y)
---------------------------------------------
