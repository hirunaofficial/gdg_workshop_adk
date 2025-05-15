# weather_agent_interactive_completed.py
# Date: May 15, 2025

# Imports from the Google ADK and Google Generative AI library
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types # For creating the message content
from datetime import datetime

from weather_agent.agent import root_agent

# --- Configuration ---
APP_NAME = "weather_workshop_interactive_app_completed"
USER_ID = "interactive_user_completed"
SESSION_ID = "session_weather_interactive_v2" # Unique session ID for this script run


# --- Step 3: Set up Runner and Session Service ---
session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)

# --- Step 4: Run the Agent Interactively ---
if __name__ == "__main__":
    print("Interactive Weather Agent (ADK) - Completed Code")
    print(f"Date: May 15, 2025. Assistant Context: Boralesgamuwa, Sri Lanka.")
    print("Ask about the weather (e.g., 'Weather in Colombo?'). Type 'quit' or 'exit' to stop.")
    print("-" * 30)
    print("Note: LLM responses require proper Google Cloud/API setup (e.g., GOOGLE_API_KEY).")
    print("-" * 30)

    # --- Create the Session for this run ---
    # For InMemorySessionService, we create the session when the script starts.
    # If create_session raises an error because it already exists (e.g., if this code
    # was part of a larger app where it might be called multiple times with the same IDs
    # on the same service instance), this try-except would catch it.
    # For a simple script run, this will typically just create it.
    try:
        session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
        print(f"Session '{SESSION_ID}' created successfully for user '{USER_ID}'.")
    except Exception as e:
        # This might happen if, for some reason, create_session fails (e.g., ADK internal state).
        # Or if it's called on a session_id that the InMemoryService instance thinks already exists
        # and doesn't allow re-creation (behavior can vary by ADK version).
        # In most simple InMemory cases for a script, this means the session should be considered usable.
        print(f"Session '{SESSION_ID}' may already exist or an error occurred during creation: {e}. Assuming usable.")
    print(f"Session '{SESSION_ID}' is prepared.")
    print("-" * 30)


    while True:
        try:
            query = input(f"[{datetime.now().strftime('%H:%M:%S')}] You: ")
        except KeyboardInterrupt:
            print("\nExiting agent by user interrupt...")
            break

        if query.lower() in ["quit", "exit"]:
            print("Exiting agent...")
            break
        if not query.strip():
            continue

        user_message_content = types.Content(role='user', parts=[types.Part(text=query)])

        try:
            print("Agent is thinking...")
            events = runner.run(
                user_id=USER_ID,
                session_id=SESSION_ID, # Use the same session for the interactive conversation
                new_message=user_message_content
            )

            agent_responded = False
            for event in events:
                if event.is_final_response():
                    if event.content and event.content.parts:
                        final_response_text = event.content.parts[0].text
                        print(f"Agent: {final_response_text}")
                        agent_responded = True
                    else:
                        print("Agent: Received a final response event, but it had no text content.")
                    break # Got the final response

            if not agent_responded:
                print("Agent: Did not provide a final text response. (The LLM might have used a tool without a follow-up, or an issue occurred).")

        except ValueError as ve: # Specifically catch ValueErrors which might include session issues from runner
             print(f"Agent: A ValueError occurred: {ve}")
             if "Session not found" in str(ve):
                 print("       This indicates the session was not available to the runner. Please check session creation logic.")
        except Exception as e: # Catch other general errors during agent processing
            print(f"Agent: An error occurred during processing: {e}")
            print("       (This could be related to LLM access, API key, or an internal ADK issue.)")
            # Simplified fallback to show direct mock tool output
            print("       (Attempting to call mock tool directly as a fallback...)")
            try:
                city_in_query = "unknown"
                words_in_query = query.lower().replace("?", "").replace(".","").split()
                if "in" in words_in_query:
                    city_idx = words_in_query.index("in")
                    if city_idx + 1 < len(words_in_query): city_in_query = " ".join(words_in_query[city_idx+1:])
                elif "for" in words_in_query:
                    city_idx = words_in_query.index("for")
                    if city_idx + 1 < len(words_in_query): city_in_query = " ".join(words_in_query[city_idx+1:])
                elif len(words_in_query) > 0 and words_in_query[-1] not in ["weather", "today", "now", "please", "me", "tell"]:
                     city_in_query = words_in_query[-1]

                if city_in_query and city_in_query != "unknown":
                     print(f"       Mock Tool (direct call for '{city_in_query}'): {get_weather(city_in_query)}")
                else:
                    print("       Could not determine city from query for direct mock tool call.")
            except Exception as fallback_e:
                print(f"       Error during fallback mock tool call: {fallback_e}")
        print("-" * 10)

    print("\nInteractive session ended.")