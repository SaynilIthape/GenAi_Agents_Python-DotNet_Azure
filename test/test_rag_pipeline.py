from app.rag_pipeline import answer_question

while True:
    question = input("\nAsk your manufacturing question (or type 'exit'): ")
    if question.lower=="exit":
        break

    answer =  answer_question(question)

    print("\nAnswer:")
    print(answer)
