# NETWORK-SPEED-TEST-TOOL

GROUP NAME:CAPSTONE TEAM-1

GROUP MEMBERSS: 

1.PRIYADHARSSHINI V
2.SHAFEEKHA FATHIMA
3.AKSHIYA
4.HARINI
5.SANJANA
6.RAVEENA

DESCRIPTION OF THE PROJECT:

Network Speed Test & Analysis
This project is a Network Speed Tester that measures Download Speed, Upload Speed, and Ping over time and visualizes the results using a line chart.

Features:
Measures Network Speed using the speedtest library.

Real-time Monitoring: Runs multiple tests at intervals.

Graphical Representation: Uses matplotlib to plot network speed trends.

Time-Based Logging: Captures speed variations at different timestamps.

Tech Stack:
Python

speedtest-cli (for network speed testing)

matplotlib (for visualization)

time (for scheduling tests)

How It Works:
The script runs 10 consecutive speed tests with a 1-second delay between each.

It records:

Download Speed (Mbps)

Upload Speed (Mbps)

Ping (ms)

Data is plotted on a graph to visualize performance over time.
Ensure you have the required dependencies:

!pip install speedtest-cli matplotlib

Running the Script:

python speed_test.py
This will execute the test and display a real-time performance graph.

OUTPUT:
![Image](https://github.com/user-attachments/assets/22933560-b5c0-43ea-85fd-17c1bd94161a)
