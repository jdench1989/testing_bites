from lib.counter import Counter

def test_initial_count():
    counter = Counter()
    assert counter.count == 0

def test_add():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5

def test_report():
    counter = Counter()
    counter.add(3)
    assert counter.report() == "Counted to 3 so far."