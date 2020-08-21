type Picture = [[Char]]

toString :: Picture -> String
toString = concat . map (++ "\n")

cavalo=[".......##...",
         ".....##..#..",
         "...##.....#.",
         "..#.......#.",
         "..#...#...#.",
         "..#...###.#.",
         ".#....#..##.",
         "..#...#.....",
         "...#...#....",
         "....#..#....",
         ".....#.#....",
         "......##...."]

mint_OS = ["#############################",
           "#################################",
            "###      ###                ######",
            "#######  ###  ################# ###",
            "#######  ###  ################# ###",
            "    ###  ###  ################# ###",
            "    ###  ###  ####  ####   #### ###",
            "    ###  ###  ####  ####   #### ###",
            "    ###  ###  ####  ####   #### ###",
            "    ###  #### ####  ####   #### ###",
            "    #### #####################  ###",
            "    ##### ####################  ###",
            "     #########################  ###",
            "      #############################",
            "         ##########################",
            "            #####################  "]

--Para girar na horizontal basta um reverse da ordem das lihas
flipH :: Picture -> Picture
flipH = reverse

above :: Picture -> Picture -> Picture
above = (++)

beside :: Picture -> Picture -> Picture
beside  = zipWith (++)

invertChar :: Char -> Char
invertChar ch
    | ch == '.' = '#'
    |otherwise = '.'


invertLine :: [Char] -> [Char]
invertLine line = map invertChar line

invertColour :: Picture -> Picture
invertColour pic = map invertLine pic

--Irá inverter cada elemento da linha.
flipV :: Picture -> Picture
flipV = map (\x->reverse x)

replicateAll :: Int -> [a] -> [a]
replicateAll n = concat . map(replicate n)

scalar :: Int -> Picture -> Picture
scalar size pic = map (replicateAll size) (replicateAll size pic)

{-
-- Propriedades
prop_AboveFlipV :: Picture -> Picture -> Bool
prop_AboveFlipV pic1 pic2 =
  flipV (above pic1 pic2) == above (flipV pic1) (flipV pic2)

prop_AboveFlipH :: Picture -> Picture -> Bool
prop_AboveFlipH pic1 pic2 =
  flipH (above pic1 pic2) == above (flipH pic1) (flipH pic2)
-}

--SEXTA LISTA OBRIGATÓRIA

{-
Dada a definição
sumPot2 0 = 1
sumPot2 n = 2^n + sumPot2 (n-1)
A seguinte propriedade é válida
sumPot2 n = 2^(n+1) - 1
Prove por indução.
-}

{-
Estabelecendo o caso base
sumPot2 0 = 2^(0+1)-1 = 2^1 - 1 = 1

Estabelecendo minha hipótese
para (n-1)
sumPot2 (n-1) = 2^(n -1 +1) -1 = 2^n - 1
sumPot2 (n-1) = 2^n -1

Provando--------------------------------------------------------!Repete a base e soma os expoentes.
sumPot2 n = 2^n + sumPot2(n-1) = 2^n + 2^n - 1 = 2*2^n - 1 = 2^(n+1) - 1
sumPot2 n = 2^(n+1) - 1
-}


fact :: Int -> Int
fact 0 = 1
fact n = n * fact (n-1)
