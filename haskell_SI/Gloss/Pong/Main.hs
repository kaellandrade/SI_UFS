import Graphics.Gloss
import Graphics.Gloss.Data.ViewPort
import Graphics.Gloss.Interface.IO.Interact


width, height, offset :: Int
width = 300
height = 300
offset = 100
fps = 60

playerSpeed = 4.0 -- Velocidade das raquetes

velocidadePorBatidas = 10 -- A cada n batidas aa velocidade será aumentada.

ballRadius = 10
paddleWidth = 5 -- Largura das raquetes
paddleLength = 30 -- Comprimento das raquetes.
wallWidth = 10

paddleYMax = 160 - paddleLength - wallWidth -- Verifica o limite das rquetes.

initialPosition = (0.0, 0.0)
initialDirection = (1.5, 1.0)
initialSpeed = 60.0
speedIncrement = 0.25 -- Valor que será incrementado a cada batida nas raquetes

window :: Display
window = InWindow "Pong" (width, height) (offset, offset)

background :: Color
background = black

main :: IO ()
main = play window background fps initialState draw handleKeys update

update :: Float -> PongGame -> PongGame
update seconds game = ((moveBall seconds) . reinicibatidas . wallBounce . paddleBounce . movePlayers . reiniciamesa) game

type Radius = Float
type Position = (Float, Float)
data PlayerMovement = PlayerUp | PlayerStill | PlayerDown deriving Show   -- Estados dos movimentos

data PongGame = Game
  { ballLoc :: Position
  , ballDirection :: (Float, Float)
  , ballSpeed :: Float
  , player1 :: Position
  , player1Movement :: PlayerMovement
  , player2 :: Position
  , player2Movement :: PlayerMovement
  , batidas :: Float
  } deriving Show

initialState :: PongGame
initialState = Game initialPosition initialDirection initialSpeed
  (-144.0, 20.0) PlayerStill
  (144.0, 100.0) PlayerStill
  0.0

-- Cria meus componentes do jogo, bola , parede e raquetes
draw :: PongGame -> Picture
draw game = pictures [ball, walls, mkPaddle black (player1 game), mkPaddle black (player2 game)]
  where
    --  A bola.
    ball = uncurry translate (ballLoc game) $ color ballColor $ circleSolid ballRadius
    ballColor = dark yellow

    --  As paredes
    wall :: Float -> Picture
    wall offset =
      translate 0 offset $
        color wallColor $
          rectangleSolid 273 wallWidth

    wallColor = greyN 0.5
    walls = pictures [wall 150, wall (-150)]

    --  Cria as raquetes.
    mkPaddle :: Color -> Position -> Picture
    mkPaddle col pos = pictures
      [ translate x y $ color paddleColor $ rectangleSolid (2.3 * paddleWidth) (2.3 * paddleLength)
        ]
      where (x, y) = pos
    paddleColor = light (dark orange)

moveBall :: Float -> PongGame -> PongGame
moveBall seconds game = game { ballLoc = (x', y') }
  where
    (x, y) = ballLoc game
    (vx, vy) = ballDirection game
    speed = ballSpeed game
    x' = x + vx * seconds * speed
    y' = y + vy * seconds * speed


--verifica se a bola colidiu com a parede
wallCollision :: Position -> Bool
wallCollision (_, y) = topCollision || bottomCollision
  where
    topCollision = y - ballRadius <= -fromIntegral width / 2
    bottomCollision = y + ballRadius >= fromIntegral width / 2

