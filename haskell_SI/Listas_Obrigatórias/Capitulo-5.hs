import Data.Char
--5.1
maxOccurs :: Integer -> Integer -> (Integer, Integer)
maxOccurs x y
    |x >= y    = (y, x)
    |otherwise = (x, y)

--5.2
{-
Função que coloca uma Tripla em order crescente.
-}
orderTriple :: (Integer, Integer, Integer) -> (Integer, Integer, Integer)
orderTriple (x, y, z)
    | (x <= y) && (y <= z) = (x, y, z)
    | (x <= z) && (z <= y) = (x, z, y)
    | (y <= x) && (x <= z) = (y, x, z)
    | (y <= z) && (z <= x) = (y, z, x)
    | (z <= x) && (x <= y) = (z, x, y)
    | otherwise            = (z, y, x)

--5.3
-- Obs:
-- Função que verifica quando uma linha reta cruza o eixo-x
-- a é um coeficiente angular da reta;
-- b é o coeficiente linear;
cruzax :: (Float, Float) -> String
cruzax (a, b)
    | a == 0 = "A reta nao cruza o eixo X"
    | otherwise = show ((-b)/(a))

--5.4
--Testando maxOccurs
{-
>> maxOccurs 3 1
>> (1,3)

>>maxOccurs 60 3
>> (3, 60)
-}

--Testando orderTriple
{-
>> orderTriple (20, 0, 2)
>> (0, 2, 20)

>>orderTriple (0, 20, 3)
>> (0, 3, 20)
-}

--Testando cruzax
{-
>> (2, 3)
>> "-2.0" -- Note que a reta corta o eixo x em -2.00

>> (0, 2)
>> "A reta nao cruza o eixo X" -- Pois o coeficiente angular é 0. Portanto, ela nunca irá o eixo x.
-}

--5.18
doubleAll :: [Integer] -> [Integer]
doubleAll mylist = [elemento * 2 | elemento <- mylist]

--5.19
isChar :: Char -> Bool -- Verifica se é um char.
isChar c
    | c `elem` ['a'..'z']      = True
    | c `elem` ['A'..'Z']      = True
    | otherwise                = False

capitalizeLetters :: String -> String -- Função que gera minha nova lista, com valores filtrados.
capitalizeLetters frase = [toUpper letra | letra <- frase, isChar letra] -- Perceba que isChar só retorna False caso o valor não seja uma letra..


--5.20
divisors :: Integer -> [Integer]
divisors number = [num | num <- [1..number], mod number num == 0]

isPrime :: Integer -> Bool
isPrime valor
    | produto == valor                   = True -- Ex: 7 é primo, pois product [1,7] == 7
    | otherwise                          = False
       where
         produto = product (divisors valor) --Usa a função divisor para verificar se tem dois divisores

--5.21
matches :: Integer -> [Integer] -> [Integer]
matches valor ls = [item | item <- ls, item == valor]

elem2 :: Integer -> [Integer] -> Bool
elem2 numero lista
    | length (matches numero lista) >= 1 = True
    | otherwise                          = False


--5.22
convertString :: [String] -> String
convertString listaS = [caracter | listachar <- listaS, caracter <- listachar]

onSeparateLines :: [String] -> String
onSeparateLines ls = convertString [ l ++ "\n" | l <- ls]

--5.23
duplicate :: String -> Integer -> String
duplicate cadeia valor
    | valor == 1 = cadeia
    | valor > 1  = [ c | lista <- repitidas, c <- lista  ] -- extrai da lista os valores.
    | otherwise = " "
    where
      repitidas = [cadeia | x <-[1..valor] ] -- Retona uma lista dos valores repeditos



--5.24
pushRight :: String -> Int -> String
pushRight nome linelengh = espaco ++ nome
    where
      espaco = [' '| num <- [0 .. comprimentonome]]
      comprimentonome = (linelengh) - (length nome)
--5.25
--Criticando a função...
--A função pushRighr funciona muito bem para números positivos, caso contraio não retora o espaço
-- esse erro poderia ser corrigido com abs (retorna o valor absoluto)

-- 5.27
type Persson  = String
type Book     = String
type Database = [(Persson, Book)]

--exampleBase = [("Charlie","poder do habito"),("mikael","vivendo a vida"), ("mikael","haskell"), ("maria","haskell"), ("Roy","produtividade"), ("Jose","produtividade"),]
-- Retorna o nome do(s) livro(s) que a pessoa pegou.
books :: Database -> Persson -> [Book]
books exampleBase findpersson = [book | (pers, book) <- exampleBase, findpersson == pers ]

--5.28
borrowers :: Database -> Book -> [Persson]
borrowers exampleBase2 findbook = [pers | (pers, book) <- exampleBase2, findbook == book]

--Retorna se alguém pegou o livro persquisado.
borrowed :: Database -> Book -> Bool
borrowed exampleBase3 findbook2
    | not (null encontrados) = True
    | otherwise              = False
    where
      encontrados = [ book | (pers, book) <- exampleBase3, findbook2 == book]

-- Função que retorna quantos livros a pessoa está devendo.
numBorroed :: Database -> Persson -> Int
numBorroed exampleBase4 findpersson = length [book | (pers, book) <- exampleBase4, findpersson == pers]

--5.29
exampleBase :: Database
exampleBase = [("Alice", "Tintin"),("Anna","Little Women" ),("Alice","Asterix"),("Rory","Tintin")]

returnLoan :: Database -> Persson -> Book -> Database
returnLoan dBase pers bk
    = [pair | pair <- dBase, pair /= (pers, bk)]

--calculando..
{-
--returnLoan exampleBase "Alice" "Asterix"


   dBase         pers         bk
examplebase    "Alice"     "Asterix"


("Alice", "Tintin")        ("Alice", "Tintin")        <- exampleBase,  ("Alice", "Tintin")       /=  ("Alice","Asterix")   -- True
("Anna","Little Women")    ("Anna","Little Women" )   <- exampleBase,  ("Anna","Little Women" )  /=  ("Alice","Asterix")   -- True
("Alice","Asterix")        ("Alice","Asterix")        <- exampleBase,  ("Alice","Asterix")       /=  ("Alice","Asterix")   -- False
("Rory","Tintin")          ("Rory","Tintin")          <- exampleBase,  ("Rory","Tintin")         /=  ("Alice","Asterix")   -- True

>> [("Alice","Tintin"), ("Ana","Little Women"),("Rory","Tintin")]

--returnLoan exampleBase "Alice" "Little Women"


   dBase         pers         bk
examplebase    "Alice"     "Little Women"


("Alice", "Tintin")        ("Alice", "Tintin")        <- exampleBase,  ("Alice", "Tintin")      /= ("Alice","Little Women")      -- True
("Anna","Little Women")    ("Anna","Little Women" )   <- exampleBase,  ("Anna","Little Women" ) /= ("Alice","Little Women")      -- True
("Alice","Asterix")        ("Alice","Asterix")        <- exampleBase,  ("Alice","Asterix")      /= ("Alice","Little Women")      -- True
("Rory","Tintin")          ("Rory","Tintin")          <- exampleBase,  ("Rory","Tintin")        /= ("Alice","Little Women")      -- True

>> [("Alice", "Tintin"),("Anna","Little Women" ),("Alice","Asterix"),("Rory","Tintin")]

-}


--5.31, 5.33
--Não entedi a questão


--5.34
--Função que formata a saída da função books
formatbooks :: [Book] ->  String
formatbooks [ ] = [ ]
formatbooks (x:xs) = "\n" ++  x ++ formatbooks xs
