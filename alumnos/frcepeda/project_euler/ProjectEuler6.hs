-- There isn't much to say, really.
main = print $ abs ((sum [1..100])^2 - sum (map (^2) [1..100]))
