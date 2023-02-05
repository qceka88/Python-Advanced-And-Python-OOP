3.	File Manipulator


Create a program that will receive commands until the command "End". The commands can be:
•	"Create-{file_name}" - Creates the given file with an empty content. 
If the file already exists, remove the existing text in it (as if the file is created again)
•	"Add-{file_name}-{content}" - Append the content and a new line after it.
If the file does not exist, create it, and add the content
•	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences
of the old string with the new string. If the file does not exist, print: "An error occurred"
•	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"



____________________________________________________________________________________________
Example

Input

Create-file.txt

Add-file.txt-First Line

Add-file.txt-Second Line

Replace-random.txt-Some-some

Replace-file.txt-First-1st

Replace-file.txt-Second-2nd

Delete-random.txt

Delete-file.txt

End


Explanation
The first command creates the empty file
After the first and second Add command, the content is:
First Line
Second Line
On the first Replace command, an error must occur
After the next two Replace commands, the content is:
1st Line
2nd Line
After the first Delete command, an error occurs
Finally, the 'file.txt' file is deleted
