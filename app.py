import streamlit as st

# ページ設定
st.set_page_config(
    page_title="Intimacy & Narrative Research Generator",
    page_icon="🔍",
    layout="wide"
)

# カスタムCSS（見やすさの調整）
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
    }
    .highlight {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #00a8cc;
    }
</style>
""", unsafe_allow_html=True)

# --- サイドバー：入力エリア ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1995/1995515.png", width=50) # 任意のアイコン
    st.header("リサーチ条件設定")
    
    st.markdown("---")
    
    # 入力フォーム
    target_topic = st.text_input(
        "リサーチしたいテーマ・キーワード", 
        value="便量", 
        help="例：便量、睡眠の質、激辛食品、ソロキャンプ など"
    )
    
    target_benefit = st.text_input(
        "想定される便益（任意）", 
        value="美容や健康につながる", 
        help="例：美容や健康につながる、ストレス解消になる、自己肯定感が上がる"
    )
    
    target_region = st.selectbox(
        "対象エリア",
        ["全世界（Global）", "北米・欧州中心", "アジア中心", "日本国内のみ"],
        index=0
    )

    st.markdown("---")
    st.markdown("""
    **使い方のヒント:**
    1. テーマを入力します。
    2. 生成されたプロンプトをコピーします。
    3. Gemini (Deep Research推奨) に貼り付けて実行します。
    """)

# --- メインエリア：プロンプト生成 ---
st.markdown('<div class="main-header">Intimacy & Narrative リサーチ生成</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">消費者の感情と物語を紐解く、深堀りリサーチ用プロンプトを作成します。</div>', unsafe_allow_html=True)
st.divider()

# プロンプトのテンプレート構築
prompt_template = f"""
あなたは、消費者の深層心理と文化的な文脈を深く理解する「エキスパート・マーケティング・ストラテジスト」です。
以下のテーマについて、Deep Research機能を活用して徹底的な調査を行い、レポートを作成してください。

## 1. 調査テーマ
* **トピック:** {target_topic}
* **想定される文脈:** {target_benefit}
* **調査対象地域:** {target_region}

## 2. 成功事例の抽出条件（Success Criteria）
以下のいずれかに該当する事例をリストアップしてください。
* **Social Buzz:** SNS（TikTok, Instagram, X, Reddit等）で明らかにバズっている、または投稿数が急増した事例。
* **Market Growth:** そのテーマでの商品数が急増している、または市場が拡大している。
* **Media Exposure:** 主要メディアやトレンド情報誌で大きく取り上げられた。

## 3. 分析の最重要視点（Our Philosophy）
単なる「事実の羅列」は不要です。我々は消費者の感情（Intimacy）と物語（Narrative）を重視しています。
各事例に対し、以下の視点で深堀り分析を行ってください。

### A. Intimacy（親密性・感情の力学）
* その事例は、消費者のどのような「個人的な感情」「人に言えない悩み」「恥じらい」「優越感」に触れたのか？
* どのような「感情のスイッチ」が入ることで、行動変容（購買や投稿）が起きたのか？
* タブー視されていたものが解放されたのか？ それとも新たな快楽が発見されたのか？

### B. Narrative（物語・文脈）
* その商品は、どのような「ストーリー」として消費者に受け入れられたのか？
* 機能的な価値（例：健康になる）を超えて、消費者は自分自身の人生においてどのような「主人公」になれると感じたのか？
* そのトレンドが生まれた文化的背景や、社会的な文脈は何か？

## 4. アウトプット形式
以下の構成で出力してください。

1.  **エグゼクティブサマリー:** 全体のトレンド傾向と、共通して見られる「消費者の感情（Intimacy）」の考察。
2.  **成功事例リスト（5〜10選）:**
    * 事例名/ブランド名/ハッシュタグ
    * 国/地域
    * **【Intimacy分析】:** 消費者の心の動き（詳細に）
    * **【Narrative分析】:** 受け入れられた物語（詳細に）
    * 定量的成果（わかる範囲で）
3.  **マーケティング示唆:** この調査から得られる、次の企画へのヒント。

可能な限り具体的な出典や、実際のユーザーの声（口コミ等の雰囲気）も含めてください。
"""

# 画面表示
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📋 生成されたプロンプト")
    st.info("右上のコピーボタンを押して、Geminiに入力してください。")
    # codeブロックを使うと、自動的にコピーボタンが付与されます
    st.code(prompt_template, language="markdown")

with col2:
    st.markdown("### 💡 このツールの狙い")
    st.markdown("""
    <div class="highlight">
    <b>我々のビリーフ：</b><br>
    機能的な便益（スペック）だけでなく、
    <b>「Intimacy（感情）」</b>と
    <b>「Narrative（物語）」</b>
    こそが人を動かす。<br><br>
    このプロンプトは、Geminiに対して
    単なるデータ収集ではなく、
    <b>「感情の解釈」</b>を強制するように
    設計されています。
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔍 活用例")
    st.markdown(f"""
    * **{target_topic}** × 美容
    * **{target_topic}** × アプリ
    * **{target_topic}** × ガジェット
    """)