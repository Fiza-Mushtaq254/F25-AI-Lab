
import re
documents = {
    "doc1": """University students should follow the academic rules during their studies. They are expected to attend classes, complete assignments and respect the people around them. RULE: Students must submit assignments before the announced deadline. EXCEPTION: A teacher may allow extra time when a student provides valid medical evidence before the deadline. Students should check the university portal for class updates and notices. Teachers explain course topics and guide students when they have questions. The examination department prepares the exam schedule and shares it before exams begin. Students must bring their identity cards to the examination hall. Mobile phones should be kept outside the examination room. If a student has a problem with a course, they can contact the department office. The university also provides a library, computer labs and study spaces. Students should use these facilities carefully and keep them clean. Regular attendance and good study habits can help students complete their courses successfully. They should also plan their work instead of waiting until the last day. These simple steps make study life easier for students and teachers.""",

    "doc2": """The university library gives students a quiet place to read and study. It contains textbooks, reference books, journals and newspapers for different subjects. Students can borrow a book by showing their university identity card. Each borrowed book has a return date, and students should bring it back on time. A late return may lead to a fine under the library rules. Students can search for books by using the online catalogue. Dr. Ali is the library coordinator and helps students find books. Library staff can also explain the borrowing process. Computers are available for academic research and preparing assignments. Students should keep the reading area quiet so other people can concentrate. Food and drinks should be kept away from books and computers. If a book is damaged, the student should tell a library worker. During examination weeks, the library may extend its study hours when staff are available. Students should check the notice board for changes to opening times. Group study is allowed in the assigned area, but loud conversations can disturb other readers. The library is useful when students need reliable information for their coursework. Everyone should take care of the shared resources so other students can use them too.""",

    "doc3": """The university transport service helps students travel between the campus and nearby areas. Students who want to use the buses should register at the transport office. They need to provide their student details and choose an available route. The office shares bus timings and stop locations before the semester starts. Students should reach their stops a few minutes before the bus arrives. Drivers must follow traffic rules and drive carefully in busy areas. Each bus has a limited number of seats, so students should use the seat assigned to them. Passengers must keep the bus clean and follow the safety instructions. The university may change a route if road work or heavy traffic makes the normal journey difficult. Students should read transport notices so they do not miss an update. If a student loses a bag or another item, they should contact the transport office. Staff can also receive complaints about delays or route problems. Before leaving campus, the transport team checks that the buses are ready for the journey. Students, drivers and staff all have a part in making the service safe. When a bus is delayed, students should wait at the assigned stop and contact the office for information instead of trying to board another route without permission. The service aims to provide dependable travel for the university community."""
}
def get_words(text):
    return list(re.finditer(r"\b\w+\b", text))
def fixed_chunks(text, size, overlap, doc_id):
    if overlap < 0 or overlap >= size:
        raise ValueError("Invalid overlap.")
    words = get_words(text)
    chunks = []
    step = size - overlap
    for i in range(0, len(words), step):
        part = words[i:i + size]
        if not part:
            break
        start = part[0].start()
        end = part[-1].end()
        chunks.append({
            "id": doc_id + "_fixed_" + str(len(chunks) + 1),
            "start": start,
            "end": end,
            "text": text[start:end]
        })
    return chunks
def sentence_chunks(text, size, doc_id):
    sentences = re.finditer(r"[^.!?]+[.!?]?", text)
    chunks = []
    current_words = []
    for sentence in sentences:
        words = get_words(sentence.group())
        positions = []
        for word in words:
            start = sentence.start() + word.start()
            end = sentence.start() + word.end()
            positions.append((start, end))
        if not positions:
            continue
        if len(positions) > size:
            if current_words:
                start = current_words[0][0]
                end = current_words[-1][1]
                chunks.append({
                    "id": doc_id + "_sentence_" + str(len(chunks) + 1),
                    "start": start,
                    "end": end,
                    "text": text[start:end]
                })
                current_words = []
            for i in range(0, len(positions), size):
                part = positions[i:i + size]
                start = part[0][0]
                end = part[-1][1]
                chunks.append({
                    "id": doc_id + "_sentence_" + str(len(chunks) + 1),
                    "start": start,
                    "end": end,
                    "text": text[start:end]
                })
        elif len(current_words) + len(positions) <= size:
            current_words.extend(positions)
        else:
            start = current_words[0][0]
            end = current_words[-1][1]
            chunks.append({
                "id": doc_id + "_sentence_" + str(len(chunks) + 1),
                "start": start,
                "end": end,
                "text": text[start:end]
            })
            current_words = positions[:]
    if current_words:
        start = current_words[0][0]
        end = current_words[-1][1]
        chunks.append({
            "id": doc_id + "_sentence_" + str(len(chunks) + 1),
            "start": start,
            "end": end,
            "text": text[start:end]
        })
    return chunks
def count_repeated(chunks):
    seen = set()
    repeated = 0
    for chunk in chunks:
        words = get_words(chunk["text"])
        for word in words:
            position = (
                chunk["start"] + word.start(),
                chunk["start"] + word.end()
            )
            if position in seen:
                repeated += 1
            else:
                seen.add(position)
    return repeated
def show_results(doc_id, text):
    print("\nDocument:", doc_id)
    print("Total Words:", len(get_words(text)))
    results = [
        ("Overlap 0", fixed_chunks(text, 40, 0, doc_id)),
        ("Overlap 10", fixed_chunks(text, 40, 10, doc_id)),
        ("Sentence Aware", sentence_chunks(text, 40, doc_id))
    ]
    for name, chunks in results:
        sizes = [len(get_words(c["text"])) for c in chunks]
        print("\nMethod:", name)
        print("Number of Chunks:", len(chunks))
        print("Chunk Sizes:", sizes)
        print("Repeated Words:", count_repeated(chunks))
        for chunk in chunks:
            print(
                chunk["id"],
                "Start:", chunk["start"],
                "End:", chunk["end"]
            )
        rule_found = any("RULE:" in c["text"] for c in chunks)
        exception_found = any("EXCEPTION:" in c["text"] for c in chunks)
        together = any(
            "RULE:" in c["text"] and "EXCEPTION:" in c["text"]
            for c in chunks
        )
        print("Rule Found:", rule_found)
        print("Exception Found:", exception_found)
        print("Both in Same Chunk:", together)
for doc_id, text in documents.items():
    show_results(doc_id, text)
print("\n===== Edge Case Tests =====")
empty = fixed_chunks("", 40, 0, "empty")
print("Empty Text Chunks:", len(empty))
short_text = "Students should follow university rules."
short = fixed_chunks(short_text, 40, 0, "short")
print("Short Document Chunks:", len(short))
try:
    fixed_chunks("This is a test.", 40, 40, "test")
except ValueError as error:
    print("Invalid Overlap:", error)
long_sentence = """Students should attend classes regularly complete their assignments follow university rules respect teachers check announcements use learning resources maintain discipline participate in activities complete academic tasks follow instructions respect classmates arrive on time prepare for examinations submit their work carefully improve their learning and take responsibility for their studies every day at university."""
long_chunks = sentence_chunks(long_sentence, 40, "long")
print("Long Sentence Words:", len(get_words(long_sentence)))
print("Long Sentence Chunks:", len(long_chunks))
print(
    "Long Sentence Chunk Sizes:",
    [len(get_words(c["text"])) for c in long_chunks]
)

