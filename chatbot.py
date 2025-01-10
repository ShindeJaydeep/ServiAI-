from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

# Define waiter-like responses with more questions
responses = {
    "menu": "Today's menu includes: Pasta, Pizza, Salad, and Soup. What would you like to order?",
    "order": "Sure! Please tell me what you'd like to order.",
    "bill": "Your total bill is $25. Would you like to pay now?",
    "thanks": "You're welcome! Have a great day!",
    "hello": "Hello! How can I assist you today?",
    "hours": "Our restaurant is open from 7 AM to 11 PM. How can I assist you further?",
    "reservation": "Would you like to make a reservation? Please provide the time and number of people.",
    "location": "We are located on the 2nd floor, near the elevator. Would you like directions?",
    "wifi": "Yes, we have free Wi-Fi. The network name is 'HotelWiFi' and the password is 'welcome123'.",
    "specials": "Today's specials are Grilled Salmon and Chicken Alfredo. Would you like to try them?",
    "vegetarian": "We have several vegetarian options, including the Veggie Pizza and the Garden Salad.",
    "allergies": "Please inform us of any allergies so we can adjust your order accordingly.",
    "drink": "Would you like to order a drink? We have soft drinks, juices, and coffee.",
    "open": "Yes, we are open. How can I assist you today?",
    "close": "Our restaurant closes at 11 PM. Would you like to make a reservation for later?",
}

@app.post("/chat")
async def chat(message: Message):
    user_message = message.message.lower()
    # Match user messages to predefined responses
    for keyword, response in responses.items():
        if keyword in user_message:
            return {"response": response}
    return {"response": "I'm sorry, I didn't understand that. Could you please rephrase?"}
