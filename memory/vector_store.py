class VectorStore:

    def __init__(self):
        self.store = {}

    def add(self, key, vector):
        self.store[key] = vector

    def get(self, key):
        return self.store.get(key)


if __name__ == "__main__":
    db = VectorStore()
    db.add("paper1",[1,2,3])
    print(db.get("paper1"))
