import random
import csv
from datetime import datetime, timedelta
import secrets
import string

def generate_random_birthdate(start_year=1980, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - (today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day))
    return age

def generate_random_password(length=5):
    alphabet = string.digits + '@#$%!&_-?'
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def data(final_data):
    # Generate mobile number
    mobile_number = int(f"{random.choice([6, 8, 9])}{random.randint(100000000, 999999999)}")
    
    # Generate gender
    gender = random.choice(['male', 'female'])
    
    # Generate name and surname based on gender
    male_names = ['Aarav', 'Amit', 'Arjun', 'Ishaan', 'Rahul', 'Varun', 'Yash', 'Amitabh', 'Kunal', 'Pranav', 'Vivek', 'Aryan', 'Hritik', 'Manish', 'Siddharth', 'Akash', 'Gaurav', 'Mohan', 'Parth', 'Ramesh', 'Vijay', 'Dinesh', 'Gopal', 'Prashant', 'Ravi', 'Sandeep', 'Vikram', 'Deepak', 'Harish', 'Rohan', 'Rajesh', 'Vishal', 'Shivam', 'Vijay', 'Shubham', 'Aakash', 'Raj', 'Arun', 'Rajat', 'Karan', 'Rajesh', 'Rishi', 'Rajiv', 'Abhinav', 'Rahul', 'Kamal', 'Vinay', 'Suresh', 'Sanjay']
    female_names = ['Ananya', 'Divya', 'Kavya', 'Sarika', 'Tanvi', 'Aditi', 'Anjali', 'Maya', 'Shreya', 'Zoya', 'Deepika', 'Kritika', 'Pooja', 'Riya', 'Chandni', 'Ganesh', 'Kamala', 'Manisha', 'Nisha', 'Uma', 'Yogita', 'Bhavna', 'Hema', 'Jyoti', 'Kiran', 'Neeta', 'Suman', 'Yogesh', 'Akanksha', 'Ishita', 'Shalini', 'Swati', 'Sunita', 'Preeti', 'Neelam', 'Anita', 'Ritu', 'Rashmi', 'Sangeeta', 'Pallavi','Rajani', 'Mamta', 'Indira', 'Lakshmi', 'Radha', 'Savita', 'Geeta', 'Nandini', 'Kiran', 'Vandana']
    surnames = ['Patel', 'Sharma', 'Gupta', 'Kumar', 'Singh', 'Das', 'Patil', 'Chatterjee', 'Reddy', 'Naidu', 'Mukherjee', 'Rao', 'Joshi', 'Desai', 'Banerjee', 'Mishra', 'Malhotra', 'Mehta', 'Sinha', 'Saxena', 'Verma','Pandey', 'Shah', 'Thakur', 'Jain', 'Srivastava', 'Choudhury', 'Chauhan', 'Bhat', 'Seth', 'Pillai','Acharya', 'Agarwal', 'Biswas', 'Chopra', 'Datta', 'Dubey', 'Ganguly', 'Ghosh', 'Kapoor', 'Khanna','Lal', 'Mahajan', 'Nair', 'Panicker', 'Raman', 'Sen', 'Tiwari', 'Trivedi', 'Varghese', 'Yadav','Shroff', 'Parekh', 'Jha', 'Choudhary', 'Dasgupta', 'Shinde', 'Pawar', 'Goswami', 'Nanda', 'Sengupta', 'Rathod', 'Prajapati', 'Chauhan', 'Solanki', 'Rana', 'Thakkar', 'Vaghela', 'Doshi', 'Bhattacharya', 'Meena']
    name, surname = random.choice(male_names) if gender == 'male' else random.choice(female_names), random.choice(surnames)
    
    # Generate email
    email = f"{name.lower()}{surname.lower()}{random.choice([i+1 for i in range(30)])}@gmail.com"
    
    # Generate birthdate
    date = generate_random_birthdate()
    birthdate = date.strftime("%Y-%m-%d")
    
    # Generate Age
    age = calculate_age(date)
    
    # Generate password
    password = name+random.choice('@#-~_')+generate_random_password()
    
    # Return data based on user's choice
    return_data = {}
    for data_type in final_data:
        if data_type == 'Name':return_data['Name'] = name
        elif data_type == 'Surname':return_data['Surname'] = surname
        elif data_type == 'Gender':return_data['Gender'] = gender
        elif data_type == 'Mobile Number':return_data['Mobile Number'] = mobile_number
        elif data_type == 'Email':return_data['Email'] = email
        elif data_type == 'Birthdate':return_data['Birthdate'] = birthdate
        elif data_type == 'Age':return_data['Age'] = age
        elif data_type == 'Password':return_data['Password'] = password
    return return_data

def random_data_to_sql(final_data, numbers):
    with open("random_generated_data.sql", 'w') as sql:
        sql.write(f"INSERT INTO `table_name` (")
        for i, key in enumerate(final_data):
            sql.write(f"`{key}`")
            if i < len(final_data) - 1:
                sql.write(', ')
        sql.write(f") \nVALUES \n")
        
        for _ in range(numbers):
            # Get random data
            row_data = data(final_data)
            # Generate SQL INSERT statement
            sql.write("\t(")
            for i, key in enumerate(final_data):
                if isinstance(row_data[key], str):
                    sql.write(f"'{row_data[key]}'")
                else:
                    sql.write(f"{row_data[key]}")
                if i < len(final_data) - 1:
                    sql.write(', ')
            sql.write(")")
            sql.write(";") if (_+1 == numbers) else sql.write(",\n")

def random_data_to_csv(final_data, numbers):
    with open('random_generated_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(final_data)
        for _ in range(numbers):
            # Get random data
            row_data = data(final_data)
            # Write data to CSV file
            writer.writerow([row_data[key] for key in final_data])
