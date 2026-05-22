import string

# ==================================================
# ESSAY SIMILARITY CHECKER
# ==================================================
# This program compares two essays.
# It checks common words and gives plagiarism percentage.


def read_file(file_name):
    # This part reads the essay file.

    try:
        with open(file_name, "r") as file:
            return file.read()

    except FileNotFoundError:
        print(f"Sorry, {file_name} is not found. Put it in the same folder.")
        return ""


def clean_words(text):
    # This part prepares words before comparing.

    if not isinstance(text, str):
        return []

    text = text.lower()

    # This removes punctuation like commas and full stops.
    for mark in string.punctuation:
        text = text.replace(mark, "")

    # This changes the text into a list of words.
    words = text.split()

    return words


def count_words(words):
    # This part counts how many times each word appears.

    if not isinstance(words, list):
        return {}

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def show_common_words(common_words, first_count, second_count):
    # This part shows common words found in both essays.

    print("\n" + "-" * 50)
    print("COMMON WORDS FOUND")
    print("-" * 50)

    if len(common_words) == 0:
        print("No common words found.")

    else:
        print(f"{'Word':<18} {'Essay 1':<10} {'Essay 2'}")
        print("-" * 50)

        for word in sorted(common_words):
            print(f"{word:<18} {first_count[word]:<10} {second_count[word]}")


def show_top_words(title, word_count):
    # This part shows the top 5 repeated words.

    print("\n" + title)
    print("-" * 50)

    top_words = sorted(
        word_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for word, total in top_words[:5]:
        print(f"{word:<18} {total} time(s)")


def search_word(word_to_find, first_words, second_words):
    # This part searches one word in both essays.

    if not isinstance(word_to_find, str):
        return False

    word_to_find = word_to_find.lower().strip()

    if word_to_find == "":
        print("Please enter a word.")
        return False

    first_total = first_words.count(word_to_find)
    second_total = second_words.count(word_to_find)

    print("\n" + "-" * 50)
    print("SEARCH RESULT")
    print("-" * 50)

    if first_total > 0 or second_total > 0:
        print(f"True: The word '{word_to_find}' was found.")
        print(f"Essay 1: {first_total} time(s)")
        print(f"Essay 2: {second_total} time(s)")
        return True

    else:
        print(f"False: The word '{word_to_find}' was not found.")
        return False


def calculate_similarity(first_words, second_words):
    # This part calculates plagiarism percentage.

    first_unique = set(first_words)
    second_unique = set(second_words)

    # Common words are words found in both essays.
    common_words = first_unique.intersection(second_unique)

    # All unique words are all different words from both essays.
    all_unique_words = first_unique.union(second_unique)

    if len(all_unique_words) == 0:
        return 0, common_words, all_unique_words

    similarity = (len(common_words) / len(all_unique_words)) * 100

    return similarity, common_words, all_unique_words


def show_result(similarity):
    # This part gives final plagiarism decision.

    print("\n" + "-" * 50)
    print("FINAL RESULT")
    print("-" * 50)

    print(f"Plagiarism Percentage: {similarity:.2f}%")

    if similarity >= 50:
        print("Result: Plagiarism detected.")

    else:
        print("Result: No plagiarism detected.")


def main():
    # This is the main part that runs the whole program.

    print("=" * 50)
    print("ESSAY SIMILARITY CHECKER")
    print("=" * 50)

    # Step 1: Read essay files.
    first_text = read_file("essay1.txt")
    second_text = read_file("essay2.txt")

    # Step 2: Clean the words.
    first_words = clean_words(first_text)
    second_words = clean_words(second_text)

    # Step 3: Check if essays have words.
    if len(first_words) == 0 or len(second_words) == 0:
        print("One essay has no words. Please check the files.")
        return

    # Step 4: Count words in each essay.
    first_count = count_words(first_words)
    second_count = count_words(second_words)

    # Step 5: Find similarity and common words.
    similarity, common_words, all_unique_words = calculate_similarity(
        first_words,
        second_words
    )

    # Step 6: Show common words.
    show_common_words(common_words, first_count, second_count)

    # Step 7: Show top repeated words.
    show_top_words("TOP 5 REPEATED WORDS IN ESSAY 1", first_count)
    show_top_words("TOP 5 REPEATED WORDS IN ESSAY 2", second_count)

    # Step 8: Show word statistics.
    print("\n" + "-" * 50)
    print("WORD STATISTICS")
    print("-" * 50)
    print("Common Words:", len(common_words))
    print("All Unique Words:", len(all_unique_words))

    # Step 9: Show final result.
    show_result(similarity)

    # Step 10: Keep searching words until user stops.
    while True:
        user_word = input("\nEnter a word to search (or type exit): ")

        if user_word.lower().strip() == "exit":
            print("Search ended.")
            break

        search_word(user_word, first_words, second_words)


# This starts the program.
main()