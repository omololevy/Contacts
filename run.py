#!/usr/bin/env python3.9

from contact import Contact

def create_contact(fname, lname, phone, email):
  new_contact = Contact(fname, lname, phone, email)
  return new_contact

def save_contacts(contact):
  contact.save_contact()

def delete_contact(contact):
  contact.delete_contact()

def find_contact(number):
  return Contact.find_by_number(number)

def check_existing_contacts(number):
  return Contact.contact_exist(number)

def display_contacts():
  return Contact.display_contacts()


def main():
  user_name = input ('Hello, Welcome to contact list. What\'s your name?\n')
 
  print(f"Hi {user_name}, what would you like to do?")
  print("\n")

  while True:
    print("Use these short codes to perform an action: \n cc -----> to create a new contact.\n dc -----> to display contact.\n fc -----> to find a contact\n ex -----> to exit the contact list\n")
    
    short_code = input().lower()

    if short_code == "cc":
      print("New Contact")
      print("-" *10)
      fname = input("Enter first name:\n")
      lname = input("Enter the last name:\n")
      phone = input("Phone number:\n")
      email = input("Enter the email address:\n")

      save_contacts(create_contact(fname, lname, phone, email))
      print(f"New Contact {fname} {lname} created successfully \n")

      
    elif short_code == "dc":
      if display_contacts():
        print("Here is a list of all your contacts\n")

        for contact in display_contacts():
          print(f"{contact.first_name} {contact.last_name} ..... {contact.phone_number}\n")

      else:
        print("Your don't have any contact saved yet.\n\n")


    elif short_code == "fc":
      search_number = input("Enter the number you want to search:\n")
      if check_existing_contacts(search_number):
        search_contact = find_contact(search_number)
        print(f"{search_contact.first_name} {search_contact.last_name} ")
        print("-" * 20)
        print(f"Phone number ....... {search_contact.phone_number}")
        print(f"Email address ....... {email}\n\n")

      else:
        print("That contact does not exist!")


    elif short_code == "ex":
      print("Bye!")
      break

    else:
      print("Invalid choice! Use the short codes!")

if __name__ == '__main__':
    main()
    