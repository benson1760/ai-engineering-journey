# ================================
# MEMORY STORAGE (SECOND BRAIN CORE)
# ================================

# In-memory storage (temporary for now)
memory_log = []


# ================================
# SAVE FUNCTION
# ================================

# Stores task + response in memory
def save_to_memory(task, response):

    entry = {
        "task": task,
        "response": response
    }

    # Add to memory log
    memory_log.append(entry)

    # Log for debugging
    print(f"[MEMORY SAVED] {entry}")


# ================================
# RETRIEVE FULL MEMORY
# ================================

# Returns all stored entries
def get_memory():
    return memory_log


# ================================
# OPTIONAL: GET LAST TASK
# ================================

# Useful for context-aware agents later
def get_last_task():

    if memory_log:
        return memory_log[-1]

    return None