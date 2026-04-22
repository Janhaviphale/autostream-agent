from agent import detect_intent
from rag import get_pricing_info
from tools import mock_lead_capture

name = None
email = None
platform = None


print("AutoStream AI Agent Ready!")

while True:

    user_input = input("You: ")

    intent = detect_intent(user_input)

    if intent == "greeting":
        print("Agent: Hello! How can I help you today?")

    elif intent == "pricing":
        pricing = get_pricing_info()
        print("Agent: Here are our plans:")
        print(pricing)

    elif intent == "high_intent":

        print("Agent: Great! I'd love to help you get started.")
        
        if not name:
            name = input("Agent: What's your name? ")

        if not email:
            email = input("Agent: Your email? ")

        if not platform:
            platform = input("Agent: Which platform do you create content on? ")

        mock_lead_capture(name, email, platform)

        print("Agent: Thanks! Our team will contact you soon.")

    else:
        print("Agent: Can you tell me more?")
