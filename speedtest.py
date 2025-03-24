!pip install speedtest-cli 
import speedtest
import matplotlib.pyplot as plt
import time

# Function to test network speed
def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = round(st.download() / 1_000_000, 2)  # Convert to Mbps
    upload_speed = round(st.upload() / 1_000_000, 2)  # Convert to Mbps
    ping_speed = round(st.results.ping, 2)

    return download_speed, upload_speed, ping_speed

# Collect data over time
download_speeds, upload_speeds, pings, timestamps = [], [], [], []

for _ in range(10):  # Test 10 times
    d, u, p = test_speed()
    timestamps.append(time.strftime("%H:%M:%S"))
    download_speeds.append(d)
    upload_speeds.append(u)
    pings.append(p)
    time.sleep(1)  # Delay

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(timestamps, download_speeds, label="Download (Mbps)", marker="o", color="blue")
plt.plot(timestamps, upload_speeds, label="Upload (Mbps)", marker="s", color="green")
plt.plot(timestamps, pings, label="Ping (ms)", marker="^", color="red")
plt.xlabel("Time")
plt.ylabel("Speed (Mbps) / Ping (ms)")
plt.title("Network Speed Test")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
