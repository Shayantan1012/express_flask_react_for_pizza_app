import json
from VoiceAssistance_Updated.llm_engine import get_llm
from VoiceAssistance_Updated.agent.memory import get_memory
from VoiceAssistance_Updated.service.intent_service import IntentService
from VoiceAssistance_Updated.prompts.intent_prompt import IntentPrompt

# 🔥 Create once (shared)
llm = get_llm()
memory = get_memory()


def run_agent(user_text: str) -> str:
    """
    Main orchestrator:
    1. Classify intent (LLM)
    2. Execute intent (Python)
    3. Generate response (LLM)
    4. Update memory
    """

    intent_prompt = IntentPrompt(user_text).intentPrompt()
    raw = llm.invoke(intent_prompt).content.strip()

    intent_data = json.loads(raw)

    service = IntentService(intent_data)
    result = service.handle()

    memory.chat_memory.add_user_message(user_text)
    memory.chat_memory.add_ai_message(result["response"])

    return json.dumps(result)


def clear_agent_memory():
    memory.clear()
