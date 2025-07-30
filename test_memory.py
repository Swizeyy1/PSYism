from memory import MemoryStore

def test_add_memory():
    store = MemoryStore()
    store.add_memory("Test event", "joy", 0.9)
    assert len(store.memories) == 1
