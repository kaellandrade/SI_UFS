import Data.Char
--Elimina a cabeça
drop' :: Int -> [Int] -> [Int]
drop' _ [] = []
drop' 0 (x:xs) = (x:xs)
drop' n (x:xs) = drop'(n-1) xs

eliminaRep :: [Int] -> [Int]
eliminaRep [x] = [x]
-- eliminaRep [] = []
eliminaRep (x:xs)
    | elem x xs = eliminaRep xs -- Verifica
    |otherwise = x: eliminaRep xs


eliminaRep' :: [Int] -> [Int]
eliminaRep' [x] = [x]
eliminaRep' [] = []
eliminaRep' (x1:x2:xs)
    | x1 == x2  = eliminaRep' (x2:xs)
    | otherwise = x1 : eliminaRep' (x2:xs)


--3--Retorna a primeira palavra de uma string.
primeira_palavra:: [Char] -> [Char]
primeira_palavra  ""=""
primeira_palavra (x:xs)
    |x == ' ' = ""
    |otherwise = x:(primeira_palavra xs)


--6 Dada uma lista de pontos cartesianos (x,y), calcular
-- a distância do percurso que eles representam.


-- calcula_pontos :: [(Int, Int)] -> Float
-- calcula_pontos [x] = 0
-- # Praticando

doubleAll :: [Int] -> [Int]
doubleAll [ ] = [ ]
doubleAll (x:xs) = (x * 2): doubleAll xs

roundAll :: [Float] -> [Int]
roundAll xs = map' round xs

capitalize :: String -> String
capitalize [] = []
capitalize (c:cs) = toUpper c : capitalize cs

map' :: (a->b) -> [a] -> [b]
map' f [ ] = [ ]
map' f (x:xs) = f x: map' f xs

{-
zipWith' recebe uma função e duas listas
-}
zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' f _ [] = []
zipWith' f [] _ = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

--flip' inverte a os valores
flip' :: (a->b->c) -> b -> a -> c
flip' fun y x = fun x y

filter' :: (a->Bool) -> [a] -> [a]
filter' fun [] = []
filter' fun (x:xs)
    | fun x = x: filter' fun xs
    | otherwise = filter' fun xs

maiusculas :: String -> String
maiusculas cs = filter' isUpper cs
