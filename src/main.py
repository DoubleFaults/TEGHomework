#! /usr/bin/env python3

from typing import List


def P1_GetResult(A: List[int], B: List[int], C: List[int]) -> int:
    """
    三个数组A[], B[], C[]

    求A第3大的数 + B第4小的数 + C第5大的数结果, 不存在则为0

    ```cpp
    long long GetResult(vector<int> A, vector<int> B, vector<int> C)

    {

    }
    ```
    >>> P1_GetResult([1,2,3,4], [1,2,3,4,5], [1,2,3,4,5,6])
    8
    >>> P1_GetResult([1,2], [1,2,3], [1,2,3,4])
    0
    >>> P1_GetResult([1,2], [3, 4, 5, 6], [7, 8, 9])
    6
    >>> P1_GetResult([1, 4, 5, 7], [5, 1, 1, 1, 0], [89, 1, 5, 55, 54, 99])
    9
    >>> P1_GetResult([1, 1, 1, 2, 3], [1, 1, 1, 2, 2, 2, 3, 4], [1, 2, 2, 2, 2, 3, 4, 5])
    6
    """
    from heapq import heapify, heappop, heappush

    def nth_smallest(iterables: List[int], nth: int) -> int:
        # init a smallest heap,
        #   which means the element at idx 0 is the smallest of the list itself
        h = iterables[:nth]
        heapify(h)

        for i in iterables[nth:]:
            if i > h[0]:
                heappop(h)
                heappush(h, i)
        return h[0]

    def nth_largest(iterables: List[int], nth: int) -> int:
        # init a max heap,
        #   which means the element at idx 0 is the smallest of the list itself
        h = iterables[:nth]
        heapify(h)

        for i in iterables[nth:]:
            if i < h[0]:
                heappop(h)
                heappush(h, i)
        return h[-1]

    # de-duplicated -> setup a heap -> pop to sum
    result = 0
    if len(set(A)) >= 3:
        result += nth_smallest(list(set(A)), 3)
    if len(set(B)) >= 4:
        result += nth_largest(list(set(B)), 4)
    if len(set(C)) >= 5:
        result += nth_smallest(list(set(C)), 5)

    return result

    # or just
    # return (nth_smallest(A, 3) if len(A) > 3 else 0) + \
    #     (nth_largest(B, 4) if len(C) > 4 else 0) + \
    #     (nth_smallest(C, 5) if len(C) > 5 else 0)


def P2_GetResult(A: List[int], n: int, m: int) -> List[List[int]]:
    """
    数组A[n]

    设数组A的子集为连续m个数，即A[0:m-1] , A[1:m] … A[n-m+1:n]

    子集的和为这m个数相加，求和最大的子集(有多个则输出多个)

    ```cpp
    vector<vector<int>> GetResult(vector<int> A, int n, int m)

    {

    }
    ```
    >>> P2_GetResult([1, 2, 3], 3, 2)
    [[2, 3]]
    >>> P2_GetResult([32, 0, -1, 7, -42, 5], 6, 3)
    [[32, 0, -1]]
    >>> P2_GetResult([1, 1, 1, 1, 1, 1, 1], 7, 4)
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    """

    def method_1():
        # in Python, the interval of a list is left bounded, right open
        champion_sum = sum(A[0:m])
        result: List[List[int]] = [A[0:m]]
        for mm in range(1, m):
            new_sum = sum(A[mm: mm+m])
            if new_sum > champion_sum:
                champion_sum = new_sum
                result = [A[mm: mm+m]]
            elif new_sum == champion_sum:
                result.append(A[mm: mm+m])
        return result

    # method 1 is re-calculate (m - 1) elements in each loop
    # not good enough
    # return method_1()

    # method_2 reduces the partly re-sum to 0
    def method_2():
        champion_sum = sum(A[0:m])
        result = [A[0:m]]

        # we are not going to use sum() any more
        sum_ = champion_sum
        for i in range(m, n):
            sum_ = sum_ - A[i-m] + A[i]
            if sum_ > champion_sum:
                champion_sum = sum_
                result = [A[i-m+1:i+1]]
            elif sum_ == champion_sum:
                result.append(A[i-m+1:i+1])
        return result

    return method_2()


def P3_GetResult(A: List[int], B: List[int], C: List[int]) -> List[int]:
    """
    给定三个数组A,B,C找到它们的有序交集S

    例如

    ``` cpp
    A[] = [1, 2, 3,4]

    B[] = [1, 2, 4]

    C[] = [4, 3, 1]

    S[] = [1,4]
    ```

    ```cpp
    vector<int> GetResult(vector<int> A, vector<int> B, vector<int> C)

    {

    }
    ```
    >>> P3_GetResult([1, 2, 3, 4], [1, 2, 4], [4, 3, 1])
    [1, 4]
    """
    raise NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
