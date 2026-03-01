# 🌦 Weather Forecast Web App  

A dynamic and responsive **Weather Forecast Application** built using **Python & Django**, integrating external APIs for **real-time weather data**, **Cloudinary for optimized media handling**, and **Unsplash API for dynamic background images**. The frontend is crafted using **modern HTML & CSS** for a sleek and engaging user experience.

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
- [📦 Deployment](#-deployment)  
- [🔮 Future Enhancements](#-future-enhancements)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  

---

## 🔎 Overview  

This project allows users to **fetch real-time weather data for any city worldwide**. It dynamically displays weather conditions with **beautiful background images based on the searched city**, making the application both **functional and visually appealing**.

The project demonstrates **full-stack development skills** including backend logic, API integration, UI/UX design, and deployment-ready architecture.

---

## ✨ Features  

- 🌍 **Real-time weather data** (temperature, humidity, wind speed, visibility, sunrise & sunset)  
- 🎨 **Dynamic background images** using Unsplash API  
- 📱 **Fully responsive design** (desktop, tablet & mobile)  
- ⚡ **Fast API-driven backend** using Django  
- ☁️ **Cloudinary integration** for optimized media handling  
- 🛡 **Error handling** for invalid city names and API failures  

---

## 🛠 Tech Stack  

| Category | Technologies |
|------------|----------------|
| **Backend** | Python, Django |
| **Frontend** | HTML5, CSS3 |
| **API Integration** | Weather API, Unsplash API |
| **Media Handling** | Cloudinary |
| **Database** | SQLite (Development) |
| **Version Control** | Git, GitHub |
| **Deployment** | Heroku / AWS / Render |

---

## 🏗 Architecture  

- **Django Backend** – Handles routing, API calls, business logic  
- **Weather API Integration** – Fetches real-time weather data  
- **Unsplash API** – Supplies high-quality dynamic background images  
- **Cloudinary** – Optimizes and manages media content  
- **Frontend (HTML + CSS)** – Displays weather data with responsive UI  

---

## 📸 Screenshots  

> Add screenshots here  

- Home Page  
- Weather Results  
- Mobile View  

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
