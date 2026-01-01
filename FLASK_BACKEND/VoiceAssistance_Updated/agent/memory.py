from langchain.memory import ConversationBufferMemory

# Single memory instance (per process)
# Later you can replace this with Redis / DB per user
_memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)


def get_memory():
    """
    Returns the shared conversation memory.
    """
    return _memory
