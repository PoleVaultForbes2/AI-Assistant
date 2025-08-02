# main.py
# from langchain.agents import initialize_agent
# from langchain.agents.agent_types import AgentType
# from ollama_model import get_ollama_model
# from tools import all_tools

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

    # FOR LANGCHAIN
    # llm = get_ollama_model()
    # agent = initialize_agent(
    #     tools=all_tools,
    #     llm=llm,
    #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True
    # )
    #
    # print("Type something to your assistant (or 'exit'):")
    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() in ["exit", "quit"]:
    #         break
    #     response = agent.run(user_input)
    #     print("AI:", response)


if __name__ == "__main__":
    main()