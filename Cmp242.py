from abc import ABC, abstractmethod

class Cmp242(ABC) :
    def__init__(self, grade):
        self.grade = None
        self.grade = grade

    def grade(self):
        return self.__grade

    def grade(self, value):
        if self •_grade is not None:
            raise AttributeError("Grade cannot be changed.")
        if 0 <= value <= 100:
            self.__grade = value
        else:
            raise ValueError ("Grade must be between 0 and 100.")

    @classmethod 
    def prepare__ppt(self):
    pass

    class GroupPresentation(Cmp242) :
        def prepare__ppt(self) :
            return f"Preparing group presentation. Grade: "

    class GroupScore(Cmp242) :
        def prepare__ppt(self):
            return f"Preparing score report. Grade: {self.grade}

    def make_presentation(presentation):
        print(presentation.prepare__ppt())
