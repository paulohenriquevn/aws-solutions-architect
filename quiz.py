import random
import re
import os

class QuizApp:
    def __init__(self, file_paths):
        self.questions = []
        self.correct_count = 0
        self.incorrect_count = 0
        self.load_questions(file_paths)

    def load_questions(self, file_paths):
        """Load questions from the given file paths."""
        for file_path in file_paths:
            with open(file_path, 'r') as f:
                content = f.read()
                matches = re.findall(r"### Questão.*?((?:(?!### Questão).)*?)<details>(.*?)</details>", content, re.DOTALL)
                for match in matches:
                    question_text = match[0].strip()
                    answer_details = match[1].strip()
                    self.questions.append((question_text, answer_details))

    def get_random_question(self):
        """Get a random question from the remaining list."""
        if self.questions:
            return random.choice(self.questions)
        else:
            return None

    def start_quiz(self):
        """Start the quiz application."""
        # Change terminal colors to white background and black text
        os.system('echo -e "\033[0;30;47m"')
        print("Bem-vindo ao Quiz! Responda as perguntas escolhendo uma ou mais opções corretas separadas por vírgula (ex: A,B ou A). Digite 'sair' para encerrar.")
        print(f"Total de questões disponíveis: {len(self.questions)}")
        while True:
            current_question = self.get_random_question()
            if not current_question:
                print("Você respondeu todas as questões! Parabéns!")
                break

            question_text, answer_details = current_question
            print(f"\nQuestão ({len(self.questions)} restantes):")
            print(question_text)
            user_answer = input("Sua resposta: ").strip().upper()

            if user_answer == 'SAIR':
                print("\nQuiz encerrado. Aqui está o seu resumo:")
                print(f"Acertos: {self.correct_count}")
                print(f"Erros: {self.incorrect_count}")
                print(f"Questões restantes: {len(self.questions)}")
                break

            correct_answer = re.search(r"<resposta>(.*?)</resposta>", answer_details)
            if correct_answer:
                correct_answers = set(correct_answer.group(1).split(','))
                user_answers = set(user_answer.split(','))
                if user_answers == correct_answers:
                    print("\nParabéns! Você acertou!")
                    self.correct_count += 1
                    self.questions.remove(current_question)  # Remove the question after a correct answer
                elif len(correct_answers) == 1 and user_answer in correct_answers:
                    print("\nParabéns! Você acertou!")
                    self.correct_count += 1
                    self.questions.remove(current_question)  # Remove the question after a correct answer
                else:
                    print("\nResposta incorreta.")
                    print("Resposta correta:", ','.join(correct_answers))
                    print("Explicação:")
                    explanation = re.sub(r"<resposta>.*?</resposta>", "", answer_details, flags=re.DOTALL).strip()
                    print(explanation)
                    self.incorrect_count += 1

            print(f"Questões restantes: {len(self.questions)}")
            input("Pressione Enter para continuar...")
            os.system('clear')  # Clear the terminal for the next question

if __name__ == "__main__":
    # Caminhos para os arquivos
    file_paths = ["exame-1-100.md", "exame-101-200.md"]

    # Inicializar o aplicativo
    quiz_app = QuizApp(file_paths)

    # Iniciar o quiz
    quiz_app.start_quiz()
