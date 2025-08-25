
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from langchain_gigachat.chat_models import GigaChat

model = GigaChat(
    model="GigaChat-2-Max",
    verify_ssl_certs=False,
    credentials="=="
)

###сделай минимальный интерфейс на tkinter (без классов) для ввода файла и выводы инфы о компании.

selected_file = None

def select_file():
    global selected_file
    file_path = filedialog.askopenfilename(
        title="Выберите изображение",
        filetypes=[("Изображения", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    if file_path:
        file_label.config(text=f"Файл: {file_path}")
        analyze_button.config(state="normal")
        selected_file = file_path

def analyze_image():
    try:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Анализируем изображение...")
        root.update()
        
        with open(selected_file, "rb") as image_file:
            file_uploaded_id = model.upload_file(image_file).id_
        
        message = {
            "role": "user",
            "content": "Распознай текст с этого изображения. Найди в нем название компании(name), телефоны(phones), email, адреса и сохрани их в формате JSON: {\"name\": \"\", \"phones\": [], \"email\": \"\", \"address\": \"\", \"description\": \"\"}. Верни только JSON без дополнительного текста.",
            "attachments": [file_uploaded_id]
        }
        
        response = model.invoke([message])
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, response.content)
        
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

root = tk.Tk()
root.title("Анализ информации о компании")
root.geometry("600x500")

select_button = tk.Button(root, text="Выбрать изображение", command=select_file)
select_button.pack(pady=10)

file_label = tk.Label(root, text="Файл не выбран")
file_label.pack(pady=5)

analyze_button = tk.Button(root, text="Анализировать", command=analyze_image, state="disabled")
analyze_button.pack(pady=10)

tk.Label(root, text="Результат анализа:").pack(pady=(20,5))
result_text = scrolledtext.ScrolledText(root, width=70, height=20)
result_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()


