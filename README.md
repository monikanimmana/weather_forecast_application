# 🌦️ Weather Forecast Web Application

A clean, responsive **Weather Forecast Web Application** built with **Django** that allows users to search for real‑time weather information of any city using the **OpenWeatherMap API**. The project follows best practices such as environment variables, API error handling, and a clear project structure, making it suitable for learning, showcasing, and further extension.

---

## 🚀 Features

* 🔍 Search weather by **city name**
* 🌡️ Displays **temperature (°C)**
* 💧 Shows **humidity level**
* 🌬️ Wind speed information
* ☁️ Weather condition description
* ❌ User‑friendly error handling for invalid or empty city input
* 🔐 Secure API key management using **.env** file

---

## 🛠️ Tech Stack

- 🐍 **Backend** – Python, Django  
- 🌐 **Frontend** – HTML, CSS (Django Templates)  
- ☁️ **API** – OpenWeatherMap API  
- 🔧 **Environment Management** – python-dotenv / os.getenv  
- 🗄️ **Database (optional)** – SQLite (default Django) or PostgreSQL  
- 🔧 **Version Control** – Git, GitHub

---

## 📂 Project Structure

```
Weather_Forecast_API/
│
├── Weather_Forecast/
│   ├── views.py
│   ├── urls.py
│   ├── settings.py
│   └── ...
│
├── templates/
│   ├── index.html
│   └── weather_report.html
│
├── .env.example
├── .gitignore
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/weather-forecast-project.git
cd weather-forecast-project
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
# source myenv/bin/activate  # macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install django requests python-dotenv
```

### 4️⃣ Configure environment variables

Create a `.env` file in the project root:

```env
WEATHER_API_KEY=your_openweathermap_api_key
```

> 🔒 **Note:** `.env` is ignored using `.gitignore` for security reasons.

---

## ▶️ Run the Application

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8080/
```

---

## 🧪 Usage

1. Enter a city name in the input field
2. Click **Get Weather**
3. View real‑time weather details

If an invalid city is entered, an error message will be displayed gracefully.

---

## 🔐 Security Best Practices

* API keys stored using **environment variables**
* `.env` file excluded from GitHub using `.gitignore`
* `.env.example` provided for easy setup

---

## 🌱 Future Enhancements

* 🌍 Country‑specific search
* 🖼️ Weather icons
* 📅 5‑day weather forecast
* 📱 Improved responsive UI
* 🚀 Deployment on Render / Railway / AWS

---

## 📚 What I Learned

Through this project, I gained hands-on experience with:

* 🔗 **Integrating third-party APIs** (OpenWeatherMap)
* 📡 Making HTTP requests using the `requests` library
* 🧠 Parsing and using **JSON responses** from APIs
* ⚠️ Handling API errors and invalid user input gracefully
* 🔐 Managing sensitive data securely using **environment variables (.env)**
* 🧩 Connecting backend logic with frontend templates in Django

This project strengthened my understanding of how real-world web applications communicate with external services.

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 👩‍💻 Author

**Monika**
Aspiring Python & Django Developer

* GitHub:** [https://github.com/monikanimmana](https://github.com/monikanimmana)
* LinkedIn:** (https://linkedin.com/in/monika-nimmana-0887652a4)

A clean, responsive **Weather Forecast Web Application** built with **Django** that allows users to search for real‑time weather information of any city using the **OpenWeatherMap API**. The project follows best practices such as environment variables, API error handling, and a clear project structure, making it suitable for learning, showcasing, and further extension.

---

## 🚀 Features

* 🔍 Search weather by **city name**
* 🌡️ Displays **temperature (°C)**
* 💧 Shows **humidity level**
* 🌬️ Wind speed information
* ☁️ Weather condition description
* ❌ User‑friendly error handling for invalid or empty city input
* 🔐 Secure API key management using **.env** file

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Django Templates)
* **API:** OpenWeatherMap API
* **Environment Management:** python-dotenv / os.getenv
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
Weather_Forecast_API/
│
├── Weather_Forecast/
│   ├── views.py
│   ├── urls.py
│   ├── settings.py
│   └── ...
│
├── templates/
│   ├── index.html
│   └── weather_report.html
│
├── .env.example
├── .gitignore
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/weather-forecast-project.git
cd weather-forecast-project
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
# source myenv/bin/activate  # macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install django requests python-dotenv
```

### 4️⃣ Configure environment variables

Create a `.env` file in the project root:

```env
WEATHER_API_KEY=your_openweathermap_api_key
```

> 🔒 **Note:** `.env` is ignored using `.gitignore` for security reasons.

---

## ▶️ Run the Application

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🧪 Usage

1. Enter a city name in the input field
2. Click **Get Weather**
3. View real‑time weather details

If an invalid city is entered, an error message will be displayed gracefully.

---

## 🔐 Security Best Practices

* API keys stored using **environment variables**
* `.env` file excluded from GitHub using `.gitignore`
* `.env.example` provided for easy setup

---

## 🌱 Future Enhancements

* 🌍 Country‑specific search
* 🖼️ Weather icons
* 📅 5‑day weather forecast
* 📱 Improved responsive UI
* 🚀 Deployment on Render / Railway / AWS

---

## 📚 What I Learned

Through this project, I gained hands-on experience with:

* 🔗 **Integrating third-party APIs** (OpenWeatherMap)
* 📡 Making HTTP requests using the `requests` library
* 🧠 Parsing and using **JSON responses** from APIs
* ⚠️ Handling API errors and invalid user input gracefully
* 🔐 Managing sensitive data securely using **environment variables (.env)**
* 🧩 Connecting backend logic with frontend templates in Django

This project strengthened my understanding of how real-world web applications communicate with external services.

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 👩‍💻 Author

**Monika**
Aspiring Python & Django Developer

* GitHub: [https://github.com/monikanimmana](https://github.com/monikanimmana)
* LinkedIn:www.linkedin.com/in/monika-nimmana-0887652a4


---

## ⭐ Acknowledgements

* OpenWeatherMap API
* Django Documentation
* Python Community

---

⭐ If you like this project, don’t forget to **star the repository**!


---

## ⭐ Acknowledgements

* OpenWeatherMap API
* Django Documentation
* Python Community

---

⭐ If you like this project, don’t forget to **star the repository**!




