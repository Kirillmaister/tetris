class Human():
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def print_info(self):
        print("name: " + self.name)
        print("age:", self.age)
        print("phone: " + self.phone)

    def set_phone(self, new_phone):
        self.phone = new_phone


class Student(Human):
    def __init__(self, name, age, phone, form):
        super().__init__(name, age, phone)
        self.form = form

    def print_info(self):
        super().print_info()
        print("form:", self.form, "\n")

    def set_form(self, new_form):
        self.form = new_form


class Teacher(Human):
    def __init__(self, name, age, phone, subj):
        super().__init__(name, age, phone)
        self.subj = subj

    def print_info(self):
        super().print_info()
        print("subj: " + self.subj + "\n")

    def set_subj(self, new_subj):
        self.subj = new_subj


student1 = Student("Vova", 14, "+38000000000", 9)

teacher1 = Teacher("Nikol", 20, "+388888888", "Python")
teacher1.print_info()

teacher1.set_subj("C++")
teacher1.print_info()

teacher1.set_phone("+3822222222")

teacher1.print_info()