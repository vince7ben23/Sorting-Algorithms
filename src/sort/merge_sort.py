from collections import deque

class MergeSortRecursive:
    """merge sort with a recursive approach

    steps: divid, then merge and sort
    """
    @staticmethod
    def _merge(arr, left: int, mid: int, right: int) -> None:
        """merge with pointer approach

        Args:
            arr (_type_): an array is to sort in place
            left (int): the start point of the array we want to sort
            mid (int): the middle between the start point and the end point
            right (int): the end point of the array we want to sort
        """        
        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1:right+1]
        left_ptr = 0
        right_ptr = 0
        k = left

        while left_ptr < len(left_arr) and right_ptr < len(right_arr):
            if left_arr[left_ptr] <= right_arr[right_ptr]:
                arr[k] = left_arr[left_ptr]
                left_ptr += 1
            else:
                arr[k] = right_arr[right_ptr]
                right_ptr += 1
            k += 1

        # copy remaining elements
        arr[k:k + len(left_arr) - left_ptr] = left_arr[left_ptr:]
        k += len(left_arr) - left_ptr
        arr[k:right + 1] = right_arr[right_ptr:]

    @classmethod
    def merge_sort(cls, arr: list, left: int, right: int) -> None:
        """merge sort with a recursive approach

        Args:
            arr (list): an array is to sort in place
            left (int): start point of the array we want to sort
            right (int): end point of the array we want to sort
        """
        if left == right:
            return
        mid = (left + right) // 2
        cls.merge_sort(arr, left, mid)
        cls.merge_sort(arr, mid+1, right)
        cls._merge(arr, left, mid, right)


class MergeSortIterative:
    """merge sort with an iterative approach
    implement with a queue
    """
    @staticmethod
    def _merge(left_que: deque, right_que: deque) -> deque:
        """

        Args:
            left_que (deque): the left array is to be merged
            right_que (deque): the right array is to be merged

        Returns:
            deque: the merged and sorted array
        """        
        res = deque()
        while left_que or right_que:
            if left_que and right_que:
                if left_que[0] <= right_que[0]:
                    res.append(left_que.popleft())
                else:
                    res.append(right_que.popleft())
            else:
                if not right_que:
                    res.append(left_que.popleft())
                else:
                    res.append(right_que.popleft())
        return res

    @classmethod
    def merge_sort(cls, arr: list) -> None:
        """merge sort with an iterative approach
        implement with a queue 

        Args:
            arr (list): an array is to sort in place
        
        Note:
            list.pop(0) is O(n),
            deque.popleft() is O(1),
            switch to use collection.deque
        """
        queue = deque()
        for ele in arr:
            queue.append(deque([ele]))
        # print(queue)
        while len(queue) > 1:
            left_que = queue.popleft()
            right_que = queue.popleft()
            merged_que = cls._merge(left_que, right_que)
            queue.append(merged_que)
        arr[:] = list(queue.pop())


class MergeSortIterativeWithStack:
    """merge sort with two stack"""

    @staticmethod
    def _merge(arr: list, left: int, mid: int, right: int) -> None:
        left_que = deque(arr[left:mid+1])
        right_que = deque(arr[mid+1:right+1])
        k = left

        while left_que and right_que:
            if left_que[0] <= right_que[0]:
                arr[k] = left_que.popleft()
            else:
                arr[k] = right_que.popleft()
            k += 1

        # copy remaining elements
        while left_que:
            arr[k] = left_que.popleft()
            k += 1
        while right_que:
            arr[k] = right_que.popleft()
            k += 1

        
    
    @classmethod
    def merge_sort(cls, arr: list, left: int, right: int) -> None:
        """merge sort with two stack
        one is to divid array
        another is to merge and sort

        Args:
            arr (list): the array is to be sorted in place
            left (int): the start point of the array
            right (int): the end point of the array
        """
        stack = []
        stack2 = []

        stack.append(right)
        stack.append(left)

        stack2.append(right)
        stack2.append(left)
        # divid into smallest element
        while stack2:
            start = stack2.pop()
            end = stack2.pop()
            mid = (start + end) // 2

            # left subarray
            if start < mid:
                stack.append(mid)
                stack.append(start)
                stack2.append(mid)
                stack2.append(start)

            # right sub-arrary
            if mid+1 < end:
                stack.append(end)
                stack.append(mid+1)
                stack2.append(end)
                stack2.append(mid+1)
        
        # merge and sort
        while stack:
            start = stack.pop()
            end = stack.pop()
            mid = (start + end) // 2
            cls._merge(arr, start, mid, end)


