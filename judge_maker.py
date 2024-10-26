def make_judge(grade, points):
    """
    判定を行う関数

    Args:
        grade (str): 成績 (A～Eの文字列)
        points (list): 点数 (0～100の数値の10個のリスト)

    Returns:
        int: 判定 (1: 合格, 2: 再テスト, 3: 不合格)
    """

    # 平均点を計算
    average_score = sum(points) / len(points)

    # 30点以下の成績をカウント
    count_below_30 = sum(1 for score in points if score <= 30)

    # 10点以下の成績があるか確認
    has_below_10 = any(score < 10 for score in points)

    # 成績による基本判定
    if count_below_30 >= 3:
        return 2  # 再テスト
    elif has_below_10:
        return 3  # 不合格

    # 成績の評価に基づく判定
    if grade in ["A", "B", "C"]:
        return 1  # 合格
    elif grade == "D":
        return 2  # 再テスト
    elif grade == "E":
        return 3  # 不合格

    return 3  # デフォルトで不合格を返す（エラー処理）