-- altera a direção da bola ao colidir com a parede
wallBounce :: PongGame -> PongGame
wallBounce game = game { ballDirection = (vx, vy') }
  where
    (vx, vy) = ballDirection game
    vy' = if wallCollision (ballLoc game) then -vy else vy

--Verifica se houve colisão com a raquete esquerda
leftPaddleCollision :: Position -> Position -> Bool
leftPaddleCollision ballPosition player = xCollision && yCollision
  where
    (x, y) = ballPosition
    (px, py) = player
    xCollision = (x - ballRadius <= px + paddleWidth) && (x - ballRadius >= px - paddleWidth) -- Verifica se houve colisão no X
    yCollision = (y >= py - paddleLength) && (y <= py + paddleLength) -- Verifica se houve colisão no X

--Verifica se houve colisão com a raquete direita
rightPaddleCollision :: Position -> Position -> Bool
rightPaddleCollision ballPosition player = xCollision && yCollision
  where
    (x, y) = ballPosition
    (px, py) = player
    xCollision = (x + ballRadius >= px - paddleWidth) && (x + ballRadius <= px + paddleWidth)
    yCollision = (y >= py - paddleLength) && (y <= py + paddleLength)


-- Muda a direção da bola e velocidade caso haja uma colisão com as raquetes.
paddleBounce :: PongGame -> PongGame
paddleBounce game = game { ballDirection = (vx', vy), ballSpeed = speed', batidas = batidas' }
  where
    (vx, vy) = ballDirection game
    leftCollision = leftPaddleCollision (ballLoc game) (player1 game)
    rightCollision = rightPaddleCollision (ballLoc game) (player2 game)
    vx' = if leftCollision then abs vx
          else 
            if rightCollision then - (abs vx)
          else vx
--Incrementa batidas.
    batidas' = if leftCollision || rightCollision
      then (batidas game) + 1.0 -- Incrementa quando há uma colisão.
      else (batidas game)
  
    speed' = if (batidas game) >=  velocidadePorBatidas -- Verifica se as é mior ou igual a n.
              then 
                (ballSpeed game) + speedIncrement -- Caso seja maior será aumentada a velocidade da bola.
              else 
                (ballSpeed game)




-- Realiza o movimento das raquetes.
movePlayer :: Position -> PlayerMovement -> Position
movePlayer (px, py) PlayerStill = (px, py)
movePlayer (px, py) PlayerUp = (px, py + playerSpeed)
movePlayer (px, py) PlayerDown = (px, py - playerSpeed)

-- Revebe uma posição e devolve outra posoção com o valor limite da raquete
-- paddleYMax é o valor máximo permitido.
travaraquete :: Position -> Position
travaraquete (px, py) = 
  if ((snd new) > paddleYMax) 
    then (px, paddleYMax) --Trava a parte de cima se o Y excerder o paddleYMax
    else
      if ((snd new) < -paddleYMax) 
        then (px, -paddleYMax) --Trava a parte de baixo se o Y excerder o paddleYMax
        else (px, py)
  where
    new = (px, py)
    

-- Chama a função movePlayer de acordo com estado dos movimentos.
movePlayers :: PongGame -> PongGame
movePlayers game =  game { player1 = travaraquete $  movePlayer (player1 game) (player1Movement game)
,player2 = travaraquete $ movePlayer (player2 game) (player2Movement game)}
 

-- Verifica se a bola está fora de jogo
foradamesa :: Position -> Bool
foradamesa (bx, _) | bx >= 150 = True
foradamesa (bx, _) | bx <= (-150) = True
foradamesa _ = False


-- Reinicia a posição inicial da bola, caso passe do limite.
reiniciamesa :: PongGame -> PongGame
reiniciamesa game = 
  if foradamesa (ballLoc game)
    then
      game { ballLoc = initialPosition, ballSpeed = initialSpeed, batidas = 0 }               
    else
      game

-- Reinicia um número de batidas quando o contador chegar a n batidas.
reinicibatidas :: PongGame -> PongGame
reinicibatidas game = 
  if  (batidas game) > velocidadePorBatidas
    then
      game {batidas = 0 }               
    else
      game

handleKeys :: Event -> PongGame -> PongGame
handleKeys (EventKey (Char 'r') Down _ _) game = game { ballLoc = initialPosition } -- reinicia o jogo.

handleKeys (EventKey (Char 'w') Down _ _) game = game { player1Movement = PlayerUp }
handleKeys (EventKey (Char 'w') Up _ _) game = game { player1Movement = PlayerStill }
handleKeys (EventKey (Char 's') Down _ _) game = game { player1Movement = PlayerDown }
handleKeys (EventKey (Char 's') Up _ _) game = game { player1Movement = PlayerStill }

handleKeys (EventKey (Char 'o') Down _ _) game = game { player2Movement = PlayerUp }
handleKeys (EventKey (Char 'o') Up _ _) game = game { player2Movement = PlayerStill }
handleKeys (EventKey (Char 'l') Down _ _) game = game { player2Movement = PlayerDown }
handleKeys (EventKey (Char 'l') Up _ _) game = game { player2Movement = PlayerStill }

handleKeys _ game = game