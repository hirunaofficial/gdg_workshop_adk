# weather_agent_interactive_starter.py
# Date: May 15, 2025

# Imports from the Google ADK and Google Generative AI library
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types # For creating the message content
from datetime import datetime

# --- Configuration ---
APP_NAME = "weather_workshop_interactive_app_starter"
USER_ID = "interactive_user_starter"
SESSION_ID = "session_weather_interactive_starter" # Single session for this script run

# --- Step 1: Define a Tool ---
# TODO: Define 'get_weather(city: str) -> str' function with @tool decorator if ADK version requires,
# or as a plain function if not. Include a clear docstring.
# For this workshop, use mock weather data.
# Remember to add: print(f"[Tool Call]: get_weather(city='{city}')") for debugging.

# def get_weather(city: str) -> str:
#     """
#     Gets the current mock weather for a specified city. (e.g., London, Paris, Colombo, Boralesgamuwa)
#     Returns a string describing the weather.
#     """
#     # print(f"[Tool Call]: get_weather(city='{city}')")
#     # TODO: Implement mock logic
#     pass


# --- Step 2: Define the Agent ---
# TODO: Instantiate an Agent as 'weather_assistant_agent'.
# Parameters: model, name, instruction (mentioning the tool and context like date/location),
# description, tools (list containing your get_weather function).

# weather_assistant_agent = Agent(
#     model="gemini-1.5-flash-latest",
#     name="interactive_weather_agent_starter",
#     instruction="You are a helpful weather assistant for Boralesgamuwa, Sri Lanka. Today is May 15, 2025. Use your tool for weather queries.",
#     description="Provides mock weather information.",
#     tools=[] # Add get_weather here
# )

# --- Step 3: Set up Runner and Session Service ---
# TODO: Create InMemorySessionService instance.
# session_service = InMemorySessionService()

# TODO: Create Runner instance.
# runner = Runner(
#     agent=weather_assistant_agent,
#     app_name=APP_NAME,
#     session_service=session_service
# )

# --- Step 4: Run the Agent Interactively ---
if __name__ == "__main__":
    print("Interactive Weather Agent (ADK) - Starter Code")
    print(f"Date: May 15, 2025. Context: Boralesgamuwa, Sri Lanka.")
    print("Complete TODOs to make the agent functional.")
    print("-" * 30)

    # if 'runner' in globals() and 'session_service' in globals(): # Check if setup is done
        # --- Create Session ---
        # TODO: For InMemorySessionService, create the session for this script run.
        # try:
        #     session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
        #     print(f"Session '{SESSION_ID}' prepared for user '{USER_ID}'.")
        # except Exception as e:
        #     print(f"Warning: Could not create session '{SESSION_ID}' (may already exist or other error: {e}).")
        # print("-" * 30)

        # print("Ask about weather (e.g., 'Weather in Colombo?'). Type 'quit' or 'exit'.")
        # while True:
        #     try:
        #         query = input(f"[{datetime.now().strftime('%H:%M:%S')}] You: ")
        #     except KeyboardInterrupt: # Handle Ctrl+C
        #         print("\nExiting...")
        #         break
        #
        #     if query.lower() in ["quit", "exit"]:
        #         print("Exiting...")
        #         break
        #     if not query.strip():
        #         continue
        #
        #     # TODO: Create user_message_content = types.Content(...)
        #
        #     try:
        #         print("Agent is thinking...")
        #         # TODO: Call runner.run(...)
        #         # events = runner.run(...)
        #
        #         # TODO: Loop events, find event.is_final_response(), print text.
        #         # agent_responded = False
        #         # for event in events:
        #         #   if event.is_final_response():
        #         #       # ...
        #         #       agent_responded = True
        #         #       break
        #         # if not agent_responded:
        #         #   print("Agent: Did not provide a final text response.")
        #
        #     except Exception as e:
        #         print(f"Agent: Error during processing: {e}")
        #         # Optional: simple fallback to call your mock tool directly.
        #
        #     print("-" * 10)
    # else:
    #     print("Please complete Agent, Runner, and SessionService setup first!")

    print("\nWorkshop Tip: Ensure GOOGLE_API_KEY is set for LLM calls.")