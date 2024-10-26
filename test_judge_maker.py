from judge_maker import make_judge


def test_make_judge_no1():
    """マトリックスNo1 ←テストを行うマトリックスの番号
    10点より下の点数がある場合 ←テストの内容
    """
    result = make_judge("A", [9, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 3
    result = make_judge("A", [11, 30, 15, 100, 100, 100, 100, 100, 100, 100])
    assert result == 2
    result = make_judge("A", [11, 15, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 1
    result = make_judge("D", [20, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 2
    result = make_judge("E", [20, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 3
