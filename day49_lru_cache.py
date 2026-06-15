LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache là {1=1}
lRUCache.put(2, 2); // cache là {1=1, 2=2}
lRUCache.get(1);    // trả về 1
lRUCache.put(3, 3); // vượt dung lượng, xóa key 2, cache là {1=1, 3=3}
lRUCache.get(2);    // trả về -1 (không tìm thấy)
