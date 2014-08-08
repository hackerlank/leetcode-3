class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, end = 0, len(A)-1
        while i <= end:
            if A[i] == elem:
                A[i], A[end] = A[end], A[i]
                end -= 1
            else:
                i += 1
        return end + 1
