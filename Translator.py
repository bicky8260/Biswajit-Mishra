from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox as tmsg
from deep_translator import GoogleTranslator

root = Tk()
root.title("Translator")
root.geometry("800x500")
root.config(bg="beige")

# Dictionary mapping language codes to language names
languages = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani',
    'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian',
    'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)', 'co': 'Corsican',
    'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto',
    'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician',
    'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa',
    'haw': 'Hawaiian', 'he': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic',
    'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese',
    'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'rw': 'Kinyarwanda', 'ko': 'Korean', 'ku': 'Kurdish',
    'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish',
    'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori',
    'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar', 'ne': 'Nepali', 'no': 'Norwegian', 'or': 'Odia',
    'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian',
    'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona',
    'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish',
    'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'tt': 'Tatar',
    'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'tk': 'Turkmen', 'uk': 'Ukrainian', 'ur': 'Urdu',
    'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish',
    'yo': 'Yoruba', 'zu': 'Zulu'
}

def translate_text():
    language1 = t1.get("1.0", "end-1c")
    language2 = choose_language.get()

    if language1 == "":
        tmsg.showerror("Language Translator", "Please fill the box.")
    else:
        t2.delete(1.0, END)
        language2_code = list(languages.keys())[list(languages.values()).index(language2)]
        translator = GoogleTranslator(source='auto', target=language2_code)
        output = translator.translate(language1)
        t2.insert(END, output)

def clear():
    t1.delete(1.0, END)
    t2.delete(1.0, END)

Label(root, text="Language Translator By Bicky", font="lucida 20 bold").grid(row=0, column=0, columnspan=3, pady=10)

img = ImageTk.PhotoImage(Image.open('translator.png'))
label = Label(image=img)
label.grid(row=1, column=0, pady=10, padx=10, columnspan=3)

str1 = StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=str1, state='readonly', font=('verdana', 10, 'bold'))
auto_detect['values'] = ('Auto Detect',)
auto_detect.grid(row=2, column=0, pady=10)
auto_detect.current(0)

str2 = StringVar()
choose_language = ttk.Combobox(root, textvariable=str2, state="readonly", font=('verdana', 10, 'bold'))
choose_language['values'] = list(languages.values())
choose_language.grid(row=2, column=2, pady=10)
choose_language.current(0)

t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE,font=("Helvetica", 14))
t1.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE,font=("Helvetica", 14))
t2.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

Button(root, text="Translate", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor="hand2", command=translate_text).grid(row=4, column=0, pady=5, columnspan=3)
Button(root, text="Clear", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor="hand2", command=clear).grid(row=5, column=0, pady=5, columnspan=3)

root.mainloop()
