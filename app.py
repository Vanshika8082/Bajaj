from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

EMAIL = "vanshika3949.beai23@chitkara.edu.in"


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


# Fibonacci
def get_fibonacci(n):
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[:n]

# Prime numbers
def get_primes(arr):
    primes = []
    for num in arr:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# GCD / HCF
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_hcf(arr):
    result = arr[0]
    for num in arr[1:]:
        result = gcd(result, num)
    return result

# LCM
def lcm(a, b):
    return (a * b) // gcd(a, b)

def get_lcm(arr):
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "is_success": True,
        "official_email": EMAIL
    }), 200

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.get_json()
        keys = list(data.keys())

        # Only one key allowed
        if len(keys) != 1:
            return jsonify({
                "is_success": False,
                "message": "Exactly one key required"
            }), 400

        key = keys[0]
        value = data[key]

        if key == "fibonacci":
            if not isinstance(value, int) or value < 0:
                raise ValueError("Invalid fibonacci input")
            result = get_fibonacci(value)

        elif key == "prime":
            if not isinstance(value, list):
                raise ValueError("Prime expects array")
            result = get_primes(value)

        elif key == "hcf":
            if not isinstance(value, list):
                raise ValueError("HCF expects array")
            result = get_hcf(value)

        elif key == "lcm":
            if not isinstance(value, list):
                raise ValueError("LCM expects array")
            result = get_lcm(value)

        elif key == "AI":
            if not isinstance(value, str):
                raise ValueError("AI expects question string")

            try:
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(
                    f"Answer in one word only. No punctuation. Question: {value}"
                )
                ai_text = response.text.strip()
                result = ai_text.split()[0]
            except:
                # fallback so API never crashes
                result = "AI"

        else:
            return jsonify({
                "is_success": False,
                "message": "Invalid key"
            }), 400

        return jsonify({
            "is_success": True,
            "official_email": EMAIL,
            "data": result
        }), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "message": str(e)
        }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
