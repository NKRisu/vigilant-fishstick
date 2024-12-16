


def main():
    # Questions for each block "chapter", simple dictionary structure, with the question line, answer options and correct answer
    # These were a pain to type., should have used AI or something instead.
    variable_types_questions = [
        ("What is the type of this variable?: 'var = (1, 2, 3)'", ["A: list", "B: Tuple", "C: Set", "D: Dict"], "B"),
        ("What is the type of this variable?: 'var = [1, 2, 3]'", ["A: list", "B: Tuple", "C: Set", "D: Dict"], "A"),
        ("What is the type of this variable?: 'var = {'a': 1, 'b': 2}'", ["A: list", "B: Tuple", "C: Set", "D: Dict"], "D"),
        ("What is the type of this variable?: 'var = {1, 2, 3}'", ["A: list", "B: Tuple", "C: Set", "D: Dict"], "C"),
    ]

    code_output_questions = [
        ("What is the output of this code?: print('Hello, World!'[::-1])", ["A: Hello, World!", "B: !dlroW ,olleH", "C: Hello", "D: Error"], "B"),
        ("How many times does this code loop?: 'for i in range(5):\n print(i)'", ["A: 4", "B: 2", "C: 5", "D: 3"], "C"),
        ("What is the output of this code?: 'print(2 ** 3)'", ["A: 6", "B: 8", "C: 9", "D: 16"], "B"),
        ("What is the output of this code?: 'print(len('Python'))'", ["A: 5", "B: 6", "C: 7", "D: Error"], "B"),
        ("What is the output of this code?: 'print('Python'.upper())'", ["A: python", "B: PYTHON", "C: Python", "D: Error"], "B"),
    ]

    error_identification_questions = [
         ("What is the error in the following code?\n\nx = 10\nif x > 5\n print('x is greater than 5')", ["A: Missing colon after the `if` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "A"),
         ("What is the error in the following code?\n\ndef func(x):\nprint(x * x)", ["A: Missing colon after the `def` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "B"),
         ("What is the error in the following code?\n\nfor i in range(5)\n print(i)", ["A: Missing colon after the `for` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "A"),
         ("What is the error in the following code?\n\nx = [1, 2, 3]\nprint(x[3])", ["A: Index out of range", "B: Syntax error", "C: Type error", "D: No error"], "A"),
         ("What is the error in the following code?\n\ndef func(x):\n return x + 2\nprint(func(5))", ["A: Missing colon after the `def` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "D"),
         ("What is the error in the following code?\n\nx = 10\nif x > 5:\nprint('x is greater than 5')", ["A: Missing colon after the `if` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "B"),
         ("What is the error in the following code?\n\ny = 'Hello'\nprint(y.lower)", ["A: Missing parentheses in the `lower` method", "B: Syntax error", "C: Type error", "D: No error"], "A"),
    ]

    code_modification_questions = [
        ("Modify the following code to print the square of each number in the list:\n\nnumbers = [1, 2, 3, 4, 5]\nfor number in numbers:\n print(number)", ["A: print(number ** 2)", "B: print(number * 2)", "C: print(number + 2)", "D: print(number - 2)"], "A"),
        ("Modify the following code to print 'Hello, World!' in uppercase:\n\nmessage = 'Hello, World!'\nprint(message)", ["A: print(message.upper())", "B: print(message.lower())", "C: print(message.capitalize())", "D: print(message.title())"], "A"),
        ("Modify the following code to check if a number is even:\n\nnumber = 10\nif number % 2 == 0:\n print('Even')\nelse:\n print('Odd')", ["A: if number % 2 == 1:", "B: if number % 2 != 0:", "C: if number % 2 == 0:", "D: if number % 2 > 0:"], "C"),
        ("Modify the following code to print the length of the string:\n\ntext = 'Python'\nprint(text)", ["A: print(len(text))", "B: print(text.length())", "C: print(text.size())", "D: print(text.count())"], "A"),
        ("Modify the following code to append a new item to the list:\n\nfruits = ['apple', 'banana', 'cherry']\nprint(fruits)", ["A: fruits.append('orange')", "B: fruits.add('orange')", "C: fruits.insert('orange')", "D: fruits.extend('orange')"], "A"),
        ("Modify the following code to remove the last item from the list:\n\nfruits = ['apple', 'banana', 'cherry']\nprint(fruits)", ["A: fruits.pop()", "B: fruits.remove()", "C: fruits.delete()", "D: fruits.clear()"], "A"),
        ("Modify the following code to sort the list in ascending order:\n\nnumbers = [5, 2, 9, 1, 5, 6]\nprint(numbers)", ["A: numbers.sort()", "B: numbers.reverse()", "C: numbers.order()", "D: numbers.arrange()"], "A"),
        ("Modify the following code to print the first character of the string:\n\ntext = 'Python'\nprint(text)", ["A: print(text[0])", "B: print(text[1])", "C: print(text[-1])", "D: print(text[2])"], "A"),
    ]

    # Function to ask questions and calculate score
    def ask_questions(questions):
        score = 0
        for question, options, correct_answer in questions:
            answer, is_correct = ask_question(question, options, correct_answer)
            if is_correct:
                score += 1
            print(f"You picked: {answer}, correct answer: {correct_answer}")
        return score, len(questions)

    # Ask questions for each chapter and calculate scores
    variable_score, variable_max = ask_questions(variable_types_questions)
    code_output_score, code_output_max = ask_questions(code_output_questions)
    error_identification_score, error_identification_max = ask_questions(error_identification_questions)
    code_modification_score, code_modification_max = ask_questions(code_modification_questions)

    # Calculate total score and max score
    total_score = variable_score + code_output_score + error_identification_score + code_modification_score
    total_max = variable_max + code_output_max + error_identification_max + code_modification_max

    # Calculate percentage, .1% cuts the percentage off after first decimal.
    percentage = total_score / total_max
    end_message = f"{total_score} out of {total_max}, {percentage:.1%}"

    # Print scores for each chapter
    print(f"Variable Score: {variable_score} out of {variable_max}")
    print(f"Code Output Score: {code_output_score} out of {code_output_max}")
    print(f"Error Identification Score: {error_identification_score} out of {error_identification_max}")
    print(f"Code Modification Score: {code_modification_score} out of {code_modification_max}")

    # Print final grade
    if percentage <= 0.5:
        print("You did not pass, try again! F.", end_message)
    elif percentage <= 0.65:
        print("You did pass, but you should practice more. D.", end_message)
    elif percentage <= 0.75:
        print("Nice! C!", end_message)
    elif percentage <= 0.85:
        print("Good job, B!", end_message)
    elif percentage <= 0.95:
        print("WELL DONE! A for amazing!", end_message)
    else:
        print("Incredible!! A+ effort!", end_message)


# Function to ask a single question
def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
# Checking for valid answers and making answers uppercase, should help the user press right buttons and get graded fairly
    answer = ""
    valid_options = ["A", "B", "C", "D"]
    while answer not in valid_options:
        answer = input("Pick A, B, C or D: ").upper()
        if answer not in valid_options:
            print("Invalid choice. Please pick A, B, C or D.")

    is_correct = answer == correct_answer
    return answer, is_correct


if __name__ == "__main__":
    main()
