
from model.contact import Contact
import re

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
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)


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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(id=id, last_name=lastname, first_name=firstname, address=address,
                                                  all_phones_from_homepage=all_phones,
                                                  all_mails_from_homepage=all_mails))
        return self.contact_cache


    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id, address=address,
                       email=email, email2=email2, email3=email3,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)


    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)",text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # submit deletions
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None


    def edit_link_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//a[contains(@href, %s) and contains(@href, 'edit.php?id=')]" % id).click()
        # add new data
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()
        self.contact_cache = None


    def select_group_to_view_contacts(self,group_id):
        wd = self.app.wd
        wd.find_element_by_css_selector('select[name="group"]>option[value="%s"]' % group_id).click()

    def get_contact_list_from_group_page(self, group_id):
        if self.contact_cache is None:
            wd = self.app.wd
            self.select_group_to_view_contacts(group_id)
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(id=id, last_name=lastname, first_name=firstname, address=address,
                                                      all_phones_from_homepage=all_phones,
                                                      all_mails_from_homepage=all_mails))
        return self.contact_cache


    def add_contact_to_group(self,contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        wd.find_element_by_css_selector('select[name="to_group"]>option[value="%s"]' % group_id).click()
        wd.find_element_by_css_selector("input[value='Add to']").click()
        self.app.open_home_page()
        self.contact_cache = None


    def del_contact_from_group(self,contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector('select[name="group"]>option[value="%s"]' % group_id).click()
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        wd.find_element_by_css_selector("input[name='remove']").click()
        self.app.open_home_page()
        self.contact_cache = None