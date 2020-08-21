--zip
myzip :: [a] -> [b] -> [(a,b)]
myzip (a:as) (b:bs) = (a,b): myzip as bs
myzip _ _ = [ ]

--take
mytake :: Int -> [a] -> [a]
mytake 0 _  = []
mytake _ [] = []
mytake n (a:as) = a: mytake (n-1) as
--


--7.20
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


--Testes
prop_mydrop :: Eq a => Int -> [a] -> Bool
prop_mydrop n ls
    |(mydrop n ls) == (drop n ls) = True
    |otherwise                    = False

--7.25
sublist :: Eq a => [a] -> [a] -> Bool
sublist [] [] = True
sublist _ [] = False
sublist [] _ = True
sublist (x:xs) (y:ys)
    |(x == y)  = sublist xs ys
    |otherwise = sublist (x:xs) ys


subsequence :: Eq a => [a]->[a]->Bool
subsequence [] [] = True
subsequence [] _  = True
subsequence _ []  = False
subsequence (x:xs) (y:ys)
    |(x == y) = subsequence xs ys
    |(x /= y) = subsequence (y:ys) xs
    |otherwise = subsequence (x:xs) ys

--7.9
unique :: [Int] -> [Int]
unique [ ] = [ ]
-- unique [b] = [b]
unique (x:xs)
    | (elem x xs) = unique xs
    | otherwise   = x:unique xs

data Expr = Lit Integer | 
            Op Ops Expr Expr
            deriving (Show, Read)

data Ops = Add | Sub | Mul | Div
    deriving (Show, Read)

-- (Op Add (Lit 3) (Lit 2))
-- (5+5) * 2 == Op Mul (Op Add (Lit 5) (Lit 5)) (Lit 2)