# weather_agent_interactive_starter.py
# Date: May 15, 2025

# Imports from the Google ADK and Google Generative AI library
# TODO: Add necessary imports: Agent (if used directly, but likely not needed here), Runner, InMemorySessionService
# from google.adk.agents import Agent # Not needed if root_agent is fully configured
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types # For creating the message content
from datetime import datetime

# TODO: Import the root_agent from the weather_agent.agent module.
# This assumes you have a file structure like:
# your_project_directory/
# |-- weather_agent_interactive_starter.py
# |-- weather_agent/
#     |-- __init__.py (can be empty)
#     |-- agent.py    (this file would define 'root_agent' and its tools)
#
# from weather_agent.agent import root_agent


# --- Configuration ---
# TODO: Define APP_NAME, USER_ID, and SESSION_ID
# APP_NAME = "weather_workshop_interactive_app_starter"
# USER_ID = "interactive_user_starter"
# SESSION_ID = "session_weather_interactive_starter_v2"


# --- Step 1: Agent and Tool Definition (Assumed to be in weather_agent.agent) ---
# For this starter script, we assume 'root_agent' (an instance of google.adk.agents.Agent)
# is already defined with its tools (like get_weather) in 'weather_agent/agent.py'
# and will be imported above. You would need to create that agent.py file.
#
# Example content for weather_agent/agent.py (for workshop instructor's reference):
# --------------------------------------------------------------------------------
# from google.adk.agents import Agent
#
# def get_weather(city: str) -> str:
#     """
#     Gets the current mock weather for a specified city.
#     (e.g., London, Paris, Tokyo, Colombo, Boralesgamuwa)
#     Returns a string describing the weather.
#     """
#     print(f"[Tool Call in agent.py]: get_weather(city='{city}')")
#     city_lower = city.lower()
#     # ... (mock weather logic as in the completed script) ...
#     if city_lower == "colombo":
#         return "Mock weather from agent.py: Colombo is sunny."
#     else:
#         return f"Mock weather from agent.py: No data for {city}."

# root_agent = Agent(
#     model="gemini-1.5-flash-latest",
#     name="weather_root_agent_from_module",
#     instruction="You are a helpful weather assistant. Use your tools. Today is May 15, 2025. Context: Boralesgamuwa, Sri Lanka.",
#     description="Provides weather info, defined in a separate module.",
#     tools=[get_weather]
# )
# --------------------------------------------------------------------------------


# --- Step 2: Set up Runner and Session Service ---
# TODO: Create an instance of InMemorySessionService and assign it to 'session_service'.
# session_service = InMemorySessionService()


# TODO: Create an instance of Runner.
# - Pass the imported 'root_agent'.
# - Pass your defined APP_NAME.
# - Pass the 'session_service'.
# Assign it to 'runner'.

# runner = Runner(
#     agent=root_agent, # This should be the imported agent
#     app_name=APP_NAME,
#     session_service=session_service
# )


# --- Step 3: Run the Agent Interactively ---
if __name__ == "__main__":
    print("Interactive Weather Agent (ADK) - Starter Code (Modular Agent)")
    print(f"Date: May 15, 2025. Assistant Context: Boralesgamuwa, Sri Lanka.")
    print("TODO: Ensure 'root_agent' is imported and 'runner' is initialized.")
    print("-" * 30)

    # First, check if essential variables like 'runner' and 'session_service' have been defined.
    # This helps participants catch setup issues early.
    # if 'runner' not in globals() or 'session_service' not in globals() or 'root_agent' not in globals():
    #     print("CRITICAL: 'runner', 'session_service', or 'root_agent' is not defined. Please complete the setup steps.")
    #     print("Ensure 'root_agent' is imported from 'weather_agent.agent'.")
    #     exit()

    # --- Create the Session for this run ---
    # TODO: Implement the session creation logic as in the completed script:
    # - Use a try-except block.
    # - Attempt to session_service.create_session(...)
    # - Catch a general Exception if creation fails and print a message.
    # - Print confirmation that the session is prepared.
    # try:
    #     session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    #     print(f"Session '{SESSION_ID}' created successfully for user '{USER_ID}'.")
    # except Exception as e:
    #     print(f"Session '{SESSION_ID}' may already exist or an error occurred during creation: {e}. Assuming usable.")
    # print(f"Session '{SESSION_ID}' is prepared.")
    # print("-" * 30)


    # print("Ask about the weather (e.g., 'Weather in Colombo?'). Type 'quit' or 'exit' to stop.")
    # while True:
    #     try:
    #         query = input(f"[{datetime.now().strftime('%H:%M:%S')}] You: ")
    #     except KeyboardInterrupt:
    #         print("\nExiting agent by user interrupt...")
    #         break
    #
    #     if query.lower() in ["quit", "exit"]:
    #         print("Exiting agent...")
    #         break
    #     if not query.strip():
    #         continue
    #
    #     # TODO: Create user_message_content using types.Content and the user's query.
    #     # user_message_content = types.Content(role='user', parts=[types.Part(text=query)])
    #
    #     try:
    #         print("Agent is thinking...")
    #         # TODO: Call runner.run() using USER_ID, SESSION_ID, and user_message_content.
    #         # Store the result in 'events'.
    #         # events = runner.run(...)
    #
    #         # TODO: Loop through 'events' to find the final response.
    #         # - Check if event.is_final_response().
    #         # - If true, extract text from event.content.parts[0].text.
    #         # - Print the agent's response.
    #         # - Set a flag 'agent_responded = True' and break the loop.
    #         # agent_responded = False
    #         # for event in events:
    #         #     if event.is_final_response():
    #         #         # ... (extract and print)
    #         #         agent_responded = True
    #         #         break
    #
    #         # TODO: After the loop, if not agent_responded, print a message indicating no final response.
    #         # if not agent_responded:
    #         #     print("Agent: Did not provide a final text response.")
    #
    #     except ValueError as ve:
    #         # TODO: Catch ValueError specifically (could be session issues from runner)
    #         # Print a message including str(ve).
    #         # If "Session not found" in str(ve), add a specific hint.
    #         pass
    #     except Exception as e:
    #         # TODO: Catch other general exceptions during agent processing.
    #         # Print a generic error message including str(e).
    #         # Optionally, guide the user to add the simplified fallback for calling the mock tool directly.
    #         pass
    #     print("-" * 10)
    #
    # print("\nInteractive session ended.")