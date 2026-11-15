class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu = deque(students)
        san = deque(sandwiches)
        while san and san[0] in stu:
            if stu[0] == san[0]:
                stu.popleft()
                san.popleft()
            else:
                stu.append(stu.popleft())
        return len(stu)