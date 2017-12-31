from open990.interpreter import steps

def test_return_one():
    assert 1 == steps.return_one()