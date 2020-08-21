
--Capítulo 6
type Name      = String
type Price     = Int
type BarCode   = Int
type SDatabase = [(BarCode, Name, Price)]

--Banco de dados para o supermercado
codeIndex :: SDatabase
codeIndex = [(4719, "Fishe Fingers", 121),
             (5643, "Nappies", 1010),
             (3814, "Orange Jelly", 56),
             (1111, "Hula Hoops", 21),
             (1112, "Hula Hoops (Giant)",133),
             (1234, "Dry Sherry, 1lt", 540)]

type TillType = [BarCode]
type BillType = [(Name, Price)]

--putStrLn (produceBill [code]) -- Retorna com a quebra de linha
--Leva uma lista de pares (nome, preço) em uma conta formatada
produceBill :: TillType -> String
produceBill = formatBill . makeBill

--6.39
formatPence :: Price -> String
formatPence valor
    | divRest `elem` [1..9] = show (divInt) ++ "." ++ "0" ++ show (divRest) -- para casos como 12.02
    | divRest  == 0 = show (divInt) ++ "."  ++ show (divRest) ++ "0"
    | otherwise =     show (divInt) ++ "."  ++ show (divRest)
    where
      divInt  =  valor `div` 100 -- Retorna a divisão inteira
      divRest = valor  `mod` 100 -- Retorna o resto da divisão

--6.40
formatLine :: (Name, Price) -> String
formatLine (name, preco)
    = name ++ formatoponto ++ formatPence preco ++ "\n"
    where
      tamanho = 30 - (length name + length (show preco))
      formatoponto = ['.' | ponto <- [1..tamanho]] -- Completa os epaços vazios com pontos.


--6.41
formatLines :: [(Name, Price)] -> String
formatLines [ ] = [ ] -- Meu caso base, caso seja uma lista vazia eu quero que retorne uma lista vazia.
formatLines (x:xs) = formatLine x ++ formatLines xs -- Aqui eu apliquei a recursividade e chamei a minha função 'formatLine' para aplicar a formatação.

--6.42
makeTotal :: BillType -> Price
makeTotal listacompra = total - (makeDiscount listacompra) -- estou aplicando o desconto aqui.
    where
        total = sum [ preco | (nome, preco) <- listacompra] --retorna a soma da lista dos precos

--6.43
formatTotal :: Price -> String
formatTotal total
    = "\nTotal" ++ formatoponto ++ formatPence total -- Estou usando a função formatPence definida anterior
    where
      tamanho = 25 - (length (show total))
      formatoponto = ['.' | ponto <- [1..tamanho]] -- Completa os epaços vazios com pontos.

--6.44
formatBill :: BillType -> String
formatBill carrinho
    = "\n******Mikael  Marketplace******\n"++formatLines carrinho ++ formatDiscount (makeDiscount carrinho)++ "\n" ++ formatTotal (makeTotal carrinho)

--6.45
--Pega um código de barra e retorna o Nome e valor do item, caso exista.
look :: SDatabase -> BarCode -> (Name, Price)
look codeIndex findcode
   | listper == [ ] = ("Item desconhecido", 0) -- Caso minha lista esteja vazia
   |otherwise = head listper -- Retorna a cabeça da lista, de uma lista unitária.
   where
     listper = [(nome, valor) | (code, nome, valor) <- codeIndex, (findcode, 0, 0) == (code, 0, 0)] -- Encontra o elemento pelo codigo

--6.46
lookup2 :: BarCode -> (Name, Price)
lookup2 codigo =  look codeIndex codigo -- Usso minha função anterior para verificar se o código digitado está no banco.


--6.47
--Leva uma lista de códigos de barras para uma lista de pares (nome, preço), caso o código esteja no banco de dados.
makeBill :: TillType -> BillType
makeBill codigos = [ lookup2 code | code <- codigos]

--6.48
--Aplica desconto para um determinado produto
makeDiscount :: BillType -> Price
makeDiscount banco = desconto `div` 2 -- returna o desconto para cada dois litros comprados.
    where
      desconto = sum [100 | (nome, preco) <- banco, nome == "Dry Sherry, 1lt"]

--Função que formata o desconto
formatDiscount :: Price -> String
formatDiscount discount
    = "\nDesconto" ++ formatoponto ++ formatPence discount -- Estou usando a função formatPence definida anterior
    where
      tamanho = 22 - (length (show discount))
      formatoponto = ['.' | ponto <- [1..tamanho]] -- Completa os epaços vazios com pontos.



--6.49
updateBase :: BarCode -> (Name, Price) -> (SDatabase)
updateBase code (nome, valor) = [(code, nome, valor)]
