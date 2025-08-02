# main.py
from langgraph_agent import graph


def main():
    # FOR LANGGRAPH
    print("Type something to your assistant (or 'exit'):")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        state = {"input": user_input}
        result = graph.invoke(state)

        print("AI:", result.get("output", "No response"))

if __name__ == "__main__":

    main()
