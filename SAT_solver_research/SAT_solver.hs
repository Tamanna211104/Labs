import Data.List
import System.IO

-- Type synonyms for representing literals and clauses
type Literal = Int
type Clause = [Literal]
type Formula = [Clause]

type Model = [Int]

-- Data type to represent the state of the SAT solver
data SATState = SAT | UNSAT deriving (Show, Eq)

-- Function to check if a clause is satisfied by a given variable assignment
isClauseSatisfied :: Clause -> [Literal] -> Bool
isClauseSatisfied [] _ = False
isClauseSatisfied (l:ls) assignment
  | l `elem` assignment = True
  | (-l) `elem` assignment = isClauseSatisfied ls assignment
  | otherwise = isClauseSatisfied ls assignment

-- Function to check if a formula is satisfied by a given variable assignment
isFormulaSatisfied :: Formula -> [Literal] -> Bool
isFormulaSatisfied [] _ = True
isFormulaSatisfied (c:cs) assignment
  | isClauseSatisfied c assignment = isFormulaSatisfied cs assignment
  | otherwise = False

-- Function to find the pure literals in a formula
findPureLiterals :: Formula -> [Literal]
findPureLiterals formula = nub [ l | c <- formula, l <- c, (-l) `notElem` literals ]
  where literals = nub $ concat formula

-- Function to simplify a formula by removing pure literals
simplifyFormula :: Formula -> Formula
simplifyFormula formula = [ c | c <- formula, not $ any (\l -> l `elem` pureLiterals) c ]
  where pureLiterals = findPureLiterals formula


-- Function to select the literal to branch on (first literal of the first clause)
selectLiteral :: Formula -> Literal
selectLiteral form = head $ head form

-- Function to perform unit propagation on a formula with a given literal assignment
unitPropagation :: Formula -> Literal -> Formula
unitPropagation form assignment =
  let form' = filter ( notElem assignment ) form
      form'' = map ( filter (\y -> y /= -assignment) ) form'
      in form''

  --let form' = [ c | c <- form, notElem assignment c ]
     -- form'' = [ [ y | y <- c, y /= -assignment] | c <- form']
      --in form''

-- Function to perform DPLL Algorithm
dpll :: Formula -> SATState
dpll = dpll' []

dpll' :: Model -> Formula -> SATState
dpll' _ [] = SAT

dpll' m form
      | any null form = UNSAT
      | Just [lit] <- find (\c -> case c of [_] -> True; _ -> False) form =
          dpll' (lit:m) (unitPropagation form lit)
      | otherwise = let lit = selectLiteral form
                        form' = unitPropagation form lit
                        form'' = unitPropagation form (-lit)
                    in case dpll' (lit:m) form' of
                          SAT -> SAT
                          UNSAT -> dpll' (-lit:m) form''
