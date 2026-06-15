from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_idx = {}  # email -> index tài khoản
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_idx:
                    uf.union(i, email_to_idx[email])
                else:
                    email_to_idx[email] = i

        # Gom nhóm email theo root
        idx_to_emails = defaultdict(set)
        for email, i in email_to_idx.items():
            root = uf.find(i)
            idx_to_emails[root].add(email)

        # Tạo kết quả
        res = []
        for idx, emails in idx_to_emails.items():
            res.append([accounts[idx][0]] + sorted(emails))
        return res

if __name__ == "__main__":
    s = Solution()
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
    print(s.accountsMerge(accounts))
