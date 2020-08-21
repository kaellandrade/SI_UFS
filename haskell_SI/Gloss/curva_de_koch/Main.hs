module Main(main) where

import Graphics.Gloss
import qualified Graphics.Gloss.Data.Point.Arithmetic as V
import Graphics.Gloss.Data.Vector

window :: Display
window = InWindow "Curva de Koch" (500, 500) (450, 100)

background :: Color
background = white

curva_koch:: Int -> Path -> Picture
curva_koch 0 ts = line ts
curva_koch n [p,q] = pictures[curva_koch (n-1) [p, p1]
                        , curva_koch (n-1) [p1, p2]
                        , curva_koch (n-1) [p2, p3]
                        , curva_koch (n-1) [p3, q] ]
                        where
                            v = mulSV (1/3) (q V.- p)
                            p1 = p V.+ v
                            p2 = p1 V.+ rotateV (pi/3) v
                            p3 = p2 V.+ rotateV (-pi/3) v

main :: IO ()
main = display window background (curva_koch 5 [(-200, 0),(200, 0)])
