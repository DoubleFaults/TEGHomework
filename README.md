# code examination

## Puzzles

### 第一题

三个数组A[], B[], C[]

求A第3大的数 + B第4小的数 + C第5大的数结果, 不存在则为0

```cpp
long long GetResult(vector<int> A, vector<int> B, vector<int> C)

{

}
```

### 第二题

数组A[n]

设数组A的子集为连续m个数，即A[0:m-1] , A[1:m] … A[n-m+1:n]

子集的和为这m个数相加，求和最大的子集(有多个则输出多个)

```cpp
vector<vector<int>> GetResult(vector<int> A, int n, int m)

{

}
```

### 第三题

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

## Solution

### P1

use `max heap` to find out n-th smallest element in a list, and `smallest heap` to find out n-th largest element in a list.

Big O is approximately n * log(n, 2) for each lookup journey.

### P2

#### method 1

sum with sliding a window.

keep the largest sum of a window, and loop:

    - if find a new sum of a window is larger than the kept one, replace it
    - if found one equal to the kept one, append the new window
    - otherwise keep going.

Big O is sqrt(n, 2)

the problem is I do too much re-calculation.

for example, 

A = [1, 2, 3, 4], m = 3

    loop 1: sum([1, 2, 3])
    loop 2: sum([2, 3, 4])
    it needn't re-calculating sum(2, 3) in every loop

if I solve this problem, Big O will be (n). That will be a reasonable complexity.

#### method 2

Fortunately, it is easy, just loop this:

    - the sum minus the beginning element of the window in last loop
    - plus new coming element in this loop to the sum
    - do the stuff introduced in method 1

### P3

each array should be regarded as looping array. [1, 4] and [4, 1] has the same order.

but I am running out of time.

## Verify solutions

> NOTE: requires Python 3.7+

`docker run -it --rm -v $(pwd)/src:/work python:3.7-alpine3.9 /usr/bin/env python3 "/work/main.py"`
