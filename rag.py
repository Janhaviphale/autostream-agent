import json

def load_knowledge():
    with open("knowledge_base.json") as f:
        return json.load(f)


def get_pricing_info():
    data = load_knowledge()
    return data["pricing"]


def get_policy_info():
    data = load_knowledge()
    return data["policies"]
