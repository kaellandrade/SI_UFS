-- IO ()
helloWorld :: IO ()
helloWorld = putStrLn "Hello, World!"

--Ler duas linhas e mostra seus respectivos valores
le2Linhas2 :: IO()
le2Linhas2 = do
                linha1 <- getLine
                linha2 <- getLine
                putStrLn ("Duas linhas lidas: \n" ++ linha1 ++"\n"++ linha2)

-- Reverte a linha lida
reverseLine :: IO()
reverseLine = do
                linha <- getLine
                putStrLn (reverse linha)

--Lendo dois números e retornando sua soma
soma2Num :: IO()
soma2Num = do
            num1 <- getReadable :: IO Float
            num2 <- getReadable
            let soma = num1 + num2 -- definindo uma variável local.
            putStrLn ("A soma é: ")
            putStrLn . show $ (soma)

--getInt irá ler um número em string e irá retorna seu valor primitivo
getInt :: IO Int 
getInt = do
            ln <- getLine
            return (read ln :: Int)

-- getReadable está definido genericamente
getReadable :: Read a => IO a
getReadable = do
                lin <- getLine
                return (read lin)

--Programa que faz o echo infinitamente
echo :: IO ()
echo = do 
        linha <- getLine
        putStrLn linha
        echo

-- Echo até n
echoN :: Int -> IO ()
echoN 0 = return()
echoN n = do 
            linha <- getLine
            putStrLn linha
            echoN (n-1)

-- Echo até que a linha digitada sejá ""
echoAte :: IO()
echoAte = 
    do
        valor <- getLine
        if (valor /= "")
            then
                do
                    putStrLn valor
                    echoAte
            else
                return()

echoConta :: Int -> IO ()
echoConta n = do
                valor <- getLine
                if (valor /= "")
                    then
                        echoConta (n+1)
                    else
                        do
                            putStrLn $ show n ++ " linhas lidas"
                            return()

echoContaAte :: IO()
echoContaAte = echoConta 0



--------------------------------------Praticando----------------------------------------------
{-1
Escreva um programa com IO que leia uma linha de entrada
e verifique se  a linha lida é ou não uma palavra palíndroma.
-}
palindroma :: IO()
palindroma = 
    do 
        putStrLn("Escreva uma palavra para verificarmos se é palíndroma: ")
        linha <- getLine 
        if (linha == reverse linha) 
            then putStrLn ("É palindroma!") 
            else putStrLn ("Não é palíndroma!")

{-2
Escreva um programa que leia um inteiro (Int) n e um Float f
e que imprima o valor de f elevado à n. O programa deverá
pedir cada uma das entradas e escrever o resultado em uma mensagem aproprieada.
-}
elevanf :: IO ()
elevanf = do 
            putStrLn ("Escreva sua base: ")
            numF <- getReadable :: IO Float
            putStrLn("Escreva seu espoente")
            numN <- getReadable :: IO Int
            let resultado = (numF) ^ (numN) 
            putStrLn (show numN ++ "^" ++ show numF ++ " = " ++ show resultado)
        
{-3
Escreva um programa que leia vários números inteiros, todos
digitados numa mesma linha, e que imprima a soma de todos eles.
Dica: use a função words para quebrar uma string em "palavras"
-}
somaLinhaN :: IO ()
somaLinhaN = do 
                putStrLn("Escreva uma sequencia de números separados por espaços: ")
                linhanumerica <- getLine
                let listaStr = words linhanumerica -- Estou quebrando a string em palavras
                let listaInt = map (\x -> read x :: Int ) listaStr-- Estou realizando as conversões dos valores
                putStrLn ("Sua soma é : " ++ show (sum listaInt))


{-4
Defina a função putNtimes :: Integer -> String -> IO()
tal que o efeito de putntimes n str e escrever na tela o string
str, n vezes, um por linha.
-}

putNtimes :: Integer -> String -> IO ()
putNtimes 0 s = return ()
putNtimes n s = do
                    putStrLn s 
                    putNtimes (n-1) s 

{-5
Escreva um programa que leia primemiro um número, digamos n,
depois leia n números inteiros e então escreva a soma deles.
O programa deverá escrever mensagens pedindo dados e dizendo qual é o resultado
-}
somaAten :: IO ()
somaAten = do
            putStrLn "Quantos números deseja ler ?"
            valor <- getInt
            soma  <- soma valor 0 -- chama a função soma com o número de vezes de repstiçoes e com valor inicial = 0
            putStrLn "Sua soma é: "
            putStrLn (show soma)


soma :: Int -> Int -> IO Int
soma 0 a = return a -- Caso passe 0 para somaAten será retornado 'a' que por padrão iniciou com 0
soma n a = do
            m <- getInt -- m será os valores que serão capturados pelo usuário
            soma (n-1) (a+m) -- soma até será executado até n chegar a 0

{-6
Escreva uma função wc que lê linhas até que uma linha vazia ser digitada. 
O programa deverá escrever o número de linhas, número de palavras e números de caracteres que 
foram lidos.
-}
-- wc :: IO()
-- wc = do
--         valor <- getLine
--         linhas <- contaL 0
--         if (valor == "")
--             then
--                 return()
--             else
--                 do
--                     putStrLn valor
--                     echoAte

-- -- Conta Linhas palavras Caracters
-- contaL ::  Int -> Int -> IO Int
-- contaL 0 n = 

--1

produto :: Int -> Int -> IO ()
produto n acumulador =
                        if (n == 0)
                            then putStrLn $ show acumulador
                        else
                            do 
                                valor <- getInt
                                produto (n-1) (acumulador * valor)

                        
                        


auxiliar :: IO ()
auxiliar = 
    do  vezes <- getInt
        produto vezes 1  

bhaskara :: IO ()
bhaskara = 
    do
        a <- getReadable :: IO Float
        b <- getReadable :: IO Float
        c <- getReadable :: IO Float

        let delta = (b^2) - (4 * a * c)

        let x1 =  ((-b) + sqrt (delta)) / 2 * a
        let x2 =  ((-b) - sqrt (delta)) / 2 * a
        putStrLn ("X1 é : " ++ show(x1))
        putStrLn ("X2 é : " ++ show(x2))

--3
trans :: IO [Int] 
trans = 
    do 
        valores <- getLine
        let lista = map(\x-> read x :: Int) (words valores)
        return (lista)

