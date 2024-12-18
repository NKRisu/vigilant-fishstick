import tkinter as tk
from tkinter import messagebox


# Function to check answers and calculate score
def check_answers(questions, answers, score_var, section_scores):
    total_questions = len(questions)
    correct_answers = 0
    section_correct = {section: 0 for section in section_scores.keys()}

    for i, (question, options, correct_answer, section) in enumerate(questions):
        if answers[i].get() == correct_answer:
            correct_answers += 1
            section_correct[section] += 1

    for section, score in section_correct.items():
        section_scores[section].set(score)
    score_var.set(correct_answers)
    percentage = (correct_answers / total_questions) * 100
    if percentage >= 95:
        grade = "A+, INCREDIBLE!"
    elif percentage >= 90:
        grade = "A, Amazing!!"
    elif percentage >= 80:
        grade = "B, pretty well done!"
    elif percentage >= 70:
        grade = "C, you passed!"
    elif percentage >= 60:
        grade = "D, you did pass, barely"
    else:
        grade = "F, you need some more training"

    messagebox.showinfo("Score", f"Your score: {correct_answers}/{total_questions}\nPercentage: {percentage:.2f}%\nGrade: {grade}")


# Main function
def main():
    # Questions dictionary block for var types
    variable_types_questions = [
        ("What is the type of this variable?: 'var = (1, 2, 3)'", ["A: list", "B: Tuple", "C: Set", "D: Dict"], "B", "Variable Types"),
        ("What is the type of this variable?: 'var = [1, 2, 3]'", ["A: list", "B: Tuple", "C: Set", "D: Dict"], "A", "Variable Types"),
        ("What is the type of this variable?: 'var = {'a': 1, 'b': 2}'", ["A: list", "B: Tuple", "C: Set", "D: Dict"], "D", "Variable Types"),
        ("What is the type of this variable?: 'var = {1, 2, 3}'", ["A: list", "B: Tuple", "C: Set", "D: Dict"], "C", "Variable Types"),
    ]
    # Questions dictionary block for output recognition
    code_output_questions = [
        ("What is the output of this code?: print('Hello, World!'[::-1])", ["A: Hello, World!", "B: !dlroW ,olleH", "C: Hello", "D: Error"], "B", "Code Output"),
        ("How many times does this code loop?: 'for i in range(5):\n print(i)'", ["A: 4", "B: 2", "C: 5", "D: 3"], "C", "Code Output"),
        ("What is the output of this code?: 'print(2 ** 3)'", ["A: 6", "B: 8", "C: 9", "D: 16"], "B", "Code Output"),
        ("What is the output of this code?: 'print(len('Python'))'", ["A: 5", "B: 6", "C: 7", "D: Error"], "B", "Code Output"),
        ("What is the output of this code?: 'print('Python'.upper())'", ["A: python", "B: PYTHON", "C: Python", "D: Error"], "B", "Code Output"),
    ]
    # Questions dictionary block for error identifying
    error_identification_questions = [
         ("What is the error in the following code?\n\nx = 10\nif x > 5\n print('x is greater than 5')", ["A: Missing colon after the `if` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "A", "Error Identification"),
         ("What is the error in the following code?\n\ndef func(x):\nprint(x * x)", ["A: Missing colon after the `def` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "B", "Error Identification"),
         ("What is the error in the following code?\n\nfor i in range(5)\n print(i)", ["A: Missing colon after the `for` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "A", "Error Identification"),
         ("What is the error in the following code?\n\nx = [1, 2, 3]\nprint(x[3])", ["A: Index out of range", "B: Syntax error", "C: Type error", "D: No error"], "A", "Error Identification"),
         ("What is the error in the following code?\n\ndef func(x):\n return x + 2\nprint(func(5))", ["A: Missing colon after the `def` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "D", "Error Identification"),
         ("What is the error in the following code?\n\nx = 10\nif x > 5:\nprint('x is greater than 5')", ["A: Missing colon after the `if` statement", "B: Indentation error", "C: Syntax error", "D: No error"], "B", "Error Identification"),
         ("What is the error in the following code?\n\ny = 'Hello'\nprint(y.lower)", ["A: Missing parentheses in the `lower` method", "B: Syntax error", "C: Type error", "D: No error"], "A", "Error Identification"),
    ]
    # Questions dictionary block for code modifications
    code_modification_questions = [
        ("Modify the following code to print the square of each number in the list:\n\nnumbers = [1, 2, 3, 4, 5]\nfor number in numbers:\n print(number)", ["A: print(number ** 2)", "B: print(number * 2)", "C: print(number + 2)", "D: print(number - 2)"], "A", "Code Modification"),
        ("Modify the following code to print 'Hello, World!' in uppercase:\n\nmessage = 'Hello, World!'\nprint(message)", ["A: print(message.upper())", "B: print(message.lower())", "C: print(message.capitalize())", "D: print(message.title())"], "A", "Code Modification"),
        ("Modify the following code to check if a number is even:\n\nnumber = 10\n[code here]\n print('Even')\nelse:\n print('Odd')", ["A: if number % 2 == 1:", "B: if number % 2 != 0:", "C: if number % 2 == 0:", "D: if number % 2 > 0:"], "C", "Code Modification"),
        ("Modify the following code to print the length of the string:\n\ntext = 'Python'\nprint(text)", ["A: print(len(text))", "B: print(text.length())", "C: print(text.size())", "D: print(text.count())"], "A", "Code Modification"),
        ("Modify the following code to append a new item to the list:\n\nfruits = ['apple', 'banana', 'cherry']\nprint(fruits)", ["A: fruits.append('orange')", "B: fruits.add('orange')", "C: fruits.insert('orange')", "D: fruits.extend('orange')"], "A", "Code Modification"),
        ("Modify the following code to remove the last item from the list:\n\nfruits = ['apple', 'banana', 'cherry']\nprint(fruits)", ["A: fruits.pop()", "B: fruits.remove()", "C: fruits.delete()", "D: fruits.clear()"], "A", "Code Modification"),
        ("Modify the following code to sort the list in ascending order:\n\nnumbers = [5, 2, 9, 1, 5, 6]\nprint(numbers)", ["A: numbers.sort()", "B: numbers.reverse()", "C: numbers.order()", "D: numbers.arrange()"], "A", "Code Modification"),
        ("Modify the following code to print the first character of the string:\n\ntext = 'Python'\nprint(text)", ["A: print(text[0])", "B: print(text[1])", "C: print(text[-1])", "D: print(text[2])"], "A", "Code Modification"),
    ]
    # Combine blocks into one for tkinter to show
    all_questions = variable_types_questions + code_output_questions + error_identification_questions + code_modification_questions

    # Create the main window
    root = tk.Tk()
    root.title("Quiz App")

    # Set the minimum size of window
    root.minsize(500, 800)

    # Create a variable to store the score
    score_var = tk.IntVar()

    # Create variables to store section scores
    section_scores = {
        "Variable Types": tk.IntVar(),
        "Code Output": tk.IntVar(),
        "Error Identification": tk.IntVar(),
        "Code Modification": tk.IntVar(),
    }

    # Create a frame for the app
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas for scrolling
    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar to the canvas
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create another frame inside the canvas for questions
    questions_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=questions_frame, anchor="nw")

    # Create a list to store the user's answers
    answers = []

    # Dictionary to store the number of questions in each section
    section_questions = {
        "Variable Types": len(variable_types_questions),
        "Code Output": len(code_output_questions),
        "Error Identification": len(error_identification_questions),
        "Code Modification": len(code_modification_questions),
    }

    # Add questions to the frame
    for question, options, correct_answer, section in all_questions:    # here is the all_questions
        tk.Label(questions_frame, text=question).pack(anchor="w")
        var = tk.StringVar(value='NULL')  # empty radio buttons
        answers.append(var)
        for option in options:
            tk.Radiobutton(questions_frame, text=option, variable=var, value=option[0]).pack(anchor="w")

    # Add a submit button
    tk.Button(questions_frame, text="Submit", command=lambda: check_answers(all_questions, answers, score_var, section_scores)).pack()

    # Update the scroll region
    questions_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Display section scores
    tk.Label(root, text="Section Scores", font=("Helvetica", 16, "bold")).pack(pady=10)  # title banner

    for section, score in section_scores.items():
        max_score = section_questions[section]  # maximum score for sections
        score_text = tk.StringVar()     # string variable for score text
        score_text.set(f"{score.get()} out of {max_score}")
        tk.Label(root, text=f"{section} Score:").pack()
        tk.Label(root, textvariable=score_text).pack()

        # Update the score_text whenever the score changes
        score.trace_add("write", lambda *args, score=score, score_text=score_text, max_score=max_score: score_text.set(f"{score.get()} out of {max_score}"))
        # this mess found on stackoverflow to update a string in tkinter label

    root.mainloop()

if __name__ == "__main__":
    main()
