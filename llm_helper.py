
# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
model="LoneStriker/Starling-LM-7B-beta-GGUF"

def get_context_prompt(question, context):
        """ GPT3 prompt without text-based context from marqo search. """
        return f'SOURCES: \n{context}\n\nQUESTION: {question}\n\nAnswer:'


def ask_llm(marqo_results, question):
    # Build context using Marqo's highlighting functionality.
    context = ''
    for i, hit in enumerate(marqo_results['hits']):
                    text = hit['note']
                    # for section, text in hit['_highlights'].items():
                    #     context += text + '\n'
                    context += f'Note {i})  {" ".join(text.split()[:60])}... \n'

    prompt = get_context_prompt(question=question, context=context)

    print ("Prompt : " + prompt)


    completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "En te basant sur les éléments contenus dans la section \"SOURCES\" répond à la question posée dans le section \"QUESTION\". Tu indiqueras de quelles sources est basée ta réponse."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.2,
    )

    llm=completion.choices[0].message

    print(llm)

    return llm