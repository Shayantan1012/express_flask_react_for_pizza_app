from VoiceAssistance_Updated.llm_engine import get_llm

llm = get_llm()
print(llm.invoke("Introduce urself").content)
