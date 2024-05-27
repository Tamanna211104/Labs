module Main where

import Data.List
import System.IO

-- imp resource is the online textbook called "Learn you haskell for a greater good"

{-
to install and run on terminal :
https://www.haskell.org/platform/mac.html on mac
https://www.haskell.org/platform/linux.html on linux
https://www.haskell.org/platform/windows.html on windows
type ghci
type :q to quit ghci
to load a file type :l file_name
to run file :r
to run specific function Func_name input
to view type signature (definition) of any function/operator/variable use :t
-}




-- functional programming language
--has no for while loops or technically variables but has constants
--lazy, immutable, strict compiler
{-
another method to comment in haskell : the multiline method
-}
-- DATA TYPES
{-
haskell data-types : haskell uses type inference
which means it decides on the data type based
off the value one storess inside of it;
user can also define what type of data
haskell is statically typed, once you define it you cant switch it
-}

-- Int -2^63 2^63
maxInt = maxBound :: Int
minInt = minBound :: Int
-- the above shows a type signature i.e. it tells what type of variable is maxInt
--  maxBound aka the maximum value function which is given by the datatype 'Int', the datatype of a function is defined by "::"
-- maxInt will store the 'Int' value given by maxBound

{-
second type of integer which is simply defined as :
 Integer
it is used more commonly and is a unbounded whole number,
it is as big as the computer memory can hold
-}

{-
Floats which are single precision floatig point numbers
but mostly commonly used for anything with decimals is Double
it will have precision up to 11 points
example :
-}
bigFloat = 3.9999999999 + 0.000000000000000000000005
--output will be 3.99999999

-- Bool value of either True or False

-- Char which are going to be single Unicode denoted by '

-- Tuple, can store lists made up of many different data types, for the most part will only contain two values

-- you can declare a permanent value of a variable
-- for example

always5 :: Int
always5 = 5


-- MATH FUNCTIONS

sumOfNums = sum [1..1000]
addEx = 5 + 4
subEx = 5 - 4
multEx = 5 * 4
divEx = 5 / 4

-- to get the remainder of a division
modEx = mod 5 4
-- called a prefix operator, u could also add backticks to mod
-- modEx2 = 5 `mod` 4
-- if you want to do addition with a negative number you have to put parentheis around said negative number
negNumEx = 5 + (-4)
-- Typescript of negNumEx = (sqrt :: Floating a -> a -> a)
-- plans to work with floating point numbers, it will then recieve a value and then pop out a value
-- example :
num9 = 9 :: Int
-- To work with floats we have to convert integer to float
-- round function converts float to int; output will be 3.0
sqrtOf9 = sqrt (fromIntegral num9)
-- other built in math functions
piVal = pi
ePow9 = exp 9
logOf9 = log 9
squared9 = 9 ** 2
truncateVal = truncate 9.999
-- truncate rounds down/ removes decimal points completely; output = 9
roundVal = round 9.999
-- rounds up; output = 10
ceilingVal = ceiling 9.999
--rounds up
floorVal = floor 9.999
-- rounds up

-- Also sin, cos, tan, asin, atan, acos, asin
-- tanh, cosh, asinh, acosh, atanh

-- LOGICAL OPERATORS

trueAndFalse = False
trueOrFalse = True
notTrue = False

-- nums = doubles, floats, integers, ints
{-
to use addition operator in terminal
:t (+)
(+) :: Num a -> a -> a -> a
u recieve two parameters and it  returns and outside value
example 2:
:t truncate
truncate :: (RealFrac a, Integral b) -> a -> b
-}

-- LISTS
{-
Lists in haskell are very important
they are singly linked and user can only add to the front of a list
-}
-- to add values to the front of the list
morePrime2 = 2 : morePrime2
primeNumbers = [3, 5, 7, 11] -- original list
-- to add elements to the list
morePrime = primeNumbers ++ [13, 17, 19, 23, 29]
-- output = [3, 5, 7, 11, 13, 17, 19 23, 29]

-- u can use a cons operator to construct a list
-- put colons in between list and then empty box brackets
favNums = [2, 7, 21, 66]
-- output = [2,7,21,66]

-- to put lists inside of lists
multList = [[3, 5, 7], [11, 13, 17]]
-- output = [3, 5, 7, 11, 13, 17]

-- to figure out length of a list
lenPrime = length morePrime2

-- to reverse the list
revPrime = reverse morePrime2

-- to check if list is empty
isListEmpty = null morePrime2

