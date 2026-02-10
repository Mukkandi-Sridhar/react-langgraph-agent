from langchain.tools import tool

@tool
def recommend_clothing(weather: str) -> str:
    weather = weather.lower()

    if any(w in weather for w in ["snow", "freezing"]):
        return "Wear a heavy coat, gloves, and boots."
    if "rain" in weather:
        return "Bring a raincoat and waterproof shoes."
    if any(w in weather for w in ["hot", "85"]):
        return "Wear light clothes and sunscreen."
    if any(w in weather for w in ["cold", "50"]):
        return "Wear a warm jacket."

    return "A light jacket should be fine."
