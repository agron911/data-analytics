class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {'(':')', '[':']', '{':'}' }  
        inverse_pair = {')':'(', ']':'[', '}':'{'}  
        queue = []
        for parenthese in s:
    #         print(queue)
            if parenthese not in pair:
                if queue == []:
                    return False
                elif queue[-1] != inverse_pair[parenthese]:
                    return False
                else:
                    queue.pop()
            else:
                queue.append(parenthese)
        if queue ==[]:
            return True
        else:
            return False