-- to comand and get specific index values
-- if we want to get the second prime inside of the list :
secondPrime = morePrime2 !! 1
-- output = 3

-- to get first and last values
firstPrime = head morePrime2
lastPrime = last morePrime2

-- to get everthing except the 'head' i.e. the first value
tailPrime = tail [1, 2, 3, 4, 5]

-- we can also get everything except the last value
primeInit = init morePrime2

-- u can also select getting any number of the first few values
-- for example to get the first three values :
first3Primes = take 3 morePrime2
-- output = [2, 3, 5]

-- we can also return values after removing specified number of values
removedPrimes = drop 3 morePrime2
-- will output everything except the three removed values
-- output = [7, 11, 13, 17, 19, 23, 29]

-- to check if a value is in a list
is7InList = 7 `elem` morePrime2

-- to get the maximum or minimum value
maxPrime = maximum morePrime2
minPrime = minimum morePrime2

newList = [2, 3, 5]
-- to find product of list
prodPrimes = product newList
--output = 30

-- to generate a list
zeroToten = [0..10]

-- to generate list with specifications such as even numbers
evenList = [2, 4..20]

-- to generate character list
letterList = ['A','C'..'Z']
--will output list of alternate letters
-- output = ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'Q', 'S', 'U', 'W', 'Y']

-- one can also generate an infinite list with haskell
-- However since haskell works by the methods of lazy programming it will only calculate the infinite list up to whatever the requirement is
infinPow10 = [10, 20..]
-- this list is defined as infinite but wont be created until necessary
-- it will created based on a specification like the user needing a specific item in the list

-- you can also ask it to repeat a value a defined number of times
many2s = replicate 10 2

-- u can also use replicate to repeat a valye a specific number of times
many3s = replicate 10 3

--cycle will repeat a value in a list indefinitely
cycleList = take 10 (cycle [1, 2, 3, 4, 5])
-- output = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

-- the user can also perform multiple different operations on a list
-- to multiply all elements by 2

listTimes2 = [x * 2 | x <- [1..10]]
-- u can also filter the list as per required conditions
listTimes3 = [x * 3 | x <- [1..10], x * 3 <= 50]

divisBy9N13 = [x | x <- [1..500], x `mod` 13 == 0, x `mod` 9 == 0]

-- we can also make sorted list to organise a given list i.e., put them in numerical order
sortedList = sort [9, 1, 8, 3, 4, 7, 6]

-- to combine lists
sumOfLists = zipWith (+) [1, 2, 3, 4, 5] [6, 7, 8, 9, 10]
-- we can use filter to return a list of items that match a certain condition
listBiggerThen5 =  filter (>5) morePrime

-- to use a sort of while loop use takeWhile
evensUpTo20 = takeWhile (<= 20) [2,4..]
-- the example above also shows how haskell is lazy as it didnt give any further values even though the list [2,4..] is an infinite list

-- Foldl applies an operation on each item of a list from left to right i.e. 2 * 3 * 4 * 5
multOfList = product [2, 3, 4, 5]
-- output = 120
-- u can also use foldr if u want the operation to be applies in the opposite direction

-- LIST COMPREHENSION
{-
To perform certain operations on a list
-}
pow3List = [3^n | n <- [1..10]]

-- example: generating a multiplication table by multiplying different values in different lists
multTable = [[x * y | y <- [1..10]] | x <- [1..10]]

-- TUPLES
{-
stores a list of multiple different data types
lists have to have the same data types; that isnt the case for tuples
-}

-- to create a tuple
randTuple = (1, "Random Tuple")

-- tuple players are very useful in haskell; example by creating a tuple pair containing bob smith's info:
bobSmith = ("Bob Smith", 52)
-- to get bobs name or first value in a tuple
bobsName = fst bobSmith
-- to get bobs age or second value in a tuple
bobsAge = snd bobSmith

-- we can use zip to combine two different lists into tuple pairs for us
names = ["bob", "mary", "tom"]
addresses = ["123 Main", "234 North", "567 South"]

namesNAddresses = zip names addresses

-- FUNCTIONS
{-
Calculations can be done in the terminal i.e. in ghc as well
example;
ghci> let num7 = 7
ghci> let getTriple x = x * 3
ghci> getTriple num7
21

-- if we compile our program we will be able to run it if we define everything in main
-}

main = do
    putStrLn "What is your name"
    name <- getLine -- enter name in terminal and store that value to getLine so that it take information from the console
    putStrLn ("Hello " ++ name)

