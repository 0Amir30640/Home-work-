#Amir Abdollah Abdollahi
import math

mean = 1019
std = 209
score = 820

z = (score - mean) / std

probability = 0.5 * (1 + math.erf(z / math.sqrt(2)))

percent = probability * 100

print("Z Score:", z)
print("Probability:", probability)
print("Percentage:", percent, "%")