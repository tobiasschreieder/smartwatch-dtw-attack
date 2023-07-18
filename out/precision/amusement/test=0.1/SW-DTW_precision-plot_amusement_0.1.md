# Evaluation with precision@k
* method: amusement
* test-proportion: 0.1
### Precision@k table combinations (method: rank)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | **0.2** | 0.067 | 0.133 | 0.133 | 0.0 | 0.067 | 0.067 | 0.067 | 0.133 | 0.133 | 0.133 | 0.067 | 0.0 | 0.067 | 
| k = 3 | **0.467** | 0.133 | 0.333 | 0.267 | 0.267 | 0.267 | 0.2 | 0.133 | 0.2 | 0.4 | 0.2 | 0.333 | 0.133 | 0.267 | 
| k = 5 | **0.6** | 0.333 | 0.533 | 0.4 | 0.467 | 0.4 | 0.4 | 0.2 | 0.333 | 0.533 | 0.333 | 0.533 | 0.333 | 0.467 | 

### Precision@k table combinations (method: score)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | **0.2** | 0.067 | 0.133 | 0.133 | 0.133 | **0.2** | 0.0 | 0.067 | **0.2** | 0.067 | 0.067 | 0.133 | 0.067 | 0.133 | 
| k = 3 | **0.467** | 0.133 | 0.333 | 0.267 | 0.267 | 0.267 | 0.267 | 0.133 | 0.267 | 0.333 | 0.2 | 0.333 | 0.2 | 0.2 | 
| k = 5 | **0.6** | 0.333 | 0.533 | 0.4 | 0.533 | 0.467 | 0.4 | 0.2 | 0.4 | 0.533 | 0.333 | 0.467 | 0.333 | 0.4 | 

