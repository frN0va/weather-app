# Weather App

This is a simple **Weather App** built using **Python** and **Tkinter** for the GUI. The app allows users to input a city name and get the current weather information for that city, including temperature, weather condition, and more. The app uses the **OpenWeatherMap API** to fetch weather data.

## Features

- **Search for weather** by city name.
- Display **temperature** in **Celsius**.
- Shows **weather condition** (e.g., clear, cloudy, rainy).
- Built with a **user-friendly graphical interface** using **Tkinter**.

## Requirements

To set up this project on your local machine, you'll need to have the following:

- Python 3.x
- `requests` library to make HTTP requests to the OpenWeatherMap API.
- `python-dotenv` library to load environment variables securely.
- OpenWeatherMap API key (free tier available).

## Setup Instructions

Follow these steps to set up the Weather App for yourself:

### 1. Clone the Repository

If you haven’t already cloned the repository, you can do so using:

```bash
git clone https://github.com/frn0va/weather-app
```

### 2. Install Dependencies

Before running the app, you need to install the required libraries. Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, if you're installing manually:

```bash
pip install requests python-dotenv
```

### 3. Get an OpenWeatherMap API Key

1. Go to [OpenWeatherMap](https://openweathermap.org/).
2. Sign up for a free account if you don’t already have one.
3. Once logged in, go to the **API Keys** section in your account settings.
4. Generate a new API key.

### 4. Add Your API Key

Create a `.env` file in the root of the project directory (same directory as `weather.py`) and add your API key in the following format:

```
API_KEY=your_valid_api_key_here
```

Make sure to replace `your_valid_api_key_here` with the actual API key you generated from OpenWeatherMap.

### 5. Run the Application

Once everything is set up, you can run the app by executing the following command:

```bash
python weather.py
```

This will launch the GUI window. Enter a city name, click "Get Weather," and see the weather details for that city!

### 6. Troubleshooting

- If you encounter a `401 Unauthorized` error, double-check your API key to ensure it's valid and has the correct permissions.
- If the city isn’t found, make sure the city name is correctly entered.
- If you receive an error related to missing dependencies, ensure all required libraries are installed by running the `pip install` commands.

## License

This project is open-source and available under the [MIT License](LICENSE)