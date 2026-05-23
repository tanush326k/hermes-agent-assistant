def search_tool(query: str):
    return {
        "tool": "search",
        "query": query,
        "result": f"Found relevant information about: {query}"
    }

def calculator_tool(expression: str):
    try:
        return {
            "tool": "calculator",
            "input": expression,
            "result": eval(expression)
        }
    except:
        return {"error": "Invalid expression"}