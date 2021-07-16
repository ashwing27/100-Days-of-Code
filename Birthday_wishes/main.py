import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day
today = (month,day)

birthdays = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

if (month, day) in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

my_email = "ashpython2789@gmail.com"
password = "python12345"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs=my_email,
                        msg=f"Subject:Happy Birthday!\n\n{contents}")



