# Evaluation with precision@k
* method: baseline
* test-proportion: 0.0001
### Precision@k table combinations (method: rank)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | bvp+acc | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | 0.2 | 0.067 | 0.333 | 0.133 | 0.133 | 0.4 | 0.4 | 0.2 | 0.333 | 0.333 | **0.533** | 0.467 | 0.467 | 0.267 | 0.467 | 
| k = 3 | 0.6 | 0.267 | 0.733 | 0.467 | 0.733 | 0.6 | 0.733 | 0.533 | 0.467 | 0.667 | 0.733 | 0.667 | 0.733 | 0.667 | **0.867** | 
| k = 5 | **0.867** | 0.533 | **0.867** | 0.533 | 0.8 | 0.733 | 0.733 | **0.867** | 0.6 | **0.867** | **0.867** | 0.8 | **0.867** | **0.867** | **0.867** | 

### Precision@k table combinations (method: score)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | bvp+acc | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | 0.2 | 0.067 | 0.333 | 0.133 | 0.2 | 0.333 | 0.533 | 0.133 | 0.133 | 0.4 | 0.4 | 0.333 | 0.4 | 0.4 | **0.667** | 
| k = 3 | 0.6 | 0.267 | 0.733 | 0.467 | 0.733 | 0.533 | **0.867** | 0.467 | 0.533 | 0.6 | **0.867** | 0.667 | 0.8 | 0.667 | 0.8 | 
| k = 5 | **0.867** | 0.533 | **0.867** | 0.533 | 0.733 | 0.8 | **0.867** | 0.733 | 0.667 | **0.867** | **0.867** | 0.8 | **0.867** | 0.8 | **0.867** | 

