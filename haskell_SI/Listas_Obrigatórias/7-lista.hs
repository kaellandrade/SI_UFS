import Data.List
import Data.Char

--Exercícios 5.6, 14.1, 14.2, 14.3, 14.4, 14.5, 14.6, 14.15
--Todos os do arquivo "aula29 IO.hs" e adicionalmente o exercício 8.15

----------------------------TIPOS ALGÉBRICOS---------------------------------
--5.6
infixr 5 :.:
type Par = (String, Int)
data Itemtype a = Vazia | a :.: (Itemtype a) -- Cons é meu construtor
    deriving(Show)

--14.1
type Name = String
type Book = Int
data People = People Name Book
    deriving(Show, Read)

--14.2
data Person = Person {
    autor :: String, 
    cds :: String,
    videos :: String,
    book :: String
    }deriving (Show, Eq)


--14.3 Give calculations
{-

eval (Lit 67) = 67

eval (Add (Sub (Lit 3) (Lit 1)) (Lit 3) = 
(eval (Lit 3) - eval (Lit 1)) + eval (Lit 3) =
(3 - 1) + 3 = 5

show' (Add (Lit 67) (Lit (-34))) = 
"(show' (Lit 67)) + (show' (Lit(-34)))" ==
"(67 + (-34))"
-}

{-14.4 Defina uma função que conta os números de
operadores em uma expressão
-}
-- size :: Expr -> Integer
-- size (Lit n) = 0
-- size (Add e1 e2) = 1 + (size e1) + (size e2)
-- size (Sub e1 e2) = 1 + (size e1) + (size e2)
-- size (Mul e1 e2) = 1 + (size e1) + (size e2)
-- size (Div e1 e2) = 1 + (size e1) + (size e2)


{-14.5
Adicione as operações de multiplicação e divisão inteira ao
tipo Expr e redefina as funções eval, show e size para incluir esses novos casos.
O que sua definição de eval faz quando solicitada uma a executar uma divisão por zero ?

    >> eval (Add (Div (Lit 5) (Lit 0)) (Sub (Lit 5) (Lit 4)))
    >> Infinity
-}
-- data Expr = Lit Float |
--             Add Expr Expr |
--             Sub Expr Expr |
--             Div Expr Expr |
--             Mul Expr Expr
--             deriving (Show, Read)


data Expr = Lit Float |
            Op Ops Expr Expr | 
            If BExp Expr Expr
            deriving (Show, Read)

data BExp = BooLit Bool |
            And BExp BExp |
            Not BExp |
            Equal Expr Expr |
            Greater Expr Expr
            deriving (Show, Read)

data Ops = Add | Sub | Mul | Div
    deriving (Show, Read)

show' :: Expr -> String
show' (Lit n) = show n 
show' (Op Add e1 e2) ="(" ++ show' e1 ++ " + " ++ show' e2 ++ ")"
show' (Op Sub e1 e2) ="(" ++ show' e1 ++ " - " ++ show' e2 ++ ")"
show' (Op Div e1 e2) ="(" ++ show' e1 ++ " / " ++ show' e2 ++ ")"
show' (Op Mul e1 e2) ="(" ++ show' e1 ++ " * " ++ show' e2 ++ ")"

{-14.15-}
eval :: Expr -> Float
eval (Lit n) = n
eval (Op Add e1 e2) = (eval e1) + (eval e2)
eval (Op Sub e1 e2) = (eval e1) - (eval e2)
eval (Op Div e1 e2) = (eval e1) / (eval e2)
eval (Op Mul e1 e2) = (eval e1) * (eval e2)

bEval :: BExp -> Bool
bEval (BooLit b) = b
bEval (And e1 e2) = (bEval e1) == (bEval e2)
bEval (Not e1) = not (bEval e1)
bEval (Equal e1 e2) = (eval e1) == (eval e2) -- Recursão mútua aqui, estou chamando eval.
bEval (Greater e1 e2) = (eval e1) > (eval e2) -- Recursão mútua aqui, estou chamando eval.

-- Testando com os valores
--bEval (Equal (Op Add (Lit 2) (Lit 2)) (Op Sub (Lit 10) (Lit 6))

---------------------------IO------------------------------------------
-- Funções auxiliares
getReadable :: Read a => IO a
getReadable = do 
    valor <- getLine
    return (read valor)

{-1 escreva um programa com IO que leia uma linha de entrada
e verifique se a linha lida é ou não uma palavra palíndroma.
-}
isPalindroma :: IO()
isPalindroma = do 
    palavra <- getLine
    if (palavra == reverse palavra)
        then 
            putStrLn "É palindroma!"
        else
            putStrLn "Não é palindroma!"

{-2 Escreva um programa que leia um inteiro (Int) n e um Float f
e que imprima o valor de f elevado à n. Oprograma deverá pedir cada uma das entradas e escrever
o resultado em uma mensagem apropriada
-}
elevaNF :: IO()
elevaNF = do
    putStrLn "Base: "
    f <- getReadable :: IO Float
    putStrLn "Espoente: "
    n <- getReadable :: IO Int
    let valor = f ^ n
    putStrLn $ show f ++ "^" ++ show n ++ " = " ++ show valor


{-3 Escreva um programa que leia vários números inteiros, todos digitados uma mesma linha,
e que imprima a soma de todos eles.
-- Dica: use a função words para quebrar um string em "palavras"
-}
lerNuns :: IO()
lerNuns = do
    numeros <- getLine
    let soma = sum $ map (\x-> read x :: Int ) (words numeros)
    putStrLn $ show soma

{-4 Defina a função putNtimes :: Integer -> String -> IO()
tal que o efeito de putNtimes n str é escrever na tela o string str, n vezes, um por linha.
-}
putNtimes :: Integer -> String -> IO()
putNtimes 0 str = return ()
putNtimes n str = do
    putStrLn str
    putNtimes (n-1) str

{-5 Escreva um programa que leia primeiro um número, digamos n, depois leia n números inteiros
e então escreva a soma deles. O programa deverá escrever mensagens apropriadas pedindo dados
e dizendo qual é o resultado.
-}


somaN :: IO()
somaN = do
    putStrLn "Quantos números deseja ler ?"
    n <- getReadable :: IO Int
    soma <- auxiliar n 0
    putStrLn $ "Sua soma foi: " ++ show soma

auxiliar :: Int -> Int -> IO Int
auxiliar 0 a = return(a)
auxiliar n a = do
    m <- getReadable :: IO Int 
    auxiliar (n-1) (a+m)

{-6 Escreva um programa que leia uma sequência de números inteiros
finalizada por 0 e escreva a soma de todos eles. O programa deverá
escrever mensagens apropriadas pedindo dados e dizendo qual é o resultado
-}

somaate0 :: Int -> IO ()
somaate0 n = 
    do 
        valor <- getReadable :: IO Int
        if valor == 0
            then
                putStrLn $ "Sua soma foi: " ++ show n
            else
                somaate0 (n+valor)
-- Chama minha função soma
callsum :: IO ()
callsum = somaate0 0


{-7 Escreva um programa wc que lê linhas até que uma linha vazia é digitada.
O programa deverá escrever o número de linhas, número de palavras e número de caracteres
que foram lidos.
-}
wc :: String -> Int -> IO ()
wc palavras linhas = do
    putStrLn " Digite palavras, tecle enter para finalizar."
    valor <- getLine 
    if (valor == "")
        then
            putStrLn $ "Número de linhas lidas: " ++ show ( linhas)
            ++ "\nNúmero de palavras lidas: " ++ show (length (words palavras))
            ++ "\nNúmero de Char lidos: " ++ show (length palavras)
        else
            wc (palavras ++ " " ++ valor) (linhas + 1)
callWC :: IO()
callWC = wc [] 0


{-8 Escreva um programa que lê números inteiros até ser digitado 0.
O programa de escrever a sequência de números lidos, porém em ordem crescente.
-}


lerInteiros :: [Int] -> IO()
lerInteiros numeros = do
    numero <- getReadable :: IO Int 
    if (numero == 0)
        then
            putStrLn $ show (sort numeros)
        else
            lerInteiros (numeros ++ [numero])

callerInteiros :: IO()
callerInteiros = lerInteiros []

----8.15 - Verifica se é um palindromo, sem considerar maiusculas, espaços e pontuações.
epalindromo :: IO ()
epalindromo = do
    linha <- getLine
    let palavra = map toLower $ filter isLetter linha
    if (palavra == reverse palavra)
        then
            putStrLn "É palindromo!"
        else
            putStrLn "Não é palindromo!"