class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        if not start or not end:
            return []
        
        results =[]
        visited_idx = {}
        visited_word = {}
        set = []
        final_results = []
        for idx in range(len(start)):
            visited_idx[idx] = 0
        for w in dict:
            visited_word[w] = 0
        visited_word[start] = 1
        set.append(start)
        
        self.helper(start, end, dict, results, visited_idx, visited_word, set)
        
        min =  float("inf")
        for s in results:
            if len(s) < min:
                min = len(s)
        
        for s in results:
            if len(s) == min:
                s.append(end)
                final_results.append(s)
                
        return final_results 
    
    def helper(self, start, end, dict, results, visited_idx, visited_word, set):
        diff_num = 0 
        last_w = set[-1]
        for i in range(len(end)):
            if diff_num > 1:
                break
            if last_w[i] != end[i]:
                diff_num += 1
        
        if diff_num <= 1:
            results.append(list(set))
            
        for i in range(len(start)):
            if visited_idx[i] == 1 :
                continue
            
            for w in dict:
                print(w, "w-before")
                if visited_word[w] == 1:
                    continue
                print(w, "w-after")
                print(i, "i")
                print(w[0:i], "w[0:i]")
                print(set[-1][0:i], "set[-1][0:i]")
                print(w[i+1:], "w[i+1:]")
                print(set[-1][i+1:], "set[-1][i+1:]")
                if w[0:i] == set[-1][0:i] and w[i+1:] == set[-1][i+1:]:
                    set.append(w)
                    print(set, "set")
                    visited_idx[i] = 1
                    visited_word[w] = 1
                    self.helper(start, end, dict, results, visited_idx, visited_word, set)
                    set.pop()
                    visited_idx[i] = 0 
                    visited_word[w] = 0 
            
            visited_idx[i] == 1

test = Solution()
start = "game"
end = "thee"
dict_1 = ["frye","heat","tree","thee","game","free","hell","fame","faye"]
print(test.findLadders(start, end, dict_1))
