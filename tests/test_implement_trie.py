from src.implement_trie import Trie

def test_implement_trie():
    trie = Trie()
    
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    
    trie.insert("app")
    assert trie.search("app") == True
    
    assert trie.search("bat") == False
    assert trie.startsWith("b") == False
    
    trie.insert("bat")
    assert trie.search("bat") == True
    assert trie.startsWith("ba") == True
    
    trie.insert("apps")
    assert trie.search("apps") == True
    assert trie.search("appl") == False
    
    # Single letter
    trie.insert("a")
    assert trie.search("a") == True
    assert trie.startsWith("a") == True
    