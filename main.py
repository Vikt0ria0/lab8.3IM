import tkinter as tk
import random
import matplotlib.pyplot as plt

def button_click():
    try:
        num_events = int(entry_n.get())
        prob_t = [float(entry.get()) for entry in entries_prob]

        if sum(prob_t) > 1:
            result_label.config(text="Сумма вероятностей должна быть <= 1")
            return

        prob_t.append(1 - sum(prob_t))
        stat = [0] * 5

        for _ in range(num_events):
            a = random.random()
            summ = 0
            for k in range(5):
                summ += prob_t[k]
                if a <= summ:
                    stat[k] += 1
                    break

        prob_ex = [count / num_events for count in stat]

        result_text = "\n".join([f"Событие {i+1}: {prob:.4f}" for i, prob in enumerate(prob_ex)])
        result_label.config(text=result_text)


        plt.figure(figsize=(8, 6))
        plt.bar(range(1, 6), prob_ex)
        plt.xlabel("Событие")
        plt.ylabel("Эмпирическая вероятность")
        plt.grid(True)
        plt.show()

    except ValueError:
        result_label.config(text="Введите корректные числовые значения")

window = tk.Tk()
window.title()

label_n = tk.Label(window, text="Количество событий (N):")
label_n.grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(window)
entry_n.grid(row=0, column=1, padx=5, pady=5)
labels_prob = [tk.Label(window, text=f"Вероятность события {i+1}:") for i in range(4)]
entries_prob = [tk.Entry(window) for _ in range(4)]
for i in range(4):
    labels_prob[i].grid(row=i+1, column=0, padx=5, pady=5)
    entries_prob[i].grid(row=i+1, column=1, padx=5, pady=5)
button = tk.Button(window, text="Рассчитать", command=button_click)
button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
result_label = tk.Label(window, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)


window.mainloop()