from lib. gratitudes import *

def test_Gratitudes_intiial_construct():
    grat = Gratitudes()
    assert grat.gratitudes == []

def test_Gratitudes_add_single():
    grat = Gratitudes()
    grat.add("the weather")
    assert grat.gratitudes == ["the weather"]

def test_Gratitudes_add_multiple():
    grat = Gratitudes()
    grat.add("the weather")
    grat.add("happiness")
    assert grat.gratitudes == ["the weather", "happiness"]

def test_Gratitudes_format():
    grat = Gratitudes()
    grat.add("the weather")
    grat.add("happiness")
    result = grat.format()
    assert result == "Be grateful for: the weather, happiness"