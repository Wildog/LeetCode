# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class NumMaker(object):
    def __init__(self, num):
        num, mod = divmod(num, 10)
        self.head = ListNode(mod)
        while (num > 0):
            num, mod = divmod(num, 10)
            self.tail(self.head).next = ListNode(mod)

    def __str__(self):
        r = ""
        curr = self.head
        while curr:
            r = r + str(curr.val) + " --> "
            curr = curr.next
        return r

    def tail(self, node):
        while node.next:
            node = node.next
        return node

    @staticmethod
    def getNumber(node):
        num = node.val
        mul = 10
        while node.next:
            node = node.next
            num += node.val * mul
            mul *= 10
        return num

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(None)
        curr = dummy
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = carry + n1 + n2
            carry = sum / 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next

if __name__ == '__main__':
    l1 = NumMaker(35).head
    l2 = NumMaker(65).head
    solution = Solution()
    print(NumMaker(NumMaker.getNumber(solution.addTwoNumbers(l1, l2))))
