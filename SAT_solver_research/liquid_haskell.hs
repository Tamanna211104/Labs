import Data.List
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

solveSAT :: Formula -> Maybe Model
solveSAT formula = getModel formula []

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
        Just (l, updatedFormula) ->
          case getModel (propagate l updatedFormula) (l : model) of
            Just resultModel -> Just resultModel
            Nothing -> getModel (propagate (-l) updatedFormula) (-l : model)
        Nothing -> Nothing

unitPropagate :: Formula -> Maybe (Literal, Formula)
unitPropagate formula =


pureLiteralAssign :: Formula -> Maybe (Literal, Formula)
pureLiteralAssign formula =
  case nub $ concat formula of
    [] -> Nothing
    (literal:_) -> Just (literal, removeLiteralInstances literal formula)

chooseLiteral :: Formula -> Maybe (Literal, Formula)
chooseLiteral formula =
  case concat formula of
    [] -> Nothing
    (literal:_) -> Just (literal, formula)

propagate :: Literal -> Formula -> Formula
propagate literal formula = removeLiteralInstances (-literal) formula

removeLiteral :: Literal -> Formula -> Formula
removeLiteral literal formula = filter (not . elem literal) formula

removeLiteralInstances :: Literal -> Formula -> Formula
removeLiteralInstances literal formula = map (filter (/= literal)) formula
