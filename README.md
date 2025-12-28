# Smart Manufacturing IoT‑Cloud Monitoring 

## 1. Project overview

This project implements a smart manufacturing monitoring dashboard using
historical IoT sensor data from multiple machines. The goal is to provide
a clear view of machine health, anomalies, and maintenance risk so that
plant operators can quickly identify problematic machines and reduce
unexpected downtime. The dashboard is built with Python and Streamlit and
runs locally in a web browser. [file:54]

## 2. Dataset description

The dataset represents time‑series sensor readings collected from several
manufacturing machines. Each row corresponds to a timestamped measurement
for a specific machine. The main columns are:

- `timestamp` – Date and time of the reading.
- `machine_id` – Unique ID of the machine.
- `temperature` – Machine temperature.
- `vibration` – Vibration level.
- `humidity` – Ambient humidity.
- `pressure` – System pressure.
- `energy_consumption` – Energy usage during that interval.
- `anomaly_flag` – 0 = normal operation, 1 = anomaly detected.
- `failure_type` – Type of failure or issue (Normal, Overheating, Vibration Issue, Pressure Drop, etc.).
- `predicted_remaining_life` – Estimated remaining useful life of the machine.
- `downtime_risk` – Continuous risk score related to possible downtime.
- `maintenance_required` – 0 = no maintenance, 1 = maintenance needed. [file:54]

These features are used to visualize machine behaviour, highlight anomaly
patterns, and support simple maintenance decisions in the dashboard. [file:54]

## 3. Tech stack

- Python 3.x
- Pandas – data loading and preprocessing
- Matplotlib – plotting time‑series sensor trends
- Streamlit – interactive web dashboard UI [file:54]

(Optional sections if used in your notebook:)

- scikit‑learn – experimentation with predictive models
- pickle – saving/loading trained models [file:54]

## 4. Features

### 4.1 Machine‑wise sensor monitoring

- Sidebar allows selection of a specific `machine_id`.
- For the selected machine, the dashboard plots a time‑series line chart
  of `temperature`, `vibration`, and `pressure` over the most recent
  readings.
- This helps identify abnormal spikes, trends, and outliers in machine
  behaviour. [file:54]

### 4.2 Recent health flags

- For the same machine, the dashboard shows a table containing the last
  few records with:
  - `timestamp`
  - `anomaly_flag`
  - `maintenance_required`
  - `downtime_risk`
- This provides a quick snapshot of the latest health status and risk
  for that machine. [file:54]

### 4.3 Overall anomaly summary

- The app aggregates data across all machines and computes the total
  number of anomalies per `machine_id` using the `anomaly_flag` column.
- A summary table displays the top machines with the highest anomaly
  counts, helping maintenance teams prioritise where to investigate
  first. [file:54]

### 4.4 Simple maintenance risk check (demo)

- The dashboard includes a “Simple maintenance risk check (demo)” section.
- The user can manually adjust:
  - Temperature
  - Vibration
  - Pressure
  using input widgets.
- A rule‑based scoring logic compares these values to high/low quantiles
  of the historical data and classifies the current situation as:
  - LOW risk – maintenance not urgent
  - MEDIUM risk – keep the machine under observation
  - HIGH risk – maintenance recommended
- This is a demonstration of decision support logic and can later be
  replaced by a machine‑learning model. [file:54]

## 5. Project structure

├── app.py # Streamlit dashboard
├── smart_manufacturing_data.csv # IoT manufacturing dataset
├── PROJECT.ipynb # Jupyter notebook for EDA / experiments
├── rf2_model.pkl # (optional) saved model
├── scaler.pkl # (optional) saved scaler
└── README.md # Project documentation



## 6. How to run the dashboard

1. Make sure Python 3.x is installed on your system.
2. Clone or download this repository and open a terminal inside the
   project folder.
3. Install the required packages:

4. Start the Streamlit app:


5. Open the local URL printed in the terminal (usually
`http://localhost:8501`) in your browser to use the dashboard. [file:54]

## 7. Possible future improvements

- Replace the rule‑based risk logic with a trained machine learning model
(e.g., RandomForest) that predicts `maintenance_required` from sensor
data.
- Integrate real‑time IoT streams via MQTT or HTTP instead of static CSV.
- Add authentication and role‑based access for different user types
(operators, engineers, managers).
- Deploy the Streamlit app to a cloud platform for remote access. [file:54]

### Optional ML artifacts

- `rf2_model.pkl`: Saved RandomForest model trained to predict `maintenance_required`
  from sensor data.
- `scaler.pkl`: Feature scaler used during model training.

These files are not yet integrated into the Streamlit app, but they show
that a predictive maintenance model was trained and can be loaded later
for real-time predictions.



## 8. Author

- Name: Abdul Musawir
- Program: BS IT / Computer Science
- University: [The Superior University Lahore]
- Email: [abdulmusawir8191456@gmail.com]

