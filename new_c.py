from dataclasses import dataclass
import customtkinter as ct


root = ct.CTk()
root.title('Kalkulator')
root.resizable(False, False)


def get_text(event=None):
    """function program"""
    text_content = text_display.get('1.0', ct.END).strip()
    list_signs = build_list(text_content)
    no_new_line()
    calc_list = calc(list_signs)
    result = function_distribution(calc_list)
    # return "break" # dzięki temu kursor nie przechodzi do następnej lini


def no_new_line():
    """clean text area"""
    text_display.delete('1.0', ct.END)
    

def build_list(data):
    """creating sign list from user"""
    return data.split()


def create_button(name):
    """button creator"""
    return ct.CTkButton(frame, text=name, command=lambda: print_text(name),
                        width=70, height=70,
                        corner_radius=4,
                        font=ct.CTkFont(size=24, weight="bold")) 


@dataclass
class Calculator:
    num1: float
    sign: str


def calc(data) -> list:
    """class creator"""
    calc_list = []
    for index, value in enumerate(data):
        if value in ('+', '-', ':', 'x', '='):
            try:
                num1 = float(data[index - 1]) if index > 0 else None
                calc_list.append(Calculator(num1, value))
            except ValueError:
                pass  # Ignorujemy błędy konwersji
    return calc_list


def function_distribution(data) -> int:
    """sorting and performing a logical operation"""
    result = 0
    sign = None
    for d in data:
        if d.num1 is not None:
            if sign is None:
                result = d.num1
            elif sign == '+':
                result += d.num1
            elif sign == '-':
                result -= d.num1
            elif sign == ':':
                result /= d.num1
            elif sign == 'x':
                result *= d.num1
            sign = d.sign

    if sign == '=':
        print_text(str(result))
    return result


def print_text(text):
    """writing a character from a button in the text console"""
    text_display.insert(ct.END, text)
    text_display.see(ct.END)


frame1 = ct.CTkFrame(root, corner_radius=0)
frame1.pack()
text_display = ct.CTkTextbox(frame1, height=70, width=300, corner_radius=4)
text_display.pack(pady=(5, 0))
text_display.bind("<Return>", get_text)
text_display.configure(font=("Arial", 30))

frame = ct.CTkFrame(root, corner_radius=0)
frame.pack()

padx = 3
pady = 3

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('0', 3, 1), ('=', 3, 2, lambda: (print_text(' = '), get_text())),
    (' + ', 0, 3), (' - ', 1, 3), (' x ', 2, 3), (' / ', 3, 3), ('.', 3, 0)
]

for (text, row, col, *cmd) in buttons:
    button = create_button(text)
    if cmd:
        button.configure(command=cmd[0])
    button.grid(row=row, column=col, padx=padx, pady=pady)


if __name__ == '__main__':
    root.mainloop()