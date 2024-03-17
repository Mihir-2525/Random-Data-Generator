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

def generate_random_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def data():
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
    birthdate = generate_random_birthdate()
    
    return {'Name': name, 'Surname': surname, 'Gender': gender, 'Email': email, 'Mobile Number': mobile_number, 'Birthdate': birthdate.strftime("%Y-%m-%d"), 'Age': calculate_age(birthdate), 'Password': generate_random_password()}

def random_data_to_sql(numbers):
    with open("random_generated_data.sql", 'w') as sql:
        sql.write(f"INSERT INTO `table_name` (`name`, `surname`, `gender`, `mobile_number`, `email`, `birthdate`, `age`) \nVALUES \n")
        for _ in range(numbers):
            # Get random data
            row_data = data()
            # Generate SQL INSERT statement
            sql.write(f"\t('{row_data['Name']}', '{row_data['Surname']}', '{row_data['Gender']}', {row_data['Mobile Number']}, '{row_data['Email']}', '{row_data['Birthdate']}', {row_data['Age']}, `{row_data['Password']}`)")
            sql.write(";") if (_+1 == numbers) else sql.write(",\n")

def random_data_to_csv(numbers):
    with open('random_generated_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Surname', 'Gender', 'Mobile Number', 'Email', 'Birthdate', 'Age', 'Password'])
        for _ in range(numbers):
            # Get random data
            row_data = data()
            # Write data to CSV file
            writer.writerow([row_data['Name'], row_data['Surname'], row_data['Gender'], row_data['Mobile Number'], row_data['Email'], row_data['Birthdate'], row_data['Age'], row_data['Password']])

def main():
    file_format = input("Enter the file format (sql/csv): ").lower()
    while file_format not in ['sql', 'csv']:
        print("Invalid file format!")
        file_format = input("Enter the file format (sql/csv): ").lower()
    
    number_of_data = int(input("Enter the number of data to generate: "))
    
    if file_format == 'sql':
        random_data_to_sql(number_of_data)
        print(f"{number_of_data} data entries generated and stored in 'random_generated_data.sql'")
    elif file_format == 'csv':
        random_data_to_csv(number_of_data)
        print(f"{number_of_data} data entries generated and stored in 'random_generated_data.csv'")

if __name__ == "__main__":
    main()
