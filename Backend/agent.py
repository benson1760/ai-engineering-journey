def dev_agent(task):
    return "Dev Agent: I can help you build APIs, debug code, and create systems."


def content_agent(task):
    return "Content Agent: I can help generate ideas, scripts, and content."


def help_agent(task):
    return "Help Agent: Ask me about Python, APIs, or your next step."

def orchestrator(task):
    task = task.lower()

    if "code" in task or "api" in task or "build" in task:
        return dev_agent(task)

    elif "video" in task or "content" in task:
        return content_agent(task)

    elif "help" in task or "learn" in task:
        return help_agent(task)

    else:
        return f"Orchestrator: I received your task -> {task}"