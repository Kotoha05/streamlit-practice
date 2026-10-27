import streamlit as st
import json
from pathlib import Path

from models.highlow import draw_cards, judge

st.title("High & Low Game")

json_path = Path(__file__).parent.parent / "sample_data" / "highlow.json"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

if "base_card" not in st.session_state:
    st.session_state.base_card, st.session_state.result_card = draw_cards()
    
base_card = st.session_state.base_card
result_card = st.session_state.result_card

st.write("次のカードは大きい？ 小さい？")

st.write("最初のカード")
st.header(
    f"{base_card['suit']} {base_card['rank']}"
)

#st.write("次のカード")
#st.header(
#    f"{result_card['suit']} {result_card['rank']}"
#)

if "choice" not in st.session_state:
    st.write("次のカードを予想してください")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("High", use_container_width = True):
            st.session_state.choice = "High"
            st.rerun()

    with col2:
        if st.button("Low", use_container_width = True):
            st.session_state.choice = "Low"
            st.rerun()

else:
    st.write("次のカード")
    st.header(f"{result_card["suit"]} {result_card["rank"]}")

    result = judge(
        base_card["rank"],
        result_card["rank"],
        st.session_state.choice
    )

    if result == "win":
        st.success("正解! You Win!")
    elif result == "lose":
        st.error("残念! You Lose!")
    elif result == "draw":
        st.info("引き分け! Draw!")

    if st.button("もう一度"):
        for key in ["choice", "base_card", "result"]:
            if key in st.session_state:
                del st.session_state[key]

        st.rerun()