{-
--Definindo os tipos para estaão
data Estacao = Verao | Outono | Inverno | Primavera
   deriving (Eq, Ord, Enum, Show, Read)

chove :: Estacao -> Bool
chove Inverno = True
chove _ = False

--2
data CondicaoClima = Quente | Frio | Agradavel
   deriving (Eq, Ord, Enum, Show, Read)

condicao :: Estacao -> CondicaoClima
condicao Verao = Quente
condicao Outono = Agradavel
condicao Inverno = Frio
condicao Primavera = Agradavel

condicao' :: Estacao -> CondicaoClima
condicao' e
    |e == Verao = Quente
    |e == Inverno = Frio
    |otherwise = Agradavel

--3
--Definindo o tipo para meses.
data Mes = Jan | Fev | Mar | Abril | Maio | Jun | Jul | Agost | Set | Out | Nov | Dez
    deriving (Eq, Ord, Enum, Show, Read)

mes_dias_31 = [Jan, Mar, Maio, Jul, Agost, Out, Dez]
dias :: Mes -> Int
dias mes
    | elem mes mes_dias_31 = 31
    | mes == Fev = 28
    | otherwise = 30

--Definindo o tipo da figura geometrica.
type Posicao = (Float, Float)
data Figura = Retangulo Float Float Posicao | Circulo Float Posicao
  deriving (Eq, Show, Read)

--Calcula a área
-- a = Altura
-- c = Hipotenusa
-- b = base
area :: Figura -> Float
area (Retangulo b a c) = b * a
area (Circulo r c)     = pi * r^2

mover :: (Float, Float) -> Figura -> Figura
mover (x,y) (Retangulo b a (x1,y1)) = Retangulo b a (x+x1,y+y1)
mover (x,y) (Circulo r (x1,y1)) = Circulo r (x+x1,y+y1)

--Verifica se é um círculo
eredondo :: Figura -> Bool
eredondo (Circulo _ _) = True
eredondo _ = False

--Tipo pessoa
pessoa = Person "Mikael" "Andrade" 23 1.70 "75-192-8475" "Floresta Negra"
--sintaxe de registro
data Person = Person { 
    firstName :: String,
    lastName :: String,
    age :: Int,
    height :: Float,
    phoneNumber :: String,
    flavor :: String
    }deriving (Show, Eq)
{-
 Essa notação permite criar funções que consultam os campos no tipo de dado.
-}

-- Tipo Car
data Car = Car {
    company :: String,
    model :: String,
    year :: Int
} deriving (Show)

tellcar :: Car -> String
tellcar (Car {company=c, model=m, year=y}) = "Este é o " ++ c ++ " " ++ m ++ " " ++ "produzido em " ++ show(y)

--Tipos paramétricos
data Maybe' a = Nothing' | Just' a deriving (Show)

-- Meu Boleano
data Day = Segunda | Terca | Quarta | Quinta | Sexta | Sábado | Domingo 
    deriving(Show, Eq, Ord, Read, Bounded, Enum)

type Nome     = String
type Telefone = String
type ListaTelefonica = [(Nome, Telefone)]

database = [
    ("Kaell", "12345678"),
    ("José", "1234567890"),
    ("Maria", "123")]

findbook :: Nome -> Telefone -> ListaTelefonica -> Bool
findbook nome telefone lista = elem (nome,telefone) lista

--Estruturas de dados recursivas
infixr 5 :-:
infixr 5 .++
infixr 5 :.:
data List a = Empty | a :-: (List a)
    deriving (Show, Read, Eq, Ord)

--Minha função para concatenar    
(.++) :: List a -> List a -> List a
Empty .++ ys = ys
(x:-:xs) .++ ys= x:-:(xs .++ ys)

sumsum :: List Int -> Int
sumsum Empty = 0
sumsum (x:-:xs) = x + sumsum xs

--
data ListInt = Vazia | Int :.: (ListInt)
    deriving(Show, Read, Eq, Ord)

length' :: ListInt -> Int
length' Vazia = 0
length' (x :.: xs) = 1 + length' xs

cabeca :: ListInt -> Int
cabeca (x :.: _ ) = x

data Expr = Lit Int |
            Add Expr Expr |
            Sub Expr Expr |
            Mult Expr Expr
    deriving (Eq, Show)

-- eval :: Expr -> Int
-- eval (Lit n) = n
-- eval (Add e1 e2) = (eval e1) + (eval e2)
-- eval (Mult e1 e2) = (eval e1) * (eval e2)

show' :: Expr -> String
show' (Lit n) = show n
show' (Add e1 e2) = "(" ++ show e1 ++ " + " ++ show e2 ++ ")"
show' (Mult e1 e2) ="(" ++ show e1 ++ " * " ++ show e2 ++ ")"


assoc :: Expr -> Expr
assoc (Lit n ) = Lit n
assoc (Sub e1 e2) = Sub (assoc e1) (assoc e2)
assoc (Add (Add e1 e2) e3) = assoc (Add e1 (Add e2 e3))
assoc (Add e1 e2) = Add (assoc e1) (assoc e2)


-- Tipos algebricos polimórficos
data Par a = Pares a a deriving( Show, Read)
-- data [a] = [] | a : [a]
data Lista a = Vazia | Cons a (Lista a)
    deriving(Show, Read)

--Representação do tipo *União Discriminada*
data Eitherr nome numero = Nome nome | Numero numero
    deriving(Eq, Ord, Read, Show)

-- isLeft :: Eitherr a b -> Bool
-- isLeft (Esq a) = True
-- isLeft _ = False

eitherr :: (nome->c) -> (numero -> c) -> Eitherr nome numero -> c
eitherr f g (Nome x) = f x
eitherr f g (Numero y) = g y

-- Lidando com erros
data Maybe' a = Nothing' | Just' a
    deriving (Eq, Ord, Show, Read)

divideF :: Float -> Float -> Maybe' Float
divideF m n
    | n /= 0 = Just' (m / n)
    | otherwise = Nothing'

--Transmite o erro
mapMaby :: (a->b) -> Maybe' a -> Maybe' b
mapMaby f Nothing' = Nothing'
mapMaby f (Just' x) = Just' (f x)

--Captura o erro
maybee :: b -> (a->b) -> Maybe' a -> b
maybee n f Nothing' = n
maybee n f (Just' x) = f x

parIgual :: Eq a => Par a -> Bool
parIgual (Pares x y) = (x==y)

data Tree a = Nil | Node a (Tree a) (Tree a)
    deriving(Eq, Ord, Show, Read)

depth :: Tree a -> Int
depth Nil = 0
depth (Node n t1 t2) = 1 + max (depth t1) (depth t2)

collapse :: Tree a -> [a]
collapse Nil = []
collapse (Node x t1 t2)
    = collapse t1 ++ [x] ++ collapse t2
-}

data Tree a = EmptyTree | Node a (Tree a) (Tree a)
    deriving (Show, Read, Eq)

singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree

treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x EmptyTree = singleton x
treeInsert x (Node a left right)
    | x == a = Node x left right
    | x < a = Node a (treeInsert x left) right
    | x > a = Node a left (treeInsert x right)

treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node a left right)
    |x == a = True
    |x < a  = treeElem x left
    |x > a  = treeElem x right
