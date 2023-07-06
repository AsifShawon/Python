# class Student:
#     ...


# def main():
#     student = get_studetnt()
#     print(f"{student.name} from {student.name}")


# def get_studetnt():
#     student = Student()  # "student" is an object of class "Student()"
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()


# -------------------------------------------------------------------------------


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "🐕"
            case _:
                return "🪄"
    
    # getter
    @property
    def house(self):
        return self._house

    @property
    def name(self):
        return self._name
    
    # setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)  # creates an object of current class and return it


def main():
    student = Student.get()
    print(f"{student.name} from {student.house}")
    # print(student)
    # print(student.charm())
        


if __name__ == "__main__":
    main()