-- to create a function called addMe
-- define the type decleration for your function
-- type decleration/signature example
-- :t sqrt
-- sqrt :: Floating a => a -> a
addMe :: Int -> Int -> Int -- it will recieve an integer and then another integer and then it will return an integer
{-
the function name will be the actual creation of the function, it will be whatever you name your fuction and its going to be any parameters that are passed inside of it
then an equal sign after which you will have all of your operations and then a return value
-}
-- funcName param1 param2 = operations (returned value)
addMe x y = x + y

{-
x = param1
y = param2
operations and returned value = x + y
the data type of our input and output values is an integer based on the formula
functions can never start with an uppercase letter
any functions that dont recieve parameters are simply going to be called a definition or a name
-}

-- it is also possible to have haskell figure out the type decleration for you and directly write the function
sumMe x y = x + y
-- since we didnt specify via type formula we can now add with floats as well

-- to add Tuples :
addTuple :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuple (x, y) (x1, y1) = (x + x1, y + y1)

-- we can also use haskell to perform different actions based on what values we recieve as input
whatAge :: Int -> String
whatAge 16 = "You can drive"
whatAge 18 = "You can vote"
whatAge 21 = "You're an adult"
whatAge x = "Nothing Important"
-- u can also just type _ instead of x

-- RECURSION
factorial :: Int -> Int

factorial 0 = 1
factorial n = n * factorial (n-1)

-- 3 * factorial(2) = 3 * 2 = 6
-- 2 * factorial(1) = 2 * 1 = 2
-- 1 * factorial(0) : 1

-- we can also calculate factorial using product :
prodFact n = product [1..n]

-- we will also be using something called gaurds to provide different actions based off of different conditions
-- guards are denoted by |
-- to demonstrate the concept of gaurds :
isOdd :: Int -> Bool
isOdd n
    | n `mod` 2 == 0 = False
    | otherwise = True
-- the program states if a value is even return False
-- this is because function checks if value is odd
-- gaurds basically allow to catch everything its a defult so if a number is odd it will return True


-- This example can also be written as
isEven n = n `mod` 2 == 0

-- gaurds example 2 :
whatGrade :: Int -> String
whatGrade age
    | (age >= 5) && (age <= 6) = "Kindergarden"
    | (age > 6) && (age <= 10) = "Elementary"
    | (age > 10) && (age <= 14) = "Middle School"
    | (age > 14) && (age <= 18) = "High School"
    | otherwise = "Go to College"

-- Where clause using "it" with gaurds
batAvgRating :: Double -> Double -> String
batAvgRating hits atBats
    | avg <= 0.200 = "Terrible Batting Average"
    | avg <= 0.250 = "Average Player"
    | avg <= 0.280 = "Your doing pretty good"
    | otherwise = "You are a superstar"
-- this is where the Where clause comes in so that its not necessary to calculate individually at every guard
    where avg = hits / atBats

-- PATTERN MATCHING
-- some methods to access list items
getListItems :: [Int] -> String
getListItems [] = "Your list is empty"
getListItems (x:[]) = "Your list starts with" ++ show x
-- show turns anything into a string so it will be one way to access this value
getListItems (x:y:[]) = "Your List contains" ++ show x ++ "and" ++ show y
getListItems (x:xs) = "The 1st item is " ++ show x ++ " and the rest are " ++ show xs

-- We can also access list values using as pattern
getFirstItem :: String -> String
getFirstItem [] = "Empty String"
getFirstItem all@(x:xs) = "The first letter in " ++ all ++ " is " ++ [x]

-- lets take a look at higher order functions
times4 :: Int -> Int
times4 x = x * 4
listTimes4 = map times4 [1,2,3,4,5]

-- MAP
-- to see how map works we can make map
multBy4 :: [Int] -> [Int]
multBy4 [] = []
multBy4 (x:xs) = times4 x : multBy4 xs
-- times4 for first item of the list while multBy4 for the rest of te items
-- this is cuz during pattern matching i.e. (x:xs) we seperate the first item of the list from the rest
-- [1,2,3,4] : x = 1 | xs = [2,3,4]
-- [2,3,4] : x = 2 | xs = [3,4]
-- this will continue until list is empty
-- output = [4,8,12,16]

