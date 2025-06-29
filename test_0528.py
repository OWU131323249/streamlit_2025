import streamlit as st

st.title("大学生活充実度チェッカー")

st.write("あなたの大学生活について教えてください。簡単なフィードバックをします。")

# --- 入力セクション ---
st.header("あなたの情報")

# 1. 学部 (st.selectbox)
# TODO: 学部を選択するselectboxを配置してください。
# options: ["文学部", "経済学部", "理工学部", "社会情報学部", "その他"]
faculty = st.selectbox(
    "あなたの学部を選んでください：",
    ["文学部", "経済学部", "理工学部", "社会情報学部", "その他"]
)
# 2. 週の平均勉強時間 (st.slider)
# TODO: 週の平均勉強時間を入力するsliderを配置してください。
# min_value=0, max_value=50, value=10, step=1
study_hours = st.slider(
    "週の平均勉強時間は？（時間）", 
    min_value=0, max_value=50, value=10, step=1
)

# 3. 所属しているサークル・部活動 (st.multiselect)
# TODO: 所属しているサークル・部活動を複数選択するmultiselectを配置してください。
# options: ["運動系サークル", "文化系サークル", "部活動", "特になし", "その他"]
activities = st.multiselect(
    "所属しているサークル・部活動を選んでください（複数可）：", 
    ["運動系サークル", "文化系サークル", "部活動", "特になし", "その他"]
)

# 4. 友人関係の満足度 (st.radio)
# TODO: 友人関係の満足度を選択するradioを配置してください。
# options: ["大変満足", "満足", "普通", "少し不満", "不満"]
social_satisfaction = st.radio(
    "友人関係の満足度は？",
    ["大変満足", "満足", "普通", "少し不満", "不満"]
)

# 5. 平均睡眠時間 (st.number_input)
# TODO: 平均睡眠時間を入力するnumber_inputを配置してください。
# min_value=0.0, max_value=12.0, value=7.0, step=0.5
sleep_hours = st.number_input(
    "1日の平均睡眠時間（時間）", 
    min_value=0.0, max_value=12.0, value=7.0, step=0.5
)



# --- 診断ロジックセクション ---
if st.button("診断する"):
    st.header("診断結果")
    
    if faculty and social_satisfaction and sleep_hours: # 簡単な入力チェック
        feedback = []
        
        # TODO: 勉強時間に基づくフィードバック
        # 例: if study_hours < 5: feedback.append("もう少し勉強時間を確保しましょう！")
        if study_hours < 5:
            feedback.append("もう少し勉強時間を確保しましょう！")
        elif study_hours > 30:
            feedback.append("勉強も大事ですが、休息も忘れずに！")
        
        # TODO: サークル活動に基づくフィードバック
        # 例: if "特になし" in activities and len(activities) == 1: feedback.append("何か新しい活動を始めてみては？")
        if "特になし" in activities and len(activities) == 1:
            feedback.append("何か新しい活動を始めてみては？")
        elif "運動系サークル" in activities and "文化系サークル" in activities:
            feedback.append("バランスよく活動できていますね！")
        
        # TODO: 友人関係の満足度に基づくフィードバック
        # 例: if social_satisfaction in ["少し不満", "不満"]: feedback.append("友人関係で悩みがあれば、相談できる人を探してみましょう。")
        if social_satisfaction in ["少し不満", "不満"]:
            feedback.append("友人関係で悩みがあれば、相談できる人を探してみましょう。")

        # TODO: 睡眠時間に基づくフィードバック
        # 例: if sleep_hours < 6.0: feedback.append("睡眠時間をしっかり確保することも大切です。")

        if not feedback:
            st.success("素晴らしい大学生活を送っているようですね！")
        else:
            for item in feedback:
                st.warning(item)
    else:
        st.error("すべての項目を入力・選択してください。")

st.write("---")
st.caption("これは演習用のサンプルアプリです。") 
