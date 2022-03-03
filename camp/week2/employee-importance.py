from ast import List
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
class Solution:
    def dfs(self, employees, idd):
        employee = employees[self.dic[idd]]
        summ = employee.importance
        for uniqueId in employee.subordinates:
            summ += self.dfs(employees, uniqueId)  
        return summ
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.dic = {}
        for i in range(len(employees)):
            self.dic[employees[i].id] = i
        return self.dfs(employees, id)