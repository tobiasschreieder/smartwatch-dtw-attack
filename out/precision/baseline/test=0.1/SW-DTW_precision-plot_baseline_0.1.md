# Evaluation with precision@k
* method: baseline
* test-proportion: 0.1
### Precision@k table combinations (method: rank)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | 0.2 | 0.067 | 0.2 | 0.2 | 0.067 | 0.067 | 0.067 | 0.067 | **0.333** | 0.2 | 0.067 | 0.133 | 0.2 | 0.2 | 
| k = 3 | 0.4 | 0.133 | 0.6 | 0.4 | 0.467 | 0.4 | 0.467 | 0.2 | 0.4 | 0.6 | 0.6 | 0.667 | 0.533 | **0.733** | 
| k = 5 | 0.6 | 0.333 | 0.8 | 0.467 | 0.533 | 0.467 | 0.667 | 0.533 | 0.6 | 0.8 | 0.733 | **0.867** | 0.733 | 0.8 | 

### Precision@k table combinations (method: score)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | **0.2** | 0.067 | **0.2** | **0.2** | 0.067 | **0.2** | 0.067 | 0.067 | **0.2** | 0.067 | 0.067 | **0.2** | 0.133 | 0.133 | 
| k = 3 | 0.4 | 0.133 | **0.6** | 0.4 | 0.2 | 0.4 | 0.333 | 0.133 | 0.467 | 0.333 | 0.133 | 0.467 | 0.333 | 0.333 | 
| k = 5 | 0.6 | 0.333 | **0.8** | 0.467 | 0.4 | 0.4 | 0.467 | 0.467 | 0.533 | 0.533 | 0.533 | 0.667 | 0.533 | 0.533 | 

