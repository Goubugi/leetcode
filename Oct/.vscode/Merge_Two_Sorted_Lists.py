#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]):
        head = current = ListNode()
        while (list1 and list2):
            if list1.val <= list2.val:
                current.next = list1
                list1, current = list1.next, current.next
        restOfLL = list2 if list1 else list1
        current.next = restOfLL
        return head
                
if __name__ == "__main__":
    s = Solution()
    l = ListNode(1)
    l2 = ListNode(2, l)
    l3 = ListNode(3, l2)
    

        