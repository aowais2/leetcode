# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = []
        while l1 is not None:
            a.append(l1.val)
            l1 = l1.next
        a = list(reversed(a))
        
        b = []
        while l2 is not None:
            b.append(l2.val)
            l2 = l2.next
        b = list(reversed(b))
        
        '''
        sum = list( map(add, a, b) )
        for i in range(len(sum)):
            if sum[i]/10 > 1:
                sum[i+1] += sum[i]%10
                sum[i] = 0
            elif sum[i]/10 == 1:
                sum[i+1] += 1
                sum[i] = 0
        '''
        
        strings = [str(integer) for integer in a]
        a_string = "".join(strings)
        xa = int(a_string)
        
        strings = [str(integer) for integer in b]
        a_string = "".join(strings)
        xb = int(a_string)
        
        #print(xa + xb)
        return ListNode(xa+xb)
