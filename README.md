## Group
Joyce Wu and Ashley Qin

## Description
In the pegging phase of Cribbage, we applied 5 heuristics to the greedy agent. These heuristics include biasing card values less than 5, placing a card that sums up to 15, placing a card that sums over 15, placing a triple, and placing a double. Each heuristic is set to a default value of 0.5. 

We have created a hill climbing agent and a genetic algorithm agent to tune our heuristic weights in Cribbage. For each agent, we have created a script (`hill_evaluate.py and genetic_evaluate.py`) that use the hill climbing algorithm and genetic algorithm, respectively, to find the heuristic weights that result in the highest expected number of wins for the player using this strategy. The `hill_evaluate.py` script takes around 25 minutes to run starting with parameter constants of 0.5 for each heuristic, while the `genetic_evaluate.py` script takes 2+ hours to run with the number of generations = 2 and individuals in population = 5. We then hard-coded these weights into `test_cribbage.py` so that the final test script does not take as long as each of the agent scripts.

## Results
Hill climbing compared to greedy agent: 0.002 (NET)

Genetic algorithm compared to greedy agent: 0.0007 (NET)

Hill climbing vs Genetic algorithm: 0.0009 (NET)

The hill climbing agent only performs slightly better than the greedy agent (statistically insignificant). This may be due to the fact that the pegging phase of cribbage has many local maxima. The hill climbing algorithm only runs about 10-15 iterations before stopping and hitting a max. After running the hill climbing algorithm, results show that specific heuristics are only biased by a small amount in comparison to each other. This may also mean that the heuristic values are already relatively optimized with constant values of 0.5.

The genetic algorithm agent only performs slightly better than the greedy agent and the hill climbing agent. Due to time constraints, we were only able to run the greedy algorithm with parameters of population size = 5 and number of generations = 2. We suspect that this population size/number of generations did not allow the algorithm enough time to fully explore all maxima. We predict that if the algorithm was given more time to run with a larger population size and greater number of generations, it would have performed better.


## Running the code
Run `make TestCribbage`

Give command-line arguments as follows:

- The script takes in three arguments with 2 specified flags:

  – hill → calls the hill climbing agent
  
  – greedy → calls the greedy agent with heuristics 
  
  – genetic → calls the genetic algorithm agent
  
- The first command-line argument specifies the first agent that will be evaluated (either `--hill`, `genetic`, or `greedy’)
- The second command-line argument specifies the agent that will be played against the first (either `--hill`, `genetic`, or `greedy’)
- The third command-line argument specifies the number of games that are played
- Example: ./TestCribbage –hill –greedy 1000
