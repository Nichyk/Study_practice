# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line.

# Does the new file show up in the directory where you ran your scripts?
# Відповідь: Так, файл з'явиться.
# What if you add a different directory path to the filename passed to open?
# Відповідь: Якщо вказати коректний шлях до файлу, то все буде ок.

with open('myfile.txt', 'w') as f:
    f.write('Hello file world!\n''Another file world string')

with open('C:\\Users\\nichy\\Study\\BeetrootAcademy\\RemoteDirectory\\myfile.txt') as f:
    text = f.read()
    print(text)

# Працює через cmd
