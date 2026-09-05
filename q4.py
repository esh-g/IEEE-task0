# Q4 - numpy basics
# values are written directly here, csv is used from q5 onwards

import numpy as np

hours = np.array([6.8, 7.3, 5.9, 6.1, 5.9, 6.0, 6.3, 3.6, 6.5, 1.2])
attendance = np.array([87, 92, 77, 67, 100, 62, 88, 85, 73, 74])
previous = np.array([92, 49, 95, 92, 52, 66, 61, 74, 49, 77])
final = np.array([79, 69, 67, 63, 60, 55, 52, 47, 41, 35])

print("hours      ", hours.shape, hours.dtype)
print("attendance ", attendance.shape, attendance.dtype)
print("previous   ", previous.shape, previous.dtype)
print("final      ", final.shape, final.dtype)

print()
print("Mean final score:", final.mean())
print("Max final score:", final.max())
print("Min final score:", final.min())
print("Std deviation:", round(final.std(), 2))

bonus = final + 5
print("After 5 bonus marks:", bonus)

# boolean array for scores 75 and above
above_75 = final >= 75
print("Scored 75 or more?", above_75)
print("Those scores:", final[above_75])
