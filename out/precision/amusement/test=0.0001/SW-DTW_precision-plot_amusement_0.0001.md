# Evaluation with precision@k
* method: amusement
* test-proportion: 0.0001
### Precision@k table combinations (method: rank)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | bvp+acc | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | 0.267 | 0.133 | 0.133 | 0.133 | 0.2 | 0.267 | 0.2 | 0.067 | 0.067 | 0.133 | **0.333** | 0.2 | 0.267 | 0.067 | 0.267 | 
| k = 3 | **0.8** | 0.2 | 0.533 | 0.333 | 0.6 | 0.667 | 0.667 | 0.6 | 0.267 | 0.267 | 0.733 | 0.533 | 0.6 | 0.533 | 0.667 | 
| k = 5 | **0.933** | 0.4 | 0.733 | 0.4 | 0.867 | 0.733 | 0.8 | 0.667 | 0.467 | 0.467 | 0.867 | 0.8 | 0.8 | 0.733 | 0.733 | 

### Precision@k table combinations (method: score)
| Precision@k | bvp | eda | acc | temp | bvp+eda | bvp+temp | bvp+acc | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| k = 1 | 0.267 | 0.133 | 0.133 | 0.133 | 0.2 | 0.267 | **0.4** | 0.133 | 0.133 | 0.2 | 0.333 | 0.2 | 0.267 | 0.2 | 0.333 | 
| k = 3 | **0.8** | 0.2 | 0.533 | 0.333 | 0.533 | 0.533 | **0.8** | 0.4 | 0.333 | 0.267 | 0.733 | 0.6 | **0.8** | 0.333 | 0.6 | 
| k = 5 | **0.933** | 0.4 | 0.733 | 0.4 | 0.867 | 0.8 | 0.867 | 0.667 | 0.467 | 0.6 | **0.933** | 0.8 | 0.867 | 0.733 | 0.867 | 

