import pandas as pd
import numpy as np

# 入力CSVファイルのパス
input_csv = "input.csv"

# 教科の対応付け
subject_map = {1: "国語", 2: "数学", 3: "理科", 4: "社会", 5: "英語"}

# 成績の対応付け
grade_map = {
    1: "A",
    2: "B",
    3: "B",
    4: "C",
    5: "C",
    6: "C",
    7: "C",
    8: "D",
    9: "D",
    10: "E",
}


# 判定のルール
def determine_result(average, below_30_count, below_10):
    if below_10:
        return "不合格"
    if below_30_count >= 3:
        return "再テスト"
    if average >= 60:
        return "合格"
    return "不合格"


# 入力CSVファイルを読み込む
df = pd.read_csv(input_csv, header=None, names=["名前", "教科", "点数"])

# 生徒ごとに処理を行う
students = df["名前"].unique()
for student in students:
    student_data = df[df["名前"] == student]

    # 教科ごとにデータを集計
    results = []
    for subject_id in range(1, 6):
        subject_data = student_data[student_data["教科"] == subject_id]
        scores = subject_data["点数"]

        # 平均点と成績の計算
        if not scores.empty:
            average = scores.mean()
            below_30_count = (scores <= 30).sum()
            below_10 = (scores < 10).any()
            rank = None

            # 教科ごとの成績を評価
            if average >= 0:
                results.append(
                    {
                        "教科": subject_map[subject_id],
                        "平均点": round(average, 1),
                        "成績": None,  # 後で順位を計算してから入れる
                        "判定": determine_result(average, below_30_count, below_10),
                    }
                )

    # 平均点で順位付け
    averages = [result["平均点"] for result in results]
    sorted_results = sorted(zip(results, averages), key=lambda x: x[1], reverse=True)

    for rank, (result, _) in enumerate(sorted_results, start=1):
        result["順位"] = rank
        result["成績"] = grade_map[rank]

    # 出力ファイルの作成
    output_filename = f"生徒{student[-1]}.csv"
    output_df = pd.DataFrame(
        [
            {
                "教科": result["教科"],
                "平均点": result["平均点"],
                "順位": result["順位"],
                "成績": result["成績"],
                "判定": result["判定"],
            }
            for result in results
        ]
    )

    # ヘッダーを追加してCSVに書き出し
    output_df.to_csv(
        output_filename, index=False, header=["教科", "平均点", "順位", "成績", "判定"]
    )

print("通知簿の出力が完了しました。")
