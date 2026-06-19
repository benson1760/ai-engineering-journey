def agent_response(task):
    task = task.lower()

    if "ai" in task:
        return "You should focus on Python, APIs, and building systems."

    elif "project" in task:
        return "Try building an API or improving your dashboard."

    elif "help" in task:
        return "I can guide you. Ask about coding, projects, or next steps."

    else:
        return f"I received your task: {task}"