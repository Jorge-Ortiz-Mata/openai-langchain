from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

# def generic_answer(answer):
#   llm = OpenAI(temperature=0.6, model="gpt-3.5-turbo")

#   prompt_template = PromptTemplate(
#     input_variables=["answer"],
#     template="{answer}",
#   )

#   name_chain = LLMChain(llm=llm, prompt=prompt_template)

#   response = name_chain({"answer": answer})

#   return response

def langchain_agent():
  llm = OpenAI(temperature=0.7)

  tools = load_tools(["wikipedia", "llm-math"], llm = llm)

  agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
  )

  response = agent.run(
    "What is the averege age of dogs? Multiply by 4"
  )

  print(response)

# question_one = generic_answer("Hello, who won the world cup in 2014?")

# print(question_one)

langchain_agent()
