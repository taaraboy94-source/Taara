from fastapi import FastAPI
import secrets
import time

app = FastAPI()

# Generator-ka Key-ga oo si gaar ah u shaqaynaya
def generate_unique_key():
    random_str = secrets.token_urlsafe(64)
    timestamp = str(int(time.time()))
    return f"SOM-{timestamp}-{random_str}"

@app.get("/generate-new-key")
def get_key():
    new_key = generate_unique_key()
    # Waxaad u soo celinaysaa qofka Key-ga cusub
    return {
        "status": "success", 
        "api_key": new_key, 
        "message": "Key-gaan waa mid kuu gaar ah."
    }

@app.get("/")
def home():
    return {"message": "API-gaagu wuu shaqaynayaa!"}
