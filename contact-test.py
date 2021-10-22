import unittest
import pyperclip
from contact import Contact

class TestContact(unittest.TestCase):
  def setUp(self): #method to create new instance of Contact
    self.new_contact = Contact("Levy", "Omolo", "0715506018", "test@user.com") #instance variable

  def test_init(self):
    self.assertEqual(self.new_contact.first_name, "Levy")
    self.assertEqual(self.new_contact.last_name, "Omolo")
    self.assertEqual(self.new_contact.phone_number, "0715506018")
    self.assertEqual(self.new_contact.email, "test@user.com")

  def test_save_contact(self):
    self.new_contact.save_contact()
    self.assertEqual(len(Contact.contact_list),1)

  def tearDown(self):
    Contact.contact_list = []

  def test_save_multiple_contact(self):
    self.new_contact.save_contact()
    test_contact = Contact("Test", "user", "0715506018", "test@user.com")
    test_contact.save_contact()
    self.assertEqual(len(Contact.contact_list),2)

  def test_delete_contact(self):
    self.new_contact.save_contact()
    test_contact = Contact("Test", "user", "0715506018", "test@user.com")
    test_contact.save_contact()

    self.new_contact.delete_contact()
    self.assertEqual(len(Contact.contact_list),1)

  def test_find_contact_by_number(self):
    self.new_contact.save_contact()
    #test_contact.save_contact()
    test_contact = Contact("Test", "user", "0715506018", "test@user.com")
    test_contact.save_contact()

    found_contact = Contact.find_by_number("0715506018")
    self.assertEqual(found_contact.email, test_contact.email)

  def test_contact_exist(self):
    test_contact = Contact("Test", "user", "0715506018", "test@user.com")
    self.new_contact.save_contact()
    contact_exist = Contact.contact_exist("0715506018")
    self.assertTrue(contact_exist)
    
  def test_display_all_contacts(self):
    self.assertEqual(Contact.display_contacts(),Contact.contact_list)

  def test_copy_email(self):
    test_contact = Contact("kaka", "mama", "0748939901", "kakama@user.com")
    self.new_contact.save_contact()
    Contact.copy_email("0748939901")
    self.assertEqual(self.new_contact.email, pyperclip.paste())

if __name__ == '__main__':
  unittest.main()