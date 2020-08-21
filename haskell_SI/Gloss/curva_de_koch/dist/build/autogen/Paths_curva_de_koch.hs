{-# LANGUAGE CPP #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -fno-warn-implicit-prelude #-}
module Paths_curva_de_koch (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/kaell_andrade/Git/quarta_lista/curva_de_koch/.cabal-sandbox/bin"
libdir     = "/home/kaell_andrade/Git/quarta_lista/curva_de_koch/.cabal-sandbox/lib/x86_64-linux-ghc-8.0.2/curva-de-koch-0.1.0.0"
dynlibdir  = "/home/kaell_andrade/Git/quarta_lista/curva_de_koch/.cabal-sandbox/lib/x86_64-linux-ghc-8.0.2"
datadir    = "/home/kaell_andrade/Git/quarta_lista/curva_de_koch/.cabal-sandbox/share/x86_64-linux-ghc-8.0.2/curva-de-koch-0.1.0.0"
libexecdir = "/home/kaell_andrade/Git/quarta_lista/curva_de_koch/.cabal-sandbox/libexec"
sysconfdir = "/home/kaell_andrade/Git/quarta_lista/curva_de_koch/.cabal-sandbox/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "curva_de_koch_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "curva_de_koch_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "curva_de_koch_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "curva_de_koch_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "curva_de_koch_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "curva_de_koch_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
