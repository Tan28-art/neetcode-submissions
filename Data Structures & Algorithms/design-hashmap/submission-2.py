class MyHashMap:

    def __init__(self):
        # initialize the data structure
        self.hash_map = {}
        

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value
        

    def get(self, key: int) -> int:
        val = self.hash_map.get(key)
        return val if val is not None else -1

    def remove(self, key: int) -> None:
        if self.hash_map.get(key):
            del(self.hash_map[key])
        



# Your Myhash_map object will be instantiated and called as such:
# obj = Myhash_map()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)