main = do
    putStrLn "Olá, qual o seu nome ?"
    nome <- getLine
    putStrLn(nome++", programar Haskell será um grande bem para você")