-- another recursion example to look at :
areStringsEq :: [Char] -> [Char] -> Bool
areStringsEq [] [] = True
areStringsEq (x:xs) (y:ys) = x == y && areStringsEq xs ys
-- we had to call areStringsEq the second time since  there could be more than one item in the list
areStringsEq _ _ = False
-- to demonstrate example run areStringsEq "Hello" "Hello"
-- output = True
-- areStringsEq "Hello" "Hello You"
-- output = False


-- TO PASS A FUNCTION INTO A FUNCTION
doMult :: (Int -> Int) -> Int
-- we expect a function to be passed inside of (Int -> Int)
-- once that function is passed into the new function we can return an Int
doMult func = func 3
-- the function we will pass is times4 and it will take 3 as input
num3Times4 = doMult times4
-- num3Times4 will store the value of the function doMult
-- this was to recieve a function

-- TO RETURN A FUNCTION
getAddFunc :: Int -> (Int -> Int)
getAddFunc x y = x + y
adds3 = getAddFunc 3
-- this will take the first Int as 3 return the function and store it in adds3
fourPlus3 = adds3 4
-- if u run fourPlus3
    -- output = 7

-- we can use this with map as well
threePlusList = map adds3 [1,2,3,4,5]

-- LAMBDA
{-
it is a way to create functions that dont have  a name
'\' is typed before x since lamda doesnt have  a name
-}
dbl1To10 = map (\x -> x * 2) [1..10]

-- CONDITIONALS
{-
comparison operators :
<> <= >= == /=
logical operators :
&& || not
-}
-- IF STATEMENTS
-- can be used in haskell even tho not something commonly done
doubleEvenNumber y =
    if (y `mod` 2 /= 0)
        then y
        else y * 2
-- else is necessary due to haskell's strict compiler

-- CASE STATEMENTS
-- will take input value 'n' in this case and pass it through given conditions using "case"
getClass :: Int -> String
getClass n = case n of
    5 -> "Go to Kindergarten"
    6 -> "Go to elementary school"
    _ -> "Go away"

-- MODULES
{-
shown in the beginning of this file
Data.Set, Data.List
System.IO
modules contain a bunch of functions which you use for your programs
to load a module simply import module
-}
{- an example to show how to create your own module and load it

module SampFunctions (getClass, doubleEvenNumbers) where

import SampFunctions

-}

-- ENUMERATIONS
{-
Enumeration types are basically going to be used when you want to define a list of possible types
to create a enumerated type, type in 'data'
the format shown below can also be done in one line 'Player | Catcher..'
the given format is given preference for neatness
-}
data BaseballPlayer = Pitcher
                      | Catcher
                      | Infielder
                      | Outfield
                    deriving Show
-- 'deriving Show' is for the function to actually print out like String even if data type is not String
-- 'Show' will be explained in the Type Classes section
barryBonds :: BaseballPlayer -> Bool
barryBonds Outfield = True

barryInOF = print(barryBonds Outfield)
-- output will be : True

-- CUSTOM TYPES
-- u can store multiple values sort of like a struct to create a custom data type
data Customer = Customer String String Double
-- this is to put all the types we want inside of it
    deriving Show

jackReacher :: Customer
-- then we put in the information of customer "Name" "Address" balance.0
jackReacher = Customer "Jack Reacher" "141 9th St" 1520.50

-- we can then define functions to get specific values from this custom type
getBalance :: Customer -> Double
getBalance (Customer _ _ b) = b

-- rock paper scisscor example:
data RPS = Rock | Paper | Siccors
-- input all different types, this is just an enumerate type we used to create a custum type
shoot :: RPS -> RPS -> String
-- now we define all of the possible answers
shoot Paper Rock = "Paper Beats Rock"
shoot Rock Scissors = "Rock Beats Scissors"
shoot Scissors Paper = "Scissors Beat Paper"
shoot Paper Scissors = "Paper Loses to Scissors"
shoot Rock Paper = "Rock Loses to Paper"
shoot _ _ = "Error"

-- POLYMORPHIC TYPE
{-
we can define two versions of a type
for example to create shape type that will work for rectangles and circles
circle will have 3 floats to represent x y coordinates and the last one will be the radius
rectangle will have 4 floats to represent upper left hand coordinates x y and bottom right hand coordinates x y
-}
data Shape = Circle Float Float Float | Rectangle Float Float Float Float
    deriving Show

area :: Shape -> Float
area (Circle _ _ r) = pi * r ^ 2
area (Rectangle x y x1 y1) = (abs $ x1-x) * (abs $ y2-y)
-- abs is to get the absolute value of the data type passed in
    -- to get rid of excessive perenthesis use $

