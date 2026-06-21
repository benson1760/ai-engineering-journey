# ================================
# IMPORT PIPELINES
# ================================

# Pipelines define multi-step workflows
from pipeline import dev_pipeline, content_pipeline


# ================================
# AGENT DEFINITIONS (SPECIALIZED ROLES)
# ================================

# Development Agent
# Handles coding, APIs, and technical tasks
def dev_agent(task):
    return dev_pipeline(task)


# Content Agent
# Handles content generation tasks (ideas, scripts, etc.)
def content_agent(task):
    return content_pipeline(task)


# Help Agent
# Provides general assistance and guidance
def help_agent(task):
    return "Help Agent: Ask me about Python, APIs, or your next step."


# ================================
# ORCHESTRATOR (CORE SYSTEM LOGIC)
# ================================

# This function decides WHICH agent should handle a task
def orchestrator(task):

    # Normalize input (lowercase for easier matching)
    task = task.lower()

    # ----------------------------
    # ROUTING LOGIC
    # ----------------------------

    # If task relates to development
    if "code" in task or "api" in task or "build" in task:
        return dev_agent(task)

    # If task relates to content creation
    elif "video" in task or "content" in task:
        return content_agent(task)

    # If user needs help / learning
    elif "help" in task or "learn" in task:
        return help_agent(task)

    # Default fallback
    else:
        return f"Orchestrator: I received your task -> {task}"