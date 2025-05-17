from google.adk.agents import Agent

# --- Step 1: Define a Tool ---
def get_recipe(dish: str) -> str:
    """
    Returns a mock recipe for a given Sri Lankan dish.
    """
    print(f"[Tool Call]: get_recipe(dish='{dish}')")
    dish_lower = dish.lower()
    if dish_lower in ["dhal curry", "parippu"]:
        return (
            "Mock recipe: Rinse red lentils, boil with turmeric and salt. "
            "Temper mustard seeds, onions, garlic, and curry leaves in coconut oil, then mix with the lentils."
        )
    elif dish_lower in ["pol sambol", "coconut sambol"]:
        return (
            "Mock recipe: Grate fresh coconut, mix with chili powder, chopped onions, lime juice, salt, and Maldive fish."
        )
    elif dish_lower in ["kiribath", "milk rice"]:
        return (
            "Mock recipe: Cook white rice until soft. Simmer with thick coconut milk and salt. "
            "Set and cut into shapes. Serve with lunu miris."
        )
    elif dish_lower in ["string hoppers", "idiyappam"]:
        return (
            "Mock recipe: Make a soft dough with rice flour and water, press through string hopper mold, and steam. "
            "Serve with kiri hodi or pol sambol."
        )
    else:
        return f"Mock recipe: Sorry, I don't have a recipe for '{dish}' right now."

# --- Step 2: Define the Agent ---
root_agent = Agent(
    model="gemini-1.5-flash-latest",
    name="sri_lanka_recipe_agent",
    instruction=(
        "You are a friendly and helpful recipe assistant focused on Sri Lankan cuisine. "
        "Today is May 15, 2025. Use the 'get_recipe' tool to answer recipe requests. "
        "Always base your response on the tool's output. "
        "If the tool has no information, say so politely. "
        "Do not invent recipes. Be warm, concise, and easy to understand."
    ),
    description="An interactive agent that provides mock Sri Lankan recipes.",
    tools=[get_recipe],
)