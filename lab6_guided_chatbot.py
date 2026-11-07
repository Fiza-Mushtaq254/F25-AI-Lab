
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
faq_data = [
    (
        "Where can I view my exam results?",
        "Students can view their examination results by signing in to the university portal.",
        "Examination Information Guide"
    ),
    (
        "How do I apply for a leave?",
        "Students can submit a leave request through the student affairs office.",
        "Student Affairs Handbook"
    )
]
faq_questions = [item[0] for item in faq_data]
text_model = TfidfVectorizer(stop_words="english")
faq_matrix = text_model.fit_transform(faq_questions)
print("===== University Support Assistant =====")
print("Enter 'exit' to close the chatbot.")
while True:
    entered_text = input("\nStudent: ").strip()
    if entered_text.lower() == "exit":
        print("Assistant: Thank you! Have a nice day.")
        break
    if not entered_text:
        print("Assistant: Please type your question first.")
        continue
    exact_match = False
    for item in faq_data:
        clean_input = entered_text.lower().strip("?.! ")
        clean_question = item[0].lower().strip("?.! ")
        if clean_input == clean_question:
            print("Assistant:", item[1])
            print("Reference:", item[2])
            exact_match = True
            break
    if exact_match:
        continue
    input_vector = text_model.transform([entered_text])
    similarity_values = cosine_similarity(input_vector, faq_matrix)
    selected_index = similarity_values.argmax()
    selected_score = similarity_values[0][selected_index]
    if selected_score >= 0.40:
        print("Assistant: A related question is available.")
        print("Suggested question:", faq_questions[selected_index])
        confirmation = input("Is this what you are asking? (yes/no): ")
        if confirmation.lower().strip() == "yes":
            print("Assistant:", faq_data[selected_index][1])
            print("Reference:", faq_data[selected_index][2])
        else:
            print("Assistant: Please enter your question again.")
    else:
        print("Assistant: No relevant information was found.")

