from pipeline import dev_pipeline, content_pipeline


def dev_agent(task):
    return dev_pipeline(task)


def content_agent(task):
    return content_pipeline(task)


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
