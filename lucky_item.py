import streamlit as st

st.title("ラッキーアイテム診断アプリ")
st.caption("星座を選んで、今日のラッキーアイテムを診断しましょう。")

st.markdown("---")
st.subheader("ラッキーアイテム診断")
st.write(" 星座を選ぶと、今日のラッキーアイテムとアドバイス、関連画像を表示するアプリを作成する。")

# 星座のリスト
constellations = [
    "おひつじ座 🐏", "おうし座 🐂", "ふたご座 ♊️", "かに座 🦀", 
    "しし座 🦁", "おとめ座 👧", "てんびん座 ⚖️", "さそり座 🦂", 
    "いて座 ♐️", "やぎ座  🐐", "みずがめ座 🏺", "うお座 ♓️"
]

# ラッキーアイテムとアドバイス、画像の辞書
lucky_items = {
    "おひつじ座 🐏": {"item": "赤いペン", "advice": "直感で動いてOK！", "image": "red_pen.png"},
    "おうし座 🐂": {"item": "観葉植物", "advice": "自然とのふれあいが吉。", "image": "plant.png"},
    "ふたご座 ♊️": {"item": "スマホスタンド", "advice": "効率化が運を呼ぶ！", "image": "phone_stand.png"},
    "かに座 🦀": {"item": "ジャスミンティー", "advice": "長い取り組みが一区切りつきそう", "image": "tea.png"},
    "しし座 🦁": {"item": "サングラス", "advice": "目立つ行動で運気UP！", "image": "sunglasses.png"},
    "おとめ座 👧": {"item": "手帳", "advice": "丁寧な計画が幸運を招く。", "image": "notebook.png"},
    "てんびん座 ⚖️": {"item": "ハンドクリーム", "advice": "手のケアで魅力UP。", "image": "hand_cream.png"},
    "さそり座 🦂": {"item": "香水", "advice": "香りで気分も運気も上昇。", "image": "perfume.png"},
    "いて座 ♐️": {"item": "スニーカー", "advice": "アクティブな行動が吉。", "image": "sneakers.png"},
    "やぎ座 🐐": {"item": "本", "advice": "知識の積み重ねが鍵。", "image": "book.png"},
    "みずがめ座 🏺": {"item": "イヤホン", "advice": "自分だけの世界を楽しもう。", "image": "earphones.png"},
    "うお座 ♓️": {"item": "アロマキャンドル", "advice": "癒しの時間を大切に。", "image": "aroma_candle.png"},
}

# 星座選択
selected_constellation = st.selectbox("あなたの星座を選んでください", constellations)

# 診断ボタン
if st.button("今日のラッキーアイテムを診断する！"):
    result = lucky_items.get(selected_constellation)
    if result:
        item = result["item"]
        advice = result["advice"]
        image_path = result["image"]

        st.subheader(f"{selected_constellation}のあなたの今日のラッキーアイテムは「{item}」です！")
        st.write("**アドバイス:**")
        st.info(advice)

  # 画像表示
        try:
            st.image(image_path, caption=f"{item}のイメージ", width=250)
        except FileNotFoundError:
            st.warning(f"画像ファイル ({image_path}) が見つかりません。")
            st.image("https://via.placeholder.com/250x250/CCCCCC/FFFFFF?Text=No+Image", caption="画像準備中")
        except Exception as e:
            st.error(f"画像表示中にエラーが発生しました: {e}")     
    
       

st.markdown("---")



