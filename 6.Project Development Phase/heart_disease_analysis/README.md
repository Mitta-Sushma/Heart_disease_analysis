# ❤️ Heart Disease Analysis Web Application

## Abstract  
Heart disease is one of the leading causes of health complications worldwide. Early detection and risk assessment play a vital role in prevention and timely treatment. This project, **Heart Disease Analysis Web Application**, is a Flask-based web system developed to analyze basic cardiovascular health parameters and estimate a user's heart disease risk level. The application provides user authentication, a heart-themed user interface, and a rule-based risk evaluation mechanism. This project is intended for academic and learning purposes and demonstrates full-stack web development using Python and Flask.

---

## Introduction  
The increasing prevalence of heart-related illnesses has created a need for simple and accessible health assessment tools. This web application allows users to input essential health parameters and instantly receive an estimated risk level. The system uses predefined medical thresholds to calculate a risk score and categorize users into Low, Medium, or High risk groups. The application includes login and sign-up functionality, ensuring controlled access to the analysis module.

---

## Objectives  
- To design a simple and user-friendly heart disease analysis system  
- To implement user login and registration functionality  
- To collect basic heart health parameters from users  
- To calculate heart disease risk using rule-based logic  
- To display results in an intuitive and visually appealing format  

---

## Scope of the Project  
This project is suitable for educational demonstrations, mini projects, and learning Flask web development. It does not replace professional medical diagnosis and is not intended for real-world clinical use.

---

## System Architecture  
The application follows a client–server architecture. The frontend is built using HTML and CSS, while the backend is developed using Python Flask. Static assets such as images are managed using Flask’s static folder. User requests are processed by Flask routes, which render appropriate HTML templates.

---

## Technologies Used  
- **Python 3** – Backend programming language  
- **Flask** – Web framework  
- **HTML5** – Structure of web pages  
- **CSS3** – Styling and layout  
- **Static Image Assets** – UI enhancement  

---

## Project Structure  
HeartDiseaseAnalysis/
├── app.py
├── templates/
│ ├── login.html
│ ├── signup.html
│ ├── index.html
│ └── result.html
├── static/
│ └── heart.jpg
└── README.md

---

## Functional Description  

### User Authentication  
The application allows any user to register using an email and password. Registered users can log in to access the heart disease analysis page. User data is stored temporarily in memory.

### Heart Disease Analysis  
Users enter health details such as age, blood pressure, cholesterol, heart rate, and oldpeak value. The system evaluates each parameter against predefined thresholds and calculates a cumulative risk score.

### Result Generation  
Based on the total score, the system categorizes the user into Low, Medium, or High risk and displays the result clearly on the result page.

---

## Risk Calculation Logic  

| Parameter | Condition | Score |
|---------|-----------|-------|
| Age | Greater than 50 | +10 |
| Blood Pressure | Greater than 130 | +10 |
| Cholesterol | Greater than 200 | +10 |
| Heart Rate | Less than 140 | +5 |
| Oldpeak | Greater than 2 | +10 |

### Risk Classification  
- **Score ≤ 20** → Low Risk  
- **Score 21–40** → Medium Risk  
- **Score > 40** → High Risk  

---

## User Interface Design  
The application uses a heart-themed static background image across all pages. Semi-transparent content boxes are used to maintain readability. The interface is designed to be simple, clean, and suitable for medical-related applications.

---

## Installation and Execution  

1. Install Python (version 3.7 or above)  
2. Install Flask using the command:  

---

## Sample Test Case  

**Input:**  
- Age: 55  
- Blood Pressure: 140  
- Cholesterol: 230  
- Heart Rate: 120  
- Oldpeak: 2.5  

**Output:**  
- Risk Score: 45  
- Risk Level: High  

---

## Limitations  
- No database integration  
- Passwords are stored in plain text  
- Uses rule-based logic instead of machine learning  
- Not suitable for real medical diagnosis  

---

## Future Enhancements  
- Database integration (MySQL / SQLite)  
- Secure password hashing  
- Machine learning-based prediction  
- Improved UI using Bootstrap  
- Graphical data visualization  

---

## Applications  
- Academic mini project  
- Flask learning project  
- Health analytics demonstration  
- College project submission  

---

## Conclusion  
The Heart Disease Analysis Web Application successfully demonstrates a basic health risk evaluation system using Flask. It integrates frontend and backend components efficiently and provides instant feedback to users. This project serves as a strong foundation for further enhancements such as machine learning integration and database connectivity.

---

## Disclaimer  
This application is developed strictly for educational purposes. It does not provide medical advice and should not be used as a substitute for professional healthcare diagnosis.

---

## Author  
Developed as part of an academic project.

---

❤️ **“Your heart matters – take care of it.”**
