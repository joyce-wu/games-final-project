# games-final-project

This project uses hill climbing and genetic algorithms to parameter tune heuristic values in the peg phase of cribbage. We compare the agent tuned with hill climbing and the agent tuned with genetic algorithms to see which performs better against the baseline greedy algorithm. Both algorithms tune

Command line takes in 3 arguments
./TestCribbage –hill –greedy 1000
First argument specifies the agent that will be evaluated
Second argument specifies the baseline agent for comparison
Third argument specifies the number of games that are played
–hill → calls the hill climbing agent
–greedy → called the greedy agent with heuristics 
–genetic → calls the genetic algorithm agent


./TestCribbage --greedy --base 1000
NET: 0.245

./TestCribbage --hill --base 1000
NET: 0.235

./TestCribbage --hill --greedy 1000
NET: -0.002

Hill climbing:
# first tried with smaller number of games to test for functionality
# playing around with parameter range for heuristics to see if it made a difference
# tuning step size
# tried to implement hill climbing stochastically first by choosing random parameter to tune at a time
# implemented hill climbing by choosing parameter with steepest ascent
# a lot of plateauing can happen