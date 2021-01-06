import pandas as pd
import numpy as np
import plotly.graph_objects as go

class test:
    def __init__(self):
        self.questions = list()
        self.answers = list()
        self.correct_answers = 0
        self.score = 0

    def add_element(self, q, a):
        self.questions.append(q)
        self.answers.append(a)

    def remove_element(self, index):
        self.questions.pop(index)
        self.answers.pop(index)
        
    def show_answer(self, index):
        print(f"Q{index}: {self.questions[index-1]} - Ans_{index}: {self.answers[index-1]}")
    
    def show_answers(self):
        for index, (q, a) in enumerate(zip(self.questions, self.answers)):
            print(f"Q{index+1}: {q} - Ans_{index+1}: {a}")
    
    def build_from_csv(self, filename):
        df = pd.read_csv(filename)
        for index in range(df.shape[0]):
            self.add_element(df['Questions'][index], df['Answers'][index])
    
    def visualize_score(self):
        fig = go.Figure(data=[go.Pie(labels=["Correct", "Incorrect"],
                                     values=[self.score, 100-self.score],
                                     marker_colors=['rgb(10,100,10)', 'rgb(230,70,70)'],
                                     hole=.3)])
        fig.show()

    def test(self):
        self.correct_answers = 0
        for index, (q, a) in enumerate(zip(self.questions, self.answers)):
            current_answer = ''
            while len(str(current_answer))==0:
                current_answer = input(f"Q{index+1}: " + q)
                if len(current_answer)>0:
                    current_answer = float(current_answer)
                    self.correct_answers += int(current_answer == a)
                    if a==current_answer:
                        print("Correct")
                    else:
                        print("Incorrect")
        self.score =  100*np.sum(self.correct_answers)/len(self.questions)
        
        print(f"Your score: {self.score}")
        self.visualize_score()