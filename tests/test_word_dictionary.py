from src.word_dictionary import WordDictionary

def test_word_dictionary():
    wd = WordDictionary()

    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    
    # assert wd.search("pad") == False
    # assert wd.search("bad") == True
    # assert wd.search(".ad") == True
    # assert wd.search("b..") == True

    wd.addWord("a")
    wd.addWord("a")
    assert wd.search(".") == True
    assert wd.search("a") == True
    assert wd.search("aa") == False
    assert wd.search("a.") == False
    assert wd.search(".a") == False

    # Empty dictionary
    wd2 = WordDictionary()
    assert wd2.search("") == False
    assert wd2.search(".") == False

    # Long word with dots
    wd.addWord("apple")
    assert wd.search("a..le") == True
    assert wd.search("app.e") == True
    assert wd.search(".....") == True
    assert wd.search("a.p.e") == True