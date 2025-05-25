"""
The problem a median-finding algorithm solves is the following:

Given an array A=[1,...,n] of n numbers and an index i, where 1 ≤ i ≤ n, find the i-th smallest element of A. This problem can certainly be solved using a sorting 
algorithm to sort a list of numbers and return the value at the i -th index. However, many sorting algorithms can’t go faster than nlogn time. A median-finding 
algorithm can find the i-th smallest element in a list in O(n) time.

The median-of-medians algorithm is a deterministic linear-time selection algorithm. The algorithm works by dividing a list into sub-lists and then determines the 
approximate median in each of the sub-lists. Then, it takes those medians and puts them into a list and finds the median of that list. It uses that median value as 
a pivot and compares other elements of the list against the pivot. If an element is less than the pivot value, the element is placed to the left of the pivot, and 
if the element has a value greater than the pivot, it is placed to the right. The algorithm recurses on the list, honing in on the value it is looking for.

"""

def median_of_medians(A, i):

    #divide A into sublists of len 5
    sub_lists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sub_lists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        #the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians) // 2)

    #partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low,i)
    elif i > k:
        return median_of_medians(high,i-k-1)
    else: #pivot = k
        return pivot

if __name__ == '__main__':
    A = [1,2,3,4,5,1000,8,9,99]
    B = [1,2,3,4,5,6]
    print(median_of_medians(A, 0)) #should be 1
    print(median_of_medians(A,7)) #should be 99
    print(median_of_medians(B,4)) #should be 5