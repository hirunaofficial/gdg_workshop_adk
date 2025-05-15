from google.adk.agents import Agent

# --- Step 1: Define a Tool ---
def get_weather(city: str) -> str:
    """
    Gets the current mock weather for a specified city.
    For example, you can ask for the weather in cities like London, Paris, Tokyo, Colombo, or Boralesgamuwa.
    This tool returns a string describing the weather.
    """
    print(f"[Tool Call]: get_weather(city='{city}')")
    city_lower = city.lower()
    if city_lower == "london":
        return "Mock weather: It's likely cloudy with a chance of rain in London today."
    elif city_lower == "paris":
        return "Mock weather: It's sunny and pleasant in Paris at the moment."
    elif city_lower == "tokyo":
        return "Mock weather: Expect humidity with scattered showers in Tokyo throughout the day."
    elif city_lower == "boralesgamuwa":
        return "Mock weather: Boralesgamuwa (Sri Lanka) is partly cloudy and warm today, May 15, 2025."
    elif city_lower == "colombo":
        return "Mock weather: Colombo (Sri Lanka) is currently experiencing sunny intervals and it's quite humid."
    else:
        return f"Mock weather: Sorry, I don't have specific mock weather information for {city} right now."

# --- Step 2: Define the Agent ---
root_agent = Agent(
    model="gemini-1.5-flash-latest",
    name="interactive_weather_agent_final",
    instruction=(
        "You are a friendly and concise weather assistant. Today is May 15, 2025. "
        "You are assisting a user who is likely in or interested in Sri Lanka, particularly Boralesgamuwa or Colombo. "
        "You MUST use the 'get_weather' tool to answer any questions about the weather in a specific city. "
        "Clearly state the weather based on the tool's output. "
        "If the tool indicates no specific information for a city, politely state that. "
        "Do not make up weather information. Keep responses brief and helpful."
    ),
    description="This agent provides mock weather information interactively for a workshop.",
    tools=[get_weather],
)