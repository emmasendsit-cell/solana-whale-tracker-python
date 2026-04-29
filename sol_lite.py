import requests
import time

# LITE VERSION - Console Only
# Upgrade to Pro on Ko-fi for Discord Webhooks & Lofi-UI
TARGET_WALLET = "ENTER_WALLET_ADDRESS_HERE"
RPC_URL = "https://api.mainnet-beta.solana.com"

def check_movement():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSignaturesForAddress",
        "params": [TARGET_WALLET, {"limit": 1}]
    }
    try:
        response = requests.post(RPC_URL, json=payload).json()
        return response['result'][0]['signature']
    except:
        return None

print(f"--- Monitoring {TARGET_WALLET[:8]}... (Lite Version) ---")
last_sig = check_movement()

while True:
    current_sig = check_movement()
    if current_sig and current_sig != last_sig:
        print(f"🟢 Movement Detected! TX: {current_sig}")
        print("Upgrade to PRO for instant Discord/Mobile alerts.")
        last_sig = current_sig
    time.sleep(60) # Slow polling for Lite version