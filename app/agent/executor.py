from app.agent.planner import create_plan
from app.services.tools import search_tool, calculator_tool
from app.agent.memory import save_memory

def run_agent(task: str):
    plan = create_plan(task)

    tools_used = []

    # SIMPLE TOOL DECISION LOGIC
    if "search" in task.lower():
        tools_used.append(search_tool(task))

    if any(char.isdigit() for char in task):
        tools_used.append(calculator_tool("2+2"))

    result = {
        "task": task,
        "plan": plan,
        "tools_used": tools_used,
        "final_answer": f"Processed task: {task}"
    }

    save_memory(result)

    return result