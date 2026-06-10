# 30 Days of DSA Challenge – Part 2 🔥

(Day 31 → Day 60)

Chào mừng đến với **giai đoạn 2** của lộ trình 60 ngày luyện tập Cấu trúc Dữ liệu & Giải thuật.  
Mỗi ngày một bài, nâng cao tư duy với các chủ đề: cửa sổ trượt, đồ thị, quay lui, Trie, quy hoạch động, cây, toán, bitmask, v.v.

---

## 📋 Danh sách bài tập

### Day 31: Merge Intervals
**Mô tả:** Cho mảng các khoảng `intervals` với `intervals[i] = [start_i, end_i]`. Gộp tất cả các khoảng chồng lấn và trả về mảng mới gồm các khoảng không chồng lấn bao phủ toàn bộ khoảng ban đầu.  
**Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`  
**Output:** `[[1,6],[8,10],[15,18]]`

---

### Day 32: Insert Interval
**Mô tả:** Cho danh sách các khoảng không chồng lấn đã được sắp xếp theo thời gian bắt đầu, và một khoảng mới `newInterval`. Chèn `newInterval` vào đúng vị trí và gộp nếu cần, trả về danh sách mới.  
**Input:** `intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`  
**Output:** `[[1,5],[6,9]]`

---

### Day 33: Minimum Window Substring
**Mô tả:** Cho hai chuỗi `s` và `t`, tìm cửa sổ nhỏ nhất trong `s` chứa tất cả các ký tự của `t` (bao gồm cả trùng lặp). Nếu không có cửa sổ nào, trả về `""`.  
**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`  
**Output:** `"BANC"`  
**Ràng buộc:** `1 <= s.length, t.length <= 10^5`

---

### Day 34: Sliding Window Maximum
**Mô tả:** Cho mảng số nguyên `nums` và số nguyên `k`, trả về một mảng chứa giá trị lớn nhất của mỗi cửa sổ con độ dài `k` trượt từ trái qua phải.  
**Input:** `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`  
**Output:** `[3,3,5,5,6,7]`

---

### Day 35: Largest Rectangle in Histogram
**Mô tả:** Cho mảng `heights` biểu diễn chiều cao các cột của biểu đồ histogram, tính diện tích hình chữ nhật lớn nhất có thể tạo thành trong biểu đồ.  
**Input:** `heights = [2,1,5,6,2,3]`  
**Output:** `10`

---

### Day 36: Maximal Rectangle
**Mô tả:** Cho ma trận nhị phân `matrix` chỉ chứa `'0'` và `'1'`, tìm diện tích hình chữ nhật lớn nhất chỉ toàn `'1'`.  
**Input:** `matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]`  
**Output:** `6`

---

### Day 37: Coin Change
**Mô tả:** Cho mảng `coins` chứa mệnh giá của các đồng xu và số tiền `amount`. Trả về số đồng xu ít nhất để tạo thành `amount`. Nếu không thể, trả về `-1`.  
**Input:** `coins = [1,2,5]`, `amount = 11`  
**Output:** `3` (5 + 5 + 1)  
**Ràng buộc:** `1 <= coins.length <= 12`, `1 <= coins[i] <= 2^31 - 1`, `0 <= amount <= 10^4`

---

### Day 38: Longest Common Subsequence
**Mô tả:** Cho hai chuỗi `text1` và `text2`, tìm độ dài của dãy con chung dài nhất (không nhất thiết liên tiếp).  
**Input:** `text1 = "abcde"`, `text2 = "ace"`  
**Output:** `3` (dãy con "ace")

---

### Day 39: Burst Balloons
**Mô tả:** Cho `n` bóng bay, mỗi bóng có một số `nums[i]`. Khi làm nổ bóng `i`, bạn nhận được số xu = `nums[i-1] * nums[i] * nums[i+1]`. Sau khi nổ, bóng `i-1` và `i+1` trở thành kề nhau. Tìm số xu tối đa có thể thu được. Các bóng giả ở hai đầu có giá trị `1`.  
**Input:** `nums = [3,1,5,8]`  
**Output:** `167` (thứ tự nổ: 1,5,3,8)

---

### Day 40: Word Break
**Mô tả:** Cho chuỗi `s` và tập từ điển `wordDict`, kiểm tra xem có thể phân tách `s` thành các từ có trong từ điển không (mỗi từ có thể dùng nhiều lần).  
**Input:** `s = "leetcode"`, `wordDict = ["leet","code"]`  
**Output:** `True`

