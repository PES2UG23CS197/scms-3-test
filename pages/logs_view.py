import streamlit as st
from db.queries import get_logs

st.title("📝 Logs Viewer")

# --- Logs Table ---
st.subheader("System Logs")

logs = get_logs()

if logs:
    log_table = []
    for log in logs:
        user_id, action = log
        log_table.append({
            "User ID": user_id,
            "Action": action
        })
    st.table(log_table)
else:
    st.info("No logs available.")

# --- Reset Button ---
st.subheader("🧹 Reset Simulation")
st.button("Reset All Data", help="This will clear all simulation data (functionality pending)")
