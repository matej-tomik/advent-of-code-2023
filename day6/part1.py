import math

races = [[58, 478], [99, 2232], [64, 1019], [69, 1071]]
solution = 1
for race in races:
    solution = solution * math.ceil((race[0]/2-((-race[0]+math.sqrt(race[0]**2 - 4*race[1]))/(-2)))*2)
print(solution)
