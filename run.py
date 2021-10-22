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
  print ("Hello, Welcome here")
  user_name= input()
  print