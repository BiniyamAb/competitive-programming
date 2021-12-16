# from typing import List

# def findOriginalArray(changed: List[int]) -> List[int]:
#     doubled = []
#     doubles = []
#     frequencyArr = [0] * 100001
#     for i in range(len(changed)):
#         frequencyArr[changed[i]]+=1
    
#     for val in changed:
#         if frequencyArr[val * 2] != 0:
#             doubled.append(val)
#         else:
#             doubles.append(val)

#     for val in doubles:
#         if val == 0:
#             if frequencyArr[0] < 2:
#                 return []
#         if val % 2 != 0:
#             return []
#         elif frequencyArr[val // 2] == 0:
#             return []
    

# #     return doubled
        
            


# # print(findOriginalArray([1,3,4,2,6,8]))
# to= {}
# to[1] = 2
# to[2] = 4
# to[4] = 8
