import random

class RandomizedSet:
    def __init__(self):
        self.nums = []      # mảng lưu giá trị
        self.pos = {}       # val -> index trong nums

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.nums[-1]
        # Đưa phần tử cuối vào vị trí idx
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))    # True
    print(rs.remove(2))    # False
    print(rs.insert(2))    # True
    print(rs.getRandom())  # 1 hoặc 2
    print(rs.remove(1))    # True
    print(rs.insert(2))    # False
    print(rs.getRandom())  # 2
