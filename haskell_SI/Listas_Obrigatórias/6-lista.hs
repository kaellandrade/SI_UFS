{-
Do livro Haskell: The craft of functional programming, 3d ed, os exercícios
9.5, 9.6, 9.7, 9.9, 9.11,
11.25, 11.26, 11.29, 11.32 e 11.33
-}

{- 9.5 provar que sum (xs ++ ys) = sum xs + sum ys

Definição das funções
---------------------------------------
(sum ++)
sum [] = 0                 -- (sum.1)
sum (z:zs) = z + sum zs    -- (sum.2)


[] ++ zs = zs              --(++.1)
(z:zs) ++ ws = z: (zs++ws) --(++.2)
--------------------------------------

CONFIGURANDO A INDUÇÃO

sum ([]++ys) = sum [] + sum ys        <- CASO BASE

sum((x:xs)++ys) = sum (x:xs) + sum ys <- INDUÇÃO

sum (xs ++ ys) = sum xs + sum ys      <- HIPÓTESE

-------Provando o caso base---------
sum ([]++ys)=
sum ys     --(++.1)

sum [] + sum ys=
0 + sum ys      --(sum.1)
sum ys          --(aritimética)
                               C.Q.D
------------Prova-------------------
sum ((x:xs)++ys)=
sum (x:(xs++ys))  --(++.2)
x+sum(xs++ys)     --(sum.2)
x+sum xs + sum ys --(HIPÓTESE)

sum(x:xs) + sum ys
x+sum xs + sum ys --(sum.2)
                              C.Q.D
-}

{- 9.6 provar que
xs ++ [] = xs
xs ++ (ys++zs) = (xs++ys) ++ zs

Definição de ++
--------------------------------------
[]++[]=[]                  --(++.0)
[] ++ zs = zs              --(++.1)
(z:zs) ++ ws = z: (zs++ws) --(++.2)
--------------------------------------

ONFIGURANDO A INDUÇÃO

[] ++ [] = []           <- CASO BASE

 (x:xs) ++ [] = (x:xs)  <- INDUÇÃO

 xs ++ [] = xs          <- HIPÓTESE

-------Provando o caso base---------
[]++[]=
[]     --(++.0)
                               C.Q.D
------------Prova-------------------
(x:xs)++[]=
x:(xs++[])  --(++.2)
x:xs        --(HIPÓTESE)

(x:xs)=
x:xs       --(aritimética)
                              C.Q.D
-}

{-? 9.7 provar que
sum (reverse xs) = sum xs       --(prova1)
length (reverse xs) = lenght xs --(prova2)

Definição de (reverse,sum,lengh e ++)
---------------------------------------------
reverse [] = []                    --(reve.1)
reverse (z:zs) = reverse zs ++ [z] --(reve.2)

sum [] = 0               --(sum.1)
sum (z:zs) z + sum zs =  --(sum.2)

length [] = 0                -- (length.1)
length (z:zs) = 1 + legth zs -- (length.2)


[]++[]=[]                  --(++.0)
[] ++ zs = zs              --(++.1)
(z:zs) ++ ws = z: (zs++ws) --(++.2)
--------------------------------------------

ONFIGURANDO A INDUÇÃO --(prova1)

sum (reverse []) = sum []         <-CASO BASE

sum (reverse (x:xs)) = sum (x:xs) <- INDUÇÃO

sum (reverse xs) = sum xs         <- HIPÓTESE

-------Provando o caso base---------
LADO ESQUERDO
sum (reverse []) =
sum [] --(reve.1)
0      --(sum.1)

LADO DIREITO
sum [] =
0     --(sum.1)

                               C.Q.D
------------Prova-------------------
LADO ESQUERDO
sum (reverse (x:xs))=
sum (reverse xs ++ [x]) --(reve.2) -- ?

LADO DIREITO
sum xs =
sum (x:xs)
x + sum xs --(sum.2)
-}

{- 9.8 provar que elem z (xs ++ ys) = elem z xs || lem z ys

Definição de (elem e ++)
---------------------------------------------
[]++[]=[]                  --(++.0)
[] ++ zs = zs              --(++.1)
(z:zs) ++ ws = z: (zs++ws) --(++.2)

elem z [] = False                 --(elem.1)
elem z (w:ws) = z==w || elem z ws --(elem.2)

ONFIGURANDO A INDUÇÃO
elem z ([] ++ ys) = elem z [] || lem z ys         <-CASO BASE

elem z ((x:xs) ++ ys) = elem z (x:xs) || lem z ys <- INDUÇÃO

elem z (xs ++ ys) = elem z xs || elem z ys         <- HIPÓTESE

-------Provando o caso base---------
LADO ESQUERDO
elem z ([]++ys) =
elem z ys --(++.1)

LADO DIREITO
elem z [] || lem z ys =
False || elem z ys (--) --(elem.1)
elem z ys               --(Pela definição de or)

                        C.Q.D
----------------Prova----------------
LADO ESQUERDO
elem z ((x:xs)++ys)=
elem z (x:(xs++ys)) --(++.2)
z == x || elem z ys --(elem.2)

LADO DIREITO
elem z (x:xs) || elem z ys =
z==x  || elem z xs || elem z ys     --(elem.2)
z==x || elem z (xs ++ ys)           --(HIPÓTESE)
z==x || elem z ys                   --(++1)

                                                C.Q.D
-}

