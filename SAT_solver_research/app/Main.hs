{-@ LIQUID "--no-termination" @-}
module Main where

import Data.List
import qualified Data.Set as S
import System.IO

--Types to be used :
--type Literal = Int
--type Clause = [Literal]
--type Formula = [Clause]
--type Model = [Int]
--data Result = SAT Modell, UNSAT
--type Clause ; vec (GADTS)  list (LH)
--type formula; vac (GADTS) list (LH)
--data lit = lit = polarity = nat (number greater than or equal to 1)
--data Polarity = Pos / Neg
--Nat type = (LH) int with refinement; Peano numbers (GADTS)
--type Clause = [lits]

type Literal = Int
type Clause = [Literal]
type Formula = [Clause]
type Model = [Int]

{-@ measure litsC @-}
-- to get set of all literals in a clause

litsC :: Clause -> S.Set Literal
litsC [] = S.empty
litsC (l : cs) = litsC cs `S.union` S.singleton l
-- S.union (litsC cs) (singleton l)


{-@ measure litsF @-}
-- define a litsF which takes a formula and gives a set of literals
litsF :: Formula -> S.Set Literal
litsF [] = S.empty
litsF (c : ls) = litsF ls `S.union` litsC c


main :: IO ()
main = return ()

{-@ solveSAT :: f : {f: Formula | True } -> Maybe Model @-}
solveSAT :: Formula -> Maybe Model
solveSAT formula = getModel formula []

{-@ getModel :: f : {f: Formula | True } -> Model -> Maybe Model @-}
getModel :: Formula -> Model -> Maybe Model
getModel [] model = Just model
getModel formula model
  | any null formula = Nothing
  | any (null . nub) formula = Nothing
  | otherwise = case unitPropagate formula of
    Just (l, updatedFormula) -> getModel updatedFormula (l : model)
    Nothing -> case pureLiteralAssign formula of
      Just (l, updatedFormula) -> getModel updatedFormula (l : model)
      Nothing -> case chooseLiteral formula of
        Just l ->
          case getModel (propagate l formula) (l : model) of
            Just resultModel -> Just resultModel
            Nothing -> getModel (propagate (-l) formula) (-l : model)
        Nothing -> Nothing

{-@ unitPropagate :: f : {f: Formula | True } -> Maybe (Literal, Formula) @-}
unitPropagate :: Formula -> Maybe (Literal, Formula)
unitPropagate formula =
  case filter (\clause -> length clause == 1) formula of
    ([unitLit]:_) -> Just (unitLit, removeLiteral unitLit formula)
    _ -> Nothing

{-@ pureLiteralAssign :: f : {f: Formula | True } -> Maybe (Literal, Formula)@-}
pureLiteralAssign :: Formula -> Maybe (Literal, Formula)
pureLiteralAssign formula =
  case nub $ concat formula of
    [] -> Nothing
    (literal:_) -> Just (literal, removeLiteralInstances literal formula)

{-@ chooseLiteral :: f : {f: Formula | True } -> Maybe Literal @-}
chooseLiteral :: Formula -> Maybe Literal
chooseLiteral formula =
  case concat formula of
    [] -> Nothing
    (literal:_) -> Just literal
  -- choose Literal :: f : Formula -> Maybe {l: literal | l <- litsF}
  -- specifies something about the literal that is True for , ex:
  -- have to return a maybe to consider possiblity of empty list
  -- to add precondition :
  -- choose Literal | :: f : {f: Formula | size (litsF f)>0} -> {l : Literal | l <- litsF f}
  -- add set \= 0

-- assign meaning full refinement types to functions
-- removeliteralinstances
{-@ chooseLiteral' :: f : {f: Formula | litsF f /= S.empty } -> {l : Literal | S.member l (litsF f)} @-}
chooseLiteral' :: Formula -> Literal
chooseLiteral' ([] : cs) = chooseLiteral' cs
chooseLiteral' ((l : _) : cs) = l
chooseLiteral' _ = die "chooseLiteral': empty list"

{-@ propagate :: l : {l: Literal | True } -> Formula -> Formula @-}
propagate :: Literal -> Formula -> Formula
propagate literal = removeLiteralInstances (- literal)

{-@ removeLiteral :: l : {l: Literal | True } -> Formula -> Formula @-}
removeLiteral :: Literal -> Formula -> Formula
removeLiteral literal = filter (notElem literal)

-- write refinement types
{-@ removeLiteralInstances :: l : {l: Literal | True } -> Formula -> {f: Formula | l /= S.} @-}
removeLiteralInstances :: Literal -> Formula -> Formula
removeLiteralInstances literal = map (filter (/= literal))

{-@ die :: { _:String | False } -> a @-}
die :: String -> a
die = error
