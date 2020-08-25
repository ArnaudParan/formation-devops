from compare import damereau_levenstein

def test_damereau_levenstein():
    assert damereau_levenstein('hello', 'hello') == 0
    assert damereau_levenstein('hello', 'hlelo') == 1
    assert damereau_levenstein('blabla', 'blibli') == 2
    assert damereau_levenstein('test', 'tast') == 1
