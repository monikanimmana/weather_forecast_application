# 🌦 Weather Forecast Application  

A dynamic and responsive **Weather Forecast Application** built using **Python & Django**, integrating external APIs for **real-time weather data** and **Unsplash API for dynamic background images**. The frontend is crafted using **modern HTML & CSS** for a sleek and engaging user experience.

---

## 📑 Table of Contents  

- [🔎 Overview](#-overview)  
- [✨ Features](#-features)  
- [🛠 Tech Stack](#-tech-stack)  
- [🏗 Architecture](#-architecture)  
- [📸 Screenshots](#-screenshots)  
- [⚙️ Installation](#️-installation)  
- [🚀 Usage](#-usage)  
- [🌐 API Integration](#-api-integration)   
- [🔮 Future Enhancements](#-future-enhancements)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  

---

## 🔎 Overview  

This project allows users to **fetch real-time weather data for any city worldwide**. It dynamically displays weather conditions with **beautiful background images based on the searched city**, making the application both **functional and visually appealing**.

The project demonstrates **full-stack development skills** including backend logic, API integration, UI/UX design, and deployment-ready architecture.

---

## ✨ Features  

- 🌍 **Real-time weather data using OpenWeather API**  
- 🌤 **OpenWeather API integration for accurate live weather updates**  
- 🎨 **Dynamic background images using Unsplash API**  
- 📱 **Fully responsive design (desktop, tablet & mobile)**  
- ⚡ **Fast API-driven backend using Django**  
- 🛡 **Error handling for invalid city names and API failures**   

---

## 🛠 Tech Stack  

| Category | Technologies |
|------------|----------------|
| **Backend** | Python, Django |
| **Frontend** | HTML5, CSS3 |
| **API Integration** | openweatherapi , Unsplash API |
| **Database** | SQLite (Development) |
| **Version Control** | GitHub |

---

## 🏗 Architecture  

- **Django Backend** – Handles routing, API calls, business logic  
- **Weather API Integration** – Fetches real-time weather data  
- **Unsplash API** – Supplies high-quality dynamic background images  
- **Frontend (HTML + CSS)** – Displays weather data with responsive UI  

---

## 📸 Screenshots  

<img width="960" height="532" alt="image" src="https://github.com/user-attachments/assets/b25ac4bf-e249-4539-a74b-a41f601aaea1" />
<img width="947" height="538" alt="image" src="https://github.com/user-attachments/assets/736a853c-6003-4b04-a3f0-4cda989c99e9" />

---

## ⚙️ Installation  

```bash
# Clone the repository
git clone https://github.com/yourusername/weather-forecast-app.git

# Navigate into project directory
cd weather-forecast-app

# Create virtual environment
python -m venv myenv

# Activate virtual environment
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

```
## 🚀 Usage  

- Open your browser and visit:  
  **http://127.0.0.1:8080/**  
- Enter any **city name**  
- View **real-time weather information with dynamic background images**  

---

## 🌐 API Integration  

### 🌤 OpenWeather API  

Provides:  
- Temperature  
- Humidity  
- Wind Speed  
- Visibility  
- Sunrise & Sunset  

### 🖼 Unsplash API  

Provides:  
- High-quality dynamic city-based images  

### 🔑 API Keys Setup  

Create a `.env` file in the root directory:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
UNSPLASH_API_KEY=your_unsplash_api_key
```

## 🔮 Future Enhancements  

- 📆 **7-day & hourly weather forecast**  
- 👤 **User authentication system**  
- 🌙 **Dark / Light mode toggle**  
- 🌎 **Multi-language support**  
- 📊 **Weather analytics dashboard**  

---

## 🤝 Contributing  

Contributions are welcome! 🎉  

### Steps to Contribute  

```bash
# Fork the repository

# Create a new branch
git checkout -b feature/your-feature

# Commit your changes
git commit -m "Added new feature"

# Push your branch
git push origin feature/your-feature

```
## 📜 License  

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