---

### Day 41: Clone Graph
**Mô tả:** Cho một đồ thị vô hướng được biểu diễn bởi các nút, mỗi nút có `val` và danh sách `neighbors`. Tạo ra một bản sao sâu (deep copy) của đồ thị.  
**Input:** Đồ thị `[[2,4],[1,3],[2,4],[1,3]]`  
**Output:** Bản sao có cấu trúc tương tự.

---

### Day 42: Word Ladder
**Mô tả:** Cho hai từ `beginWord` và `endWord`, và danh sách `wordList`. Tìm độ dài đường biến đổi ngắn nhất từ `beginWord` đến `endWord`, mỗi bước chỉ thay đổi một ký tự và từ mới phải có trong `wordList`. Trả về số bước (tính cả điểm bắt đầu), hoặc 0 nếu không thể.  
**Input:** `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`  
**Output:** `5` (hit -> hot -> dot -> dog -> cog)

---

### Day 43: Serialize and Deserialize Binary Tree
**Mô tả:** Thiết kế thuật toán để tuần tự hóa (serialize) và giải tuần tự hóa (deserialize) một cây nhị phân.  
**Ví dụ:** Cây `[1,2,3,null,null,4,5]` được serialize thành một chuỗi, sau đó deserialize khôi phục lại cây ban đầu.

---

### Day 44: Subsets II
**Mô tả:** Cho mảng số nguyên `nums` có thể chứa các phần tử trùng lặp. Trả về tất cả các tập con có thể (tập lực lượng) không được chứa tập con trùng lặp.  
**Input:** `nums = [1,2,2]`  
**Output:** `[[],[1],[1,2],[1,2,2],[2],[2,2]]`

---

### Day 45: Combination Sum II
**Mô tả:** Cho tập ứng cử viên `candidates` (có thể trùng lặp) và số `target`. Tìm tất cả các bộ (combination) duy nhất trong đó tổng bằng `target`. Mỗi số trong `candidates` chỉ được dùng một lần.  
**Input:** `candidates = [10,1,2,7,6,1,5]`, `target = 8`  
**Output:** `[[1,1,6],[1,2,5],[1,7],[2,6]]`

---

### Day 46: Permutations II
**Mô tả:** Cho mảng `nums` có thể chứa các phần tử trùng lặp. Trả về tất cả các hoán vị duy nhất.  
**Input:** `nums = [1,1,2]`  
**Output:** `[[1,1,2],[1,2,1],[2,1,1]]`

---

### Day 47: N-Queens
**Mô tả:** Bài toán N quân hậu: đặt `n` quân hậu lên bàn cờ vua `n x n` sao cho không quân nào tấn công nhau. Trả về tất cả các cách sắp xếp. Mỗi cách biểu diễn bằng danh sách chuỗi, 'Q' cho hậu, '.' cho ô trống.  
**Input:** `n = 4`  
**Output:** Hai cách: `[".Q..","...Q","Q...","..Q."]` và `["..Q.","Q...","...Q",".Q.."]`

---

### Day 48: Sudoku Solver
**Mô tả:** Viết chương trình giải bảng Sudoku `9x9` bằng cách điền các số từ 1-9. Bảng chưa giải có các ô trống ký hiệu `'.'`. Giải trực tiếp trên bảng.  
**Input:** Bảng Sudoku hợp lệ (có lời giải duy nhất).  
**Output:** Bảng được giải.

---

### Day 49: LRU Cache
**Mô tả:** Thiết kế cấu trúc bộ nhớ đệm LRU (Least Recently Used) với dung lượng cố định. Hỗ trợ `get(key)` và `put(key, value)` trong O(1). Khi đầy, loại bỏ phần tử ít được dùng nhất.  
**Input:** 
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache là {1=1}
lRUCache.put(2, 2); // cache là {1=1, 2=2}
lRUCache.get(1); // trả về 1
lRUCache.put(3, 3); // vượt dung lượng, xóa key 2, cache là {1=1, 3=3}
lRUCache.get(2); // trả về -1 (không tìm thấy)
**Output:** `[null,null,null,1,null,-1]`

---

