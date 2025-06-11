from lib.grammar_stats import GrammarStats

def test_check_returns_true_when_text_fits_critera():
    checker = GrammarStats()
    assert checker.check("Testing first sentence.") == True
    assert checker.check("Testing second setence!") == True

def test_check_returns_false_when_text_does_not_fit_critera():
    checker = GrammarStats()
    assert checker.check("Testing first sentence") == False
    assert checker.check("Testing second setence-") == False
    assert checker.check("testing second setence-") == False  

def test_percentage_good_returns_correct_percentage():
    checker = GrammarStats()
    assert type(checker.percentage_good()) == int
    assert checker.percentage_good() == 0  
    checker.check("Testing first sentence.") # True
    checker.check("Testing second setence!") # True
    checker.check("testing third setence-")  # False
    checker.check("Testing fourth setence!") # True
    assert type(checker.percentage_good()) == int
    assert checker.percentage_good() == 75