-- OPERATORS
{-
dot operator - it will allow us to chain functions to pass output on the right to the input on the left
-}
-- the way we have learnt so far :
sumValue = putStrLn (show (1+2))
-- using dot operator and $ it can be written as :
sumValue2 = putStrLn . show $ 1 + 2
-- some more examples using custom types
areaOfCircle = area (Circle 50 60 20)
areaOfRect = area $ Rectangle 10 10 100 100

-- TYPECLASSES
{-
Num Eq Or Show
type classes correspond to sets of types which have certain operations defined for them
for example:
(+) works with parameters that use Num
(+) :: Num a => a -> a -> a
for any type 'a' whether it is a integer, double, float as long as it is an instance of Num it will work with (+)
Basically as long as it is an instance of Num we can use (+)
-}

-- to create a custom data type
data Employee = {name    :: String
                position :: String
                idNum    ::  Int
}
 deriving (Eq, Show)
-- deriving (Eq,Show) will not only show them but will also check for equality between them
-- now lets create two employees
laraCroft = Employee {name = "Lara Croft", position = "Archaeologist", idNum = 1000}
selinaKyle = Employee {name = "Selina Kyle", position = "lowly Assistant", idNum = 1001}

isLaraSelina = laraCroft == selinaKyle
-- output = false
-- to print out information
laraCroftData = show laraCroft

-- TYPE INSTANCE
-- lets create another data type
data ShirtSize = S | M | L
-- uppercase letters can be used for data types but not for functions
instance Eq ShirtSize where
    S == S = True
    M == M = True
    L == L = True
    _ == _ = False

-- we can also define how show is gonna work
instance Show ShirtSize where
    show S = "Small"
    show M = "Medium"
    show L = "Large"

smallAvail = S `elem` [S,M,L]
-- this will check if something is in a list for us
theSize = show S

-- CUSTOM TYPE CLASSES
-- to define a custom type class is gonna check for equality
class MyEq a where
    areEqual :: a -> a -> Bool
data ShirtSize = S | M | L
instance MyEq ShirtSize where
    areEqual S S = True
    areEqual M M = True
    areEqual L L = True
    areEqual _ _ = False
newSize = areEqual M M
-- output will be true

-- FILE I/O
-- to start lets create a function that allows us to chain a number of things together
sayHello = do
    putStrLn "What's Your name"
    name <- getLine
    putStrLn $ "Hello" ++ name

-- now to learn file I/O
-- 1. To write to a file
writeToFile = do
    -- we need to open the file we want to work with; to do that use openFile
    -- use WriteMode so that you write only to that file
    theFile <- openFile "test.txt" WriteMode
    -- to put text use hPutStrLn
    hPutStrLn theFile ("Random line of text")
    -- close file
    hClose theFile

-- 2. To read from a file
readFromFile = do
    theFile2 <- openFile "test.txt" ReadMode
    -- to get contents of the file
    contents <- hGetContents theFile2
    putStr contents
    hClose theFile2

-- when you writeToFile it will write in the statement you input
-- when you readFromFile output = "Random line of text"


-- FIBONACCI SEQUENCE
-- an explanation video for the Fibonacci Sequence and Golden Ratio : https://www.youtube.com/watch?v=mVO2dcuR7P0
-- Fibonacci sequence can be simply explained as the a series of values such that the two previous values will add together to form the next value
-- 1, 1, 2, 3, 5, 8, 13 .....


-- create a list
-- follow fibonacci numbers inside of it
fib - 1 : 1 : [a + b | (a,b) <- zip fib (tail fib)]
-- this statement creates a list that is going to be made up of the Fibonacci Sequence
-- : is a cons operator that combines the two values

-- How does the above line of code create an infinite list of Fibonacci numbers?
{-
the code creates a list from left to right
the values start with 1, 1 and new values will continue generating
it uses recursion at 'zip fib (tail fib)'
it uses zip to create pairs from the contents of two list
that throws them into a tuple

To explain 'zip fib (tail fib)' in more detail :-
fib is the first value at index 0 i.e., 1
tail is the second value at index 1 i.e., 1

This will now be passed over to (a,b)
Which will pass further and get added to create the third value in the list
-}
1st : fib = 1 and (tail fib) = 1
[1,1,2] : a: 1 + b: 1 = 2

2nd : fib = 1 and (tail fib) = 2
[1,1,2,3] : a: 1 + b: 2 = 3

-- the application of fibonacci sequence
fib300 = fib !! 300

-- end of notes


