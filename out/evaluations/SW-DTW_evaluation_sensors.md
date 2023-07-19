# Evaluation of Sensor-Combinations: 
* Calculated with rank_method: 'score' 
* Calculated with averaging-method: 'weighted-mean' 
* Preferred sensor-combination: 'bvp+acc' (decision based on smallest k) 
## Precision@k table: 
| k |bvp | eda | acc | temp | bvp+eda | bvp+temp | bvp+acc | eda+acc | eda+temp | acc+temp | bvp+eda+acc | bvp+eda+temp | bvp+acc+temp | eda+acc+temp | bvp+eda+acc+temp | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.19 | 0.104 | 0.223 | 0.127 | 0.179 | 0.228 | 0.375 | 0.135 | 0.107 | 0.224 | 0.232 | 0.162 | 0.237 | 0.187 | 0.27 | 
| 3 | 0.499 | 0.252 | 0.51 | 0.357 | 0.448 | 0.439 | 0.643 | 0.382 | 0.337 | 0.382 | 0.547 | 0.446 | 0.541 | 0.409 | 0.523 | 
| 5 | 0.677 | 0.457 | 0.668 | 0.456 | 0.626 | 0.559 | 0.754 | 0.575 | 0.52 | 0.6 | 0.705 | 0.603 | 0.675 | 0.586 | 0.659 | 
| max@k | k = 15 | k = 15 | k = 15 | k = 15 | k = 15 | k = 15 | k = 14 | k = 15 | k = 15 | k = 15 | k = 15 | k = 15 | k = 15 | k = 15 | k = 15 | 

