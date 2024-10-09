# Hewlett Foundation Organizations with Multiple Grants Visualization Tool

## What the tool does
Our team needed a way to visualize organizations that receive more than one grant per year and to see how those funds were used by various programs. Due to limitations within out-of-the-box Salesforce reporting and dashboarding features, we needed an alternative way to process and visualize this data. This script ingests an export from a specific Salesforce report in CSV format, strips out any organizations that only received one grant, then creates a stacked vertical bar chart with matplotlib. 

![Screen Shot 2024-10-09 at 09 22 44](https://github.com/user-attachments/assets/0f4924dd-6aff-41af-80b6-bb4e8072b185)

## How to use the tool

1. Clone the repo inside a virtual environment
2. Run `pip install -r requirements.txt`
3. Export the data the format seen in `gms_export.csv`. The placeholder in this repo shows the columns that must be filled in. No live data is currently stored in this repo.
4. Run `python3 data_processor.py`
5. The preview image that matplotlib exports will be a `.png` file, but the file you want will be a `.pdf` saved into your main directory. 
