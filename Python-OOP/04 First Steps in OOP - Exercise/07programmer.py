class Programmer:

    def __init__(self, *args):
        [self.name,
         self.language,
         self.skills
         ] = args

    def watch_course(self, course_name, language, skills_earned):
        if language != self.language:
            return f"{self.name} does not know {language}"

        self.skills += skills_earned
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language, skills_needed):
        if new_language == self.language:
            return f"{self.name} already knows {new_language}"

        if skills_needed > self.skills:
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"

        message = f"{self.name} switched from {self.language} to {new_language}"
        self.language = new_language
        return message


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
