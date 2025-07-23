import streamlit as st
from web3 import Web3

st.set_page_config(page_title="GBTNetwork L1", page_icon="🪙", layout="centered")

st.image("https://raw.githubusercontent.com/openai-user-assist/GBTNetworkAssets/main/logo.png", width=160)

st.title("GBTNetwork Layer 1 Node Interface")
rpc_url = "https://GBTNetwork"
web3 = Web3(Web3.HTTPProvider(rpc_url))

if web3.is_connected():
    st.success(f"Connected to GBTNetwork at {rpc_url}")
    st.write(f"Latest Block: {web3.eth.block_number}")
else:
    st.error("Failed to connect to GBTNetwork.")
