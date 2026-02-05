from src.lc75_search_suggestions_system import Solution

def test_lc75_search_suggestions_system():
    solution = Solution()
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    expected_output = [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]
    assert solution.suggestedProducts(products, searchWord) == expected_output