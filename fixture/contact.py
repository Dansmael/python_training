
from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.first_phone)
        self.change_field_value("mobile", contact.second_phone)
        self.change_field_value("email", contact.first_mail)
        self.change_field_value("email2", contact.second_mail)


    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletions
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()


    def edit_link(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact - edit by edit icon
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # add new data
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()


    def edit_by_details(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact - edit by details icon
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        wd.find_element_by_name("modifiy").click()
        # add new data
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img"))


    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            lastname = element.find_element_by_xpath(".//td[2]").text
            firstname = element.find_element_by_xpath(".//td[3]").text
            contacts.append(Contact(id=id, last_name=lastname, first_name=firstname))
        return contacts


