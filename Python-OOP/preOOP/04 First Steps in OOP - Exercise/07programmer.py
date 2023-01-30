class Programmer:

    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if skills_needed <= self.skills:
            if new_language == self.language:
                return f"{self.name} already knows {new_language}"
            elif new_language != self.language:
                previous_language = self.language
                self.language = new_language
                return f"{self.name} switched from {previous_language} to {new_language}"
        skills_needed = skills_needed - self.skills
        return f"{self.name} needs {skills_needed} more skills"



# Part below is part from automatic judge system from SoftUni
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))


#################################### TASK CONDITION ############################
'''
          7.	Programmer
Create a class called Programmer. Upon initialization it should receive name (string), 
language (string), skills (integer). The class should have two methods:
-	watch_course(course_name, language, skills_earned)
o	If the programmer's language is the same as the one on the course, increase his 
skills with the given amount and return a message "{name} watched {course_name}".
o	Otherwise return "{name} does not know {language}".
-	change_language(new_language, skills_needed) 
o	If the programmer has the skills and the new language is not the same as his,
change his language to the new one and return "{name} switched from {previous_language} to {new_language}".
o	If the programmer has the skills, but the given language is
 equal to his return "{name} already knows {language}".
o	In the last case the programmer does not have the skills, 
so return "{name} needs {needed_skills} more skills" and do not change his language
Submit only the class in the judge system.


_______________________________________________
Example

Test Code	(no input data in this task)

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

Output
John does not know Python
John already knows Java
John needs 50 more skills
John watched Java: zero to hero
John switched from Java to Python
John watched Python Masterclass

'''
