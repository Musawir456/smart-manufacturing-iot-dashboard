import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data load
df = pd.read_csv("smart_manufacturing_data.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

st.title("Smart Manufacturing IoT-Cloud Monitoring")

# --- Machine filter (sidebar) ---
machine_ids = sorted(df['machine_id'].unique())
selected_machine = st.sidebar.selectbox("Select Machine ID", machine_ids)

machine_data = df[df['machine_id'] == selected_machine].sort_values('timestamp')

# --- Line graph for sensors ---
st.subheader(f"Recent sensor trends - Machine {selected_machine}")

fig, ax = plt.subplots(figsize=(10,4))
machine_data.set_index('timestamp')[['temperature','vibration','pressure']].tail(200).plot(ax=ax)
st.pyplot(fig)

# --- Recent health flags table ---
st.subheader("Recent health flags")
st.write(
    machine_data[['timestamp','anomaly_flag','maintenance_required','downtime_risk']].tail(10)
)


# --- Recent health flags table ---
st.subheader("Recent health flags")
st.write(
    machine_data[['timestamp','anomaly_flag','maintenance_required','downtime_risk']].tail(10)
)



st.subheader("Overall anomaly summary (top 10 machines)")

anomaly_summary = (
    df.groupby('machine_id')['anomaly_flag']
      .sum()
      .reset_index()
      .sort_values('anomaly_flag', ascending=False)
)

st.write(anomaly_summary.head(10))



st.subheader("Simple maintenance risk check (demo)")

st.markdown("Adjust sensor values and see risk estimation (rule-based demo).")

col1, col2, col3 = st.columns(3)
with col1:
    temp_in = st.number_input("Temperature", float(machine_data['temperature'].min()), 
                              float(machine_data['temperature'].max()), 
                              float(machine_data['temperature'].mean()))
with col2:
    vib_in = st.number_input("Vibration", float(machine_data['vibration'].min()), 
                             float(machine_data['vibration'].max()), 
                             float(machine_data['vibration'].mean()))
with col3:
    pres_in = st.number_input("Pressure", float(machine_data['pressure'].min()), 
                              float(machine_data['pressure'].max()), 
                              float(machine_data['pressure'].mean()))




if st.button("Check maintenance risk"):
    risk_score = 0

    if temp_in > machine_data['temperature'].quantile(0.9):
        risk_score += 1
    if vib_in > machine_data['vibration'].quantile(0.9):
        risk_score += 1
    if pres_in < machine_data['pressure'].quantile(0.1):
        risk_score += 1

    if risk_score == 0:
        st.success("Risk LOW – maintenance not urgently required (demo logic).")
    elif risk_score == 1:
        st.warning("Risk MEDIUM – observe this machine closely (demo logic).")
    else:
        st.error("Risk HIGH – maintenance recommended (demo logic).")
