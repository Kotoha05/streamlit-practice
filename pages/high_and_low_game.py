import streamlit as st
import json
from pathlib import Path

json_path = Path(__file__).parent.parent / "sample_data" / "highlow.json"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

base_card = data["base_card"]
result_card = data["result_card"]

st.title("High & Low Game")
st.write("次のカードは大きい？ 小さい？")

st.write("最初のカード")
st.header(
    f"{base_card['suit']} {base_card['rank']}"
)

st.write("次のカード")
st.header(
    f"{result_card['suit']} {result_card['rank']}"
)
