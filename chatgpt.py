import openai

openai.api_key = "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"

completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt="¿Que hora es?",
    max_tokens=1
)

print(completion)


