## The Weather Dataset

Here, The Weather Dataset is a time series data set with per hour information about the weather conditions at a particular location situated at Cork, Ireland at station Roches Point since 01/12/1955. It records Precipitation Amount(mm), Air Temperature(C), Wet Bulb Temperature (C), Dew Point Temperature, Vapour Pressure (hPa), Relative Humidity(%), Mean Sea Level Pressure(hPa), Mean Wind Speed(kt), Predominant Wind Direction(deg), and Indicator. I analyzed this data set with Pandas. 
###### Station Height: 40 Meters	
###### Latitude: 51.793 / Longitude: -8.244
###### Source data: www.met.ie (Met Éireann)

## Metadata

- **date**: Date and Time (UTC)
- **rain**: Precipitation Amount (mm)
- **temp**: Air Temperature (C)
- **wetb**: Wet Bulb Temperature (C)
- **dewpt**: Dew Point Temperature (C)
- **vappr**: Vapour Pressure (hPa)
- **rhum**: Relative Humidity (%)
- **msl**: Mean Sea Level Pressure (hPa)
- **wdsp**: Mean Wind Speed (kt)
- **wddir**: Predominant Wind Direction (deg)

## Project Structure
```
weather-analysis/
├── data/
│   ├── raw/                 # Raw data files
│   ├── processed/           # Processed data files
│   └── external/            # External datasets or data obtained from external sources
├── notebooks/               # Jupyter notebooks for data exploration, and analysis
├── src/                     # Source code
│   ├── data_preprocessing/  # Scripts or modules for data preprocessing
│   ├── feature_engineering/ # Scripts or modules for feature engineering
│   ├── modeling/            # Scripts or modules for modeling (machine learning models)
│   └── evaluation/          # Scripts for model evaluation and performance metrics
├── reports/                 # Reports generated(HTML, PDF) from analysis and modeling
├── models/                  # Saved models or model artifacts
├── environment.yml          # Conda environment file specifying dependencies
├── README.md                # README file describing the project and its components
└── requirements.txt         # Python dependencies file (alternative to environment.yml)
```

## Model Saving Script
I create a script within the modeling/ directory that defines the model, trains it, and then saves it to the /models folder. I execute the train_model.py script to train your model and save it. 
