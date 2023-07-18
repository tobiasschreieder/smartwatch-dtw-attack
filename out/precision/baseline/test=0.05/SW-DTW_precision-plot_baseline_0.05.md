# Evaluation with precision@k
* method: baseline
* test-proportion: 0.05
### Precision@k table combinations (method: rank)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | 0.133 | 0.067 | **0.267** | 0.2 | 0.133 | 0.133 | 0.067 | 0.067 | **0.267** | 0.2 | 0.067 | 0.2 | 0.2 | 0.133 | 
| k = 3 | 0.267 | 0.2 | **0.6** | 0.4 | 0.267 | 0.267 | 0.4 | 0.333 | 0.4 | **0.6** | 0.467 | **0.6** | 0.533 | 0.533 | 
| k = 5 | 0.467 | 0.333 | 0.733 | 0.533 | 0.467 | 0.467 | 0.667 | 0.6 | 0.733 | 0.667 | 0.667 | **0.8** | **0.8** | **0.8** | 

### Precision@k table combinations (method: score)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | 0.133 | 0.067 | **0.267** | 0.2 | 0.067 | 0.2 | 0.067 | 0.067 | **0.267** | 0.067 | 0.067 | 0.2 | 0.133 | 0.133 | 
| k = 3 | 0.267 | 0.2 | **0.6** | 0.4 | 0.2 | 0.4 | 0.333 | 0.4 | 0.4 | 0.4 | 0.333 | 0.533 | 0.467 | 0.467 | 
| k = 5 | 0.467 | 0.333 | **0.733** | 0.533 | 0.467 | 0.6 | 0.6 | 0.6 | **0.733** | 0.667 | 0.6 | **0.733** | 0.6 | 0.6 | 