{-? 9.9 provar que zip (fst (unzip ps)) (snd (unzip ps)) = ps
 e unzip (zip xs ys) = (xs,ys)

Definição de (unzip, zip, fst, snd)
---------------------------------------------
fst (p1,_) = p1                     --(fst.1)
snd (_,p2) = p2                     --(snd.1)

zip _ [] = []                       --(zip.1)
zip [] _ = []                       --(zip.2)
zip (x:xs) (y:ys) = (x,y):zip xs ys --(zip.3)

unzip [] = ([],[])                  --(unzip.1)
unzip ((x,y):ps) = (x:xs, y:ys)     --(unzip.2)
   where                            --(unzip.3)
      (xs,ys) = unzip ps            --(unzip.4)


prova 1-------------------------------------------------------------------
CONFIGURANDO A INDUÇÃO
zip (fst (unzip [])) (snd (unzip [])) = []            <- CASO BASE

zip (fst (unzip (p:ps))) (snd (unzip (p:ps))) = (p:ps)<- INDUÇÃO

zip (fst (unzip ps)) (snd (unzip ps)) = ps            <- HIPÓTESE

-------Provando o caso base---------
LADO ESQUERDO
zip (fst (unzip [])) (snd (unzip [])) =
zip (fst ([],[])) (snd ([],[]))        --(unzip.1)
zip ([]) ([])                          --(zip.2)
[]

LADO DIREITO
= []
[]
                                  C.Q.D

----------------Prova----------------
LADO ESQUERDO
zip (fst (unzip (p:ps))) (snd (unzip (p:ps))) =
zip (fst (p:ps, p:ps)) (snd (p:ps, p:ps)) --(unzip.2)
zip p:ps p:ps                             --(fst.1, snd.1)
(p,p):zip ps ps                           --(zip.3)
??????????????

2 prova----------------------------------------------------
CONFIGURANDO A INDUÇÃO
unzip (zip [] ys) = ([],ys)         <- CASO BASE

unzip (zip (x:xs) ys) = ((x:xs),ys) <- INDUÇÃO

unzip (zip xs ys) = (xs,ys)         <- HIPÓTESE
-------------Provando o caso base--------------------------
LADO ESQUERDO
unzip (zip xs [])=
unzip []     --(unzip.1)
([],[])

LADO DIREITO
([],ys) =

LOGO não está definido par lista vazia ([],[]) /= ([],ys)

----------------Prova----------------
LADO ESQUERDO
unzip (zip (x:xs) ys) =
unzip (x,y):zip xs ys  --(zip.3)
(xs,ys)                --(HIPÓTESE)
unzip ps               --(unzip.4)

LADO DIREITO
((x:xs),ys)=
unzip ps             --(unzip.4)
                                  C.Q.D
-}

{-9.11
Write QuickCheck properties for the propositions that you have proved,
and check that indeed hold.
-}

--9.5
prop_sum_concat::[Int] -> [Int] -> Bool
prop_sum_concat xs ys = sum(xs ++ ys) == sum xs + sum ys

--9.6
prop_concat :: [Int] -> [Int] ->Bool
prop_concat xs ys = (xs ++ [] == xs) && (xs ++ (ys ++ ys) == (xs++ys) ++ ys)

--9.7
prop_sum_reve :: [Int] -> Bool
prop_sum_reve xs = sum (reverse xs) == sum xs && length (reverse xs) == length xs

--9.9
prop_zip :: [(Int,Int)] -> Bool
prop_zip xs = zip(fst(unzip xs)) (snd (unzip xs)) == xs

prop_zip_unzip ::[(Int, Int)] -> [(Int, Int)] -> Bool
prop_zip_unzip xs ys = unzip (zip xs ys) == (xs,ys)
--Como foi provado, prop_zip_unzip não está definida para
--o caso base

{-11.25 Pelo princípio da extensionalidade mostrar que f . (g . h) = (f . g) . h

definiçõa de (.)
(.) f g = f (g x)

LADO ESQUERDO
f . (g . h)=
f . g (h)
f (g (h))

LADO DIREITO
(f . g) . h=
f (g . h)
f (g (h))

-}

{-11.26 mostre que para todo f, id . f = f
Definição de (id)
id x =  x --(id.1)

(id . f) x = f x
id (f x) = f x
f x = f x --(id.1)
-}
