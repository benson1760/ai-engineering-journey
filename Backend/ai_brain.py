from pipeline import dev_pipeline, content_pipeline
from ai_brain import ai_response


def dev_agent(task):
    return dev_pipeline(task)


def content_agent(task):
    return content_pipeline(task)


def orchestrator(task):
    task = task.lower()

    # ✅ Keep your structured pipelines
    if "build" in task or "api" in task or "code" in task:
        return dev_agent(task)

    elif "content" in task or "video" in task:
        return content_agent(task)

    # ✅ EVERYTHING ELSE → AI BRAIN
    return ai_response(task)