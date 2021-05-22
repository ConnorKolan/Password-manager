import csv
import difflib
import pygetwindow._pygetwindow_win


def getTitle():
    x = pygetwindow.getWindowsWithTitle("Opera")

    i = 0
    newString = ""
    for entry in x:
        for char in str(entry):
            if i < str(entry).find("title"):
                i += 1
                continue
            else:
                newString = newString + char
                i += 1
    return str(newString)               # returns "title="(1) Python Education – Opera">"


def extractWebsite():
    url = getTitle()
    with open('passwörter.csv', newline='') as csvFile:
        csv_file_reader = csv.reader(csvFile, delimiter=';', quotechar='|')
        for entry in csv_file_reader:
            if entry[0].lower() in url.lower():
                return entry            # looks a every website in my csv file and trys to match it with the title


def print_everything():
    with open('passwörter.csv', newline='') as csvFile:
        csv_file_reader = csv.reader(csvFile, delimiter=';', quotechar='|')
        for row in csv_file_reader:
            for entry in row:
                print(entry)
            print("\n")


class LoginData:
    def __init__(self, inner_website):
        self.website = str(inner_website)

    def get_login_data(self):
        with open('passwörter.csv', newline='') as csvFile:
            csv_file_reader = csv.reader(csvFile, delimiter=';', quotechar='|')
            for row in csv_file_reader:
                if difflib.get_close_matches(self.website.upper(), [str(row[0]).upper()]):
                    for entry in row:
                        print(entry)

    '''
    get_login_data:
        jede reihe im Dokument zu einer Liste dann durch difflib in dieser Liste nach ähnlichen 
    '''

    def write_login_data(self, inner_email, inner_username, inner_password):
        with open("passwörter.csv", "a", newline='') as csvFile:
            csv_file_writer = csv.writer(csvFile, delimiter=';', quotechar='|', quoting=csv.QUOTE_ALL)
            csv_file_writer.writerow([self.website, inner_email, inner_username, inner_password])

    def rewrite_login_data(self):
        with open("passwörter.csv", "r", newline='') as csvFile:
            csv_file_reader = csv.reader(csvFile, delimiter=';', quotechar='|')
            login_data_list = []
            for row in csv_file_reader:
                if str(row[0]).upper() == self.website.upper():
                    for entry in row:
                        print(entry)
                    continue
                login_data_list.append(row)

            list_to_append_to_login_data_list = []

            inner_email = input("\nBitte Email eingeben:\n")
            inner_username = input("\nBitte Username eingeben:\n")
            inner_password = input("\nBitte Passwort eingeben:\n")

            list_to_append_to_login_data_list.extend([self.website, inner_email, inner_username, inner_password])

            login_data_list.append(list_to_append_to_login_data_list)

            csvFile.close()

            with open("passwörter.csv", "w", newline='') as csvFile:
                csv_file_writer = csv.writer(csvFile, delimiter=';', quotechar='|', quoting=csv.QUOTE_ALL)
                for row in login_data_list:
                    csv_file_writer.writerow(row)
            csvFile.close()


runLoop = True

while runLoop:
    userInput = int(input("\n1 = Mit Browser suchen\n2 = Suchen\n3 = Hinzufügen\n4 = Liste zeigen\n5 = Eintrag bearbeiten\n10 = Beenden\n"))
    if userInput == 1:
        if not extractWebsite():
            print("")
            print("Website nicht bekannt")
        else:
            print("")
            for entry in extractWebsite():
                print(entry)
    elif userInput == 2:
        loginDataInput = LoginData(input("Bitte Website eingeben:\n"))
        loginDataInput.get_login_data()

    elif userInput == 3:
        website = input("Bitte Website eingeben:\n")
        email = input("Bitte Email eingeben:\n")
        username = input("Bitte Username eingeben:\n")
        password = input("Bitte Passwort eingeben:\n")

        loginDataInput = LoginData(website)
        loginDataInput.write_login_data(email, username, password)

    elif userInput == 4:
        print_everything()

    elif userInput == 5:
        loginDataInput = LoginData(input("Bitte Website eingeben:\n"))
        loginDataInput.rewrite_login_data()

    elif userInput == 10:
        runLoop = False
