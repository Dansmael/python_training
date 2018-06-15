
from model.contact import Contact
from random import randrange

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None


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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletions
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None


    def edit_first_link(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.edit_link_by_index(0)
        self.contact_cache = None


    def edit_link_by_index(self, contact, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('img[title="Edit"]')[index].click()
        # add new data
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()
        self.contact_cache = None


    def edit_by_details(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact - edit by details icon
        wd.find_element_by_css_selector('img[title="Details"]').click()
#       wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        wd.find_element_by_name("modifiy").click()
        # add new data
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
 #      return len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img"))
        return len(wd.find_elements_by_name("entry"))


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                self.contact_cache.append(Contact(id=id, last_name=lastname, first_name=firstname))
        return self.contact_cache