### Day 50: Insert Delete GetRandom O(1)
**Mô tả:** Cài đặt cấu trúc `RandomizedSet` hỗ trợ các thao tác sau với độ phức tạp trung bình O(1): `insert(val)`, `remove(val)`, `getRandom()` – trả về một phần tử ngẫu nhiên trong tập.  
**Input:** Ví dụ: insert 1, remove 2, insert 2, getRandom (có thể 1 hoặc 2), remove 1, insert 2, getRandom (luôn trả về 2).  
**Ràng buộc:** `-2^31 <= val <= 2^31 - 1`, tối đa `2*10^5` thao tác.

---

### Day 51: Word Search II
**Mô tả:** Cho lưới ký tự `board` kích thước `m x n` và danh sách từ `words`. Trả về tất cả các từ có trong lưới. Mỗi từ được tạo bằng cách di chuyển theo các ô liền kề (ngang/dọc), không dùng lại ô.  
**Input:** `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]`, `words = ["oath","pea","eat","rain"]`  
**Output:** `["eat","oath"]`

---

### Day 52: Accounts Merge
**Mô tả:** Cho danh sách các tài khoản `accounts`, mỗi phần tử là `[name, email1, email2, ...]`. Hợp nhất các tài khoản có chung email. Mỗi tài khoản sau khi gộp phải có tên người dùng và danh sách email đã sắp xếp.  
**Input:** `accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`  
**Output:** `[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`

---

### Day 53: Pow(x, n)
**Mô tả:** Cài đặt hàm `myPow(x, n)` tính `x^n` (x lũy thừa n). Không dùng thư viện.  
**Input:** `x = 2.00000, n = 10`  
**Output:** `1024.00000`  
**Ràng buộc:** `-100.0 < x < 100.0`, `-2^31 <= n <= 2^31-1`.

---

### Day 54: Sqrt(x)
**Mô tả:** Tính căn bậc hai số nguyên của `x`, chỉ lấy phần nguyên. Không dùng hàm mũ hoặc `**`.  
**Input:** `x = 8`  
**Output:** `2` (vì sqrt(8) = 2.82842..., lấy phần nguyên là 2)

---

### Day 55: Single Number II
**Mô tả:** Cho mảng số nguyên `nums`, trong đó mọi phần tử đều xuất hiện đúng **ba lần** ngoại trừ một phần tử xuất hiện **một lần**. Tìm phần tử đơn độc đó. Thuật toán phải chạy trong O(n) và dùng O(1) bộ nhớ.  
**Input:** `nums = [2,2,3,2]`  
**Output:** `3`

---

### Day 56: Kth Smallest Element in a BST
**Mô tả:** Cho gốc của cây tìm kiếm nhị phân (BST) và số nguyên `k`, trả về phần tử nhỏ thứ `k` trong BST.  
**Input:** `root = [3,1,4,null,2]`, `k = 1`  
**Output:** `1`  
**Ràng buộc:** `1 <= k <= số nút`.

---

### Day 57: Binary Tree Level Order Traversal
**Mô tả:** Cho cây nhị phân, trả về danh sách các mức (level order) từ trái sang phải.  
**Input:** `root = [3,9,20,null,null,15,7]`  
**Output:** `[[3],[9,20],[15,7]]`

---

### Day 58: Minimum Depth of Binary Tree
**Mô tả:** Cho cây nhị phân, tìm độ sâu nhỏ nhất (số nút trên đường đi ngắn nhất từ gốc đến lá).  
**Input:** `root = [3,9,20,null,null,15,7]`  
**Output:** `2` (3 → 9)

---

### Day 59: Count Primes
**Mô tả:** Đếm số lượng số nguyên tố nhỏ hơn số nguyên dương `n`.  
**Input:** `n = 10`  
**Output:** `4` (2,3,5,7)

---

### Day 60: Perfect Squares
**Mô tả:** Cho số nguyên dương `n`, tìm số lượng ít nhất các số chính phương (1,4,9,16,...) có tổng bằng `n`.  
**Input:** `n = 12`  
**Output:** `3` (12 = 4 + 4 + 4)  
**Ràng buộc:** `1 <= n <= 10^4`

---

Chúc bạn luyện tập vui vẻ và sớm chinh phục mọi kỳ phỏng vấn! 💻⚡
### Day 49: LRU Cache
**Mô tả:** Thiết kế cấu trúc bộ nhớ đệm LRU (Least Recently Used) với dung lượng cố định. Hỗ trợ `get(key)` và `put(key, value)` trong O(1). Khi đầy, loại bỏ phần tử ít được dùng nhất.  
**Input:** 
