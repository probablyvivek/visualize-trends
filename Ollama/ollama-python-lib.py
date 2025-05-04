import ollama

#chat api endpoint
chat_res = ollama.chat(
    model="gemma3:1b",
    messages=[{"role": "user", "content": "Give me 5 reason why Chelsea is the greatest football club in the world?"}]
)
print(chat_res["message"]["content"])

#generate api endpoint
gen_res = ollama.generate(
    model="gemma3:1b",
    prompt="Why are Arsenal fans so stupid?"
)
print(gen_res["response"])
