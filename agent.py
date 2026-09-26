from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

finance_agent = Agent(
    name="Finance Agent",
    model = Groq(id="openai/gpt-oss-120b"),

    tools=[YFinanceTools(
        enable_stock_price=True,
        enable_analyst_recommendations=True,
        enable_company_info=True,
        enable_company_news=True,
        enable_historical_prices=True,
    )],
    instructions=["You are a financial research assistant.",
        "Use financial tools whenever the user asks about stocks or companies.",
        "Always identify the company and ticker symbol when possible.",
        "Present financial information clearly.",
        "Mention that market data can change.",
        "Do not claim certainty about future stock prices.",
        "Use table for comparisons and historical data.",
        "Do not provide personalized financial advice.",
    ],

    markdown=True,
)

if __name__ == "__main__":
    print("===================================")
    print("       AI FINANCE AGENT")
    print("===================================")

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        print("\nFinance Agent:\n")

        finance_agent.print_response(
            question,
            stream=True
        )