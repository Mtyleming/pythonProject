# import area
import day5.dir.student as s
import day5.dir.class_demo as c


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(m, len(nums1), 1):
            nums1[i] = nums2[i - n]
        nums1.sort()


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    n = 3
    m = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
    print(s.get_total(nums1))
    print(s.SCORE)
    print(__name__)
    print(s.__name__)
    print(s.FULL)
    ob = c.Student("张三", 18)
    print(ob.__dict__)
    ob.introduce()


