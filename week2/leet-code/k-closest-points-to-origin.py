import math
def kClosest(points, k):
    distances = {}
    final = []
    for i in range(len(points)):
        m = (points[i][0] ** 2) + (points[i][1] ** 2)
        m = math.sqrt(m)
        distances.update({i:m})
    newDistances = (sorted(distances.items(), key =
             lambda kv:(kv[1], kv[0])))
    count = 0
    for key, _ in newDistances:
        if count == k:
            break
        final.append(points[key])
        count+=1

    return final