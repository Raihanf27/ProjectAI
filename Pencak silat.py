import tkinter as tk
from tkinter import messagebox


def hitung_persentase_kemenangan(pesilat_biru, pesilat_merah):
    bobot_mukul = 1
    bobot_nendang = 2
    bobot_banting = 3  # Bobot banting ditingkatkan
    bobot_gunting = 3  # Bobot gunting ditingkatkan
    bobot_counter = 1
    bobot_sapuan = 3  # Bobot sapuan ditingkatkan

    total_serangan_biru = (pesilat_biru['mukul'] * bobot_mukul) + (pesilat_biru['nendang'] * bobot_nendang) + (
            pesilat_biru['banting'] * bobot_banting) + (pesilat_biru['gunting'] * bobot_gunting) + (
                                  pesilat_biru['counter'] * bobot_counter) + (pesilat_biru['sapuan'] * bobot_sapuan)
    total_serangan_merah = (pesilat_merah['mukul'] * bobot_mukul) + (pesilat_merah['nendang'] * bobot_nendang) + (
            pesilat_merah['banting'] * bobot_banting) + (pesilat_merah['gunting'] * bobot_gunting) + (
                                   pesilat_merah['counter'] * bobot_counter) + (pesilat_merah['sapuan'] * bobot_sapuan)

    persentase_kemenangan_biru = (total_serangan_biru / (total_serangan_biru + total_serangan_merah)) * 100
    persentase_kemenangan_merah = (total_serangan_merah / (total_serangan_biru + total_serangan_merah)) * 100

    return persentase_kemenangan_biru, persentase_kemenangan_merah


class MartialArtsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Prediksi Pertandingan Bela Diri")
        self.geometry("400x400")

        self.pages = [
            {
                "title": "Pesilat Biru",
                "questions": [
                    "Apakah pesilat biru jago mukul?",
                    "Apakah pesilat biru jago nendang?",
                    "Apakah pesilat biru jago banting?",
                    "Apakah pesilat biru jago gunting?",
                    "Apakah pesilat biru jago counter?",
                    "Apakah pesilat biru jago sapuan?",
                ],
                "answers": [],
            },
            {
                "title": "Pesilat Merah",
                "questions": [
                    "Apakah pesilat merah jago mukul?",
                    "Apakah pesilat merah jago nendang?",
                    "Apakah pesilat merah jago banting?",
                    "Apakah pesilat merah jago gunting?",
                    "Apakah pesilat merah jago counter?",
                    "Apakah pesilat merah jago sapuan?",
                ],
                "answers": [],
            },
        ]

        self.page_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text=self.pages[self.page_index]["title"], font=("Arial", 16))
        self.label.pack(pady=20)

        self.question_label = tk.Label(self, text=self.pages[self.page_index]["questions"][0])
        self.question_label.pack()

        self.answer_frame = tk.Frame(self)
        self.answer_frame.pack()

        self.yes_button = tk.Button(self.answer_frame, text="Ya", command=self.answer_yes)
        self.yes_button.pack(side="left", padx=10)

        self.no_button = tk.Button(self.answer_frame, text="Tidak", command=self.answer_no)
        self.no_button.pack(side="left", padx=10)

    def answer_yes(self):
        self.pages[self.page_index]["answers"].append(True)
        self.show_next_question()

    def answer_no(self):
        self.pages[self.page_index]["answers"].append(False)
        self.show_next_question()

    def show_next_question(self):
        question_index = len(self.pages[self.page_index]["answers"])
        if question_index == len(self.pages[self.page_index]["questions"]):
            if self.page_index == len(self.pages) - 1:
                self.calculate_result()
            else:
                self.page_index += 1
                self.show_next_page()
        else:
            self.question_label.config(text=self.pages[self.page_index]["questions"][question_index])

    def show_next_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.create_widgets()

    def calculate_result(self):
        pesilat_biru = {
            "mukul": self.pages[0]["answers"][0] if self.pages[0]["answers"] else False,
            "nendang": self.pages[0]["answers"][1] if len(self.pages[0]["answers"]) > 1 else False,
            "banting": self.pages[0]["answers"][2] if len(self.pages[0]["answers"]) > 2 else False,
            "gunting": self.pages[0]["answers"][3] if len(self.pages[0]["answers"]) > 3 else False,
            "counter": self.pages[0]["answers"][4] if len(self.pages[0]["answers"]) > 4 else False,
            "sapuan": self.pages[0]["answers"][5] if len(self.pages[0]["answers"]) > 5 else False,
        }

        pesilat_merah = {
            "mukul": self.pages[1]["answers"][0] if self.pages[1]["answers"] else False,
            "nendang": self.pages[1]["answers"][1] if len(self.pages[1]["answers"]) > 1 else False,
            "banting": self.pages[1]["answers"][2] if len(self.pages[1]["answers"]) > 2 else False,
            "gunting": self.pages[1]["answers"][3] if len(self.pages[1]["answers"]) > 3 else False,
            "counter": self.pages[1]["answers"][4] if len(self.pages[1]["answers"]) > 4 else False,
            "sapuan": self.pages[1]["answers"][5] if len(self.pages[1]["answers"]) > 5 else False,
        }

        persentase_biru, persentase_merah = hitung_persentase_kemenangan(pesilat_biru, pesilat_merah)

        messagebox.showinfo(
            "Hasil",
            f"Persentase Kemenangan:\n\nPesilat Sudut Biru: {persentase_biru:.2f}%\nPesilat Sudut Merah: {persentase_merah:.2f}%"
        )

        self.destroy()


if __name__ == "__main__":
    app = MartialArtsApp()
    app.mainloop()
