# BFHL API – Bajaj Qualifier 1 (Chitkara University 2026)

This project implements two REST APIs as part of the Bajaj Qualifier assessment.

## Live API

Base URL:

```
https://bajaj-dgzw.onrender.com
```

### Endpoints

* `GET /health`
* `POST /bfhl`

---

## Tech Stack

* Python
* Flask
* Google Gemini API
* Gunicorn (for deployment)
* Render (hosting)

---

## API Details

### 1. Health Check

**Endpoint**

```
GET /health
```

**Response**

```json
{
  "is_success": true,
  "official_email": "vanshika3949.beai23@chitkara.edu.in"
}
```

---

### 2. Main API

**Endpoint**

```
POST /bfhl
```

Each request must contain exactly one of the following keys:

| Key         | Input           | Output                   |
| ----------- | --------------- | ------------------------ |
| `fibonacci` | Integer         | Fibonacci series         |
| `prime`     | Integer array   | Prime numbers from array |
| `lcm`       | Integer array   | LCM of numbers           |
| `hcf`       | Integer array   | HCF of numbers           |
| `AI`        | Question string | One-word AI response     |

---

## Request and Response Examples

### Fibonacci

**Request**

```json
{
  "fibonacci": 7
}
```

**Response**

```json
{
  "is_success": true,
  "official_email": "vanshika3949.beai23@chitkara.edu.in",
  "data": [0,1,1,2,3,5,8]
}
```

---

### Prime

**Request**

```json
{
  "prime": [2,4,7,9,11]
}
```

**Response**

```json
{
  "is_success": true,
  "official_email": "vanshika3949.beai23@chitkara.edu.in",
  "data": [2,7,11]
}
```

---

### LCM

**Request**

```json
{
  "lcm": [12,18,24]
}
```

**Response**

```json
{
  "is_success": true,
  "official_email": "vanshika3949.beai23@chitkara.edu.in",
  "data": 72
}
```

---

### HCF

**Request**

```json
{
  "hcf": [24,36,60]
}
```

**Response**

```json
{
  "is_success": true,
  "official_email": "vanshika3949.beai23@chitkara.edu.in",
  "data": 12
}
```

---

### AI Response

**Request**

```json
{
  "AI": "What is the capital city of Maharashtra?"
}
```

**Response**

```json
{
  "is_success": true,
  "official_email": "vanshika3949.beai23@chitkara.edu.in",
  "data": "Mumbai"
}
```

---

## Local Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bfhl-api.git
cd bfhl-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file

```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the server

```bash
python app.py
```

Server will run at:

```
http://localhost:3000
```

---

## Deployment

The API is deployed on **Render** using:

**Build Command**

```
pip install -r requirements.txt
```

**Start Command**

```
gunicorn app:app
```

---

## Evaluation Criteria Covered

* Correct HTTP status codes
* Strict response structure
* Input validation
* Graceful error handling
* Public API accessibility
* External AI API integration

---

## Author

**Vanshika**
Chitkara University
Email: [vanshika3949.beai23@chitkara.edu.in](mailto:vanshika3949.beai23@chitkara.edu.in)
