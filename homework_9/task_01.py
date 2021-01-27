# Создать три класса, описывающие реальные объекты. Каждый класс должен содержать минимум три
# приватных атрибута, конструктор, геттеры и сеттеры для каждого атрибута, два метода

class Secialists:
    def __init__(self, name, age, specialty, education, company) -> None:
        self.__name = name
        self.age = age
        self.__specialty = specialty
        self.__education = education
        self.company = company
    @property                               # getter for attribute name
    def my_name(self):
        return self.__name

    @my_name.setter                         # setter for attribute name
    def my_name(self, name):
        self.__name = name

    @property                               # getter for attribute age
    def my_age(self):
        return self.age

    @my_age.setter                          # setter for attribute age
    def my_age(self, age):
        self.age = age

    @property                               # getter for attribute specialty
    def my_specialty(self):
        return self.__specialty

    @my_specialty.setter                    # setter for attribute specialty
    def my_specialty(self, specialty):
        self.__specialty = specialty

    @property                               # getter for attribute education
    def my_education(self):
        return self.__education

    @my_education.setter                    # setter for attribute education
    def my_education(self, education):
        self.__education = education

    @property                               # getter for attribute company
    def my_company(self):
        return self.company

    @my_company.setter                      # setter for attribute company
    def my_company(self, company):
        self.company = company

    def greeting(self) -> str:
        return print(f'Hi, my name is {self.__name}, I {self.__specialty}, my age {self.age}, work in {self.company}')

    def sum(self) -> int:
        print('I can sum up 2 numbers, please enter them')
        num1 = int(input('enter the number1: '))
        num2 = int(input('enter the number2: '))
        return num1 + num2

class Bird:
    def __init__(self, name: str, kind:str, color:str, fly:bool = True) -> None:
        self.name = name
        self.__kind = kind
        self.__color = color
        self.__fly = fly

    @property
    def my_name(self):
        return self.name

    @my_name.setter
    def my_name(self, name):
        self.name = name

    @property
    def bird_kind(self):
        return self.__kind

    @bird_kind.setter
    def bird_kind(self, kind:str):
        self.__kind = kind

    @property
    def bird_color(self):
        return self.__color

    @bird_color.setter
    def bird_color(self, color:str):
        self.__color = color

    @property
    def bird_fly(self):
        return self.__fly

    @bird_fly.setter
    def bird_fly(self, fly:bool):
        self.__fly = fly

    def greeting_bird(self):
        """this is a greeting method"""
        print(f'Hello i am a bird {self.name}')

    def flying(self):
        """this method will show if the bird can fly"""
        if self.__fly == True:
            print('I can fly')
        else:
            print('I can not fly')

class Fruct:
    def __init__(self, name: str, form: str, color: str, taste: str, price: int) -> None:
        self.name = name
        self.__form = form
        self.__color = color
        self.__taste = taste
        self.price = price

    @property
    def my_name(self):
        return self.name

    @my_name.setter
    def my_name(self, name):
        self.name = name

    @property
    def fruct_form(self):
        return self.__form

    @fruct_form.setter
    def fruct_form(self, form):
        self.__form = form

    @property
    def fruct_color(self):
        return self.__color

    @fruct_color.setter
    def fruct_color(self, color):
        self.__color = color

    @property
    def fruct_taste(self):
        return self.__taste

    @fruct_taste.setter
    def fruct_taste(self, taste):
        self.__taste = taste

    @property
    def fruct_price(self):
        return self.price

    @fruct_price.setter
    def fruct_price(self, price):
        self.price = price

    def greeting_fruct(self):
        """this is a greeting method"""
        print(f'Hello i am a fruct {self.name}')

    def price_fruct(self):
        """this method will show the price category of the fruit"""
        if self.price > 20:
            print('Im an expensive fruit')
        else:
            print('Im a cheap fruit')


def main() -> str:
    spec = Secialists('Alex', 23, 'teacher', 'sr-sp', 'School №3')
    spec.greeting()
    print(spec.my_education)
    print(spec.sum())

    spec.my_name = 'Joni'
    spec.my_specialty = 'director'
    spec.age = 38
    spec.my_education = 'vh'
    spec.greeting()
    print(spec.my_education)

    return print('Done')


if __name__ == '__main__':
    main()





