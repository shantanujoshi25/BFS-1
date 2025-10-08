# // Time Complexity : O(n)
# // Space Complexity : O(n)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0 for i in range(numCourses)]
        adjlist = { i:[] for i in range(numCourses)}
        q = []

        for i in range(len(prerequisites)):
            indegree[prerequisites[i][0]] += 1
            adjlist[prerequisites[i][1]].append(prerequisites[i][0])

        for i in range(numCourses):
            if( indegree[i] == 0):
                q.append(i)

        count = 0
        while(len(q)>0):
            
            node = q.pop(0)
            #q.extend(adjlist[node])
            count += 1
            for i in adjlist[node]:
                indegree[i] -= 1
                if(indegree[i] == 0):
                    q.append(i)
        return count == numCourses


        
        
        
