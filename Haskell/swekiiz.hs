remDups :: (Eq a) => [a] -> [a] -> [a]
remDups [] _ = []
remDups (x : xs) l
  | (x `elem` l) = remDups xs l
  | otherwise = x : remDups xs (x : l)

removeDuplicates :: (Eq a) => [a] -> [a]
removeDuplicates list = remDups list []

refd :: String -> String
refd s =
  let repl 'f' = 'd'
      repl x = x
   in map repl s

main = putStrLn . refd . removeDuplicates $ "Coffee"