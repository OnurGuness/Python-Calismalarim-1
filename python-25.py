# mainloop'u anlamak
# çoklu pencereler ile çalış

import tkinter as tk

pencere1 = tk.Tk()
pencere1.title("Birinci")
pencere1.configure(bg="red")

pencere2 = tk.Tk()
pencere2.title("İkinci")
pencere2.configure(bg="yellow")
pencere3 = tk.Tk()
pencere3.title("Üçüncü")
pencere3.configure(bg="blue")
pencere3.mainloop()

pencere2.mainloop()



pencere1.mainloop()








