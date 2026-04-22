def detect_intent(user_input):

    user_input = user_input.lower()

    # High intent keywords
    high_intent_keywords = [
        "sign up",
        "try",
        "interested",
        "buy",
        "want",
        "start",
        "subscribe",
        "use pro",
        "pro plan"
    ]

    # Pricing keywords
    pricing_keywords = [
        "price",
        "pricing",
        "cost",
        "plans"
    ]

    # Greeting keywords
    greeting_keywords = [
        "hi",
        "hello",
        "hey"
    ]

    # Check high intent FIRST
    for word in high_intent_keywords:
        if word in user_input:
            return "high_intent"

    # Check greeting
    for word in greeting_keywords:
        if word in user_input:
            return "greeting"

    # Check pricing
    for word in pricing_keywords:
        if word in user_input:
            return "pricing"

    return "general"
