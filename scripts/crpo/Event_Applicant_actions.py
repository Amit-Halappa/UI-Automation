import crpo_login
import page_elements
import time
from selenium.webdriver.common.keys import Keys
import webdriver_wait
import test_data_inputpath


class ApplicantActions(crpo_login.CrpoLogin, webdriver_wait.WebDriverElementWait):
    def __init__(self):
        super(ApplicantActions, self).__init__()
        self.attachment = test_data_inputpath.attachments['attachment']
        self.ui_event_tab = []
        self.ui_event_advance_search = []
        self.ui_event_get_by_id = []
        self.ui_event_floating_actions = []
        self.ui_event_applicants = []
        self.ui_candidate_status_changed = []
        self.ui_compose_mail = []
        self.ui_applicant_advance_search = []
        self.ui_candidate_get_by_id = []
        self.ui_candidate_tab = []
        self.ui_candidate_advance_search = []
        self.ui_tag_to_event = []
        self.ui_send_sms = []
        self.ui_tag_to_job = []
        self.ui_untag_applicant = []
        self.ui_more_action = []
        self.ui_send_rl = []
        self.ui_send_ac = []
        self.ui_single_pdf = []
        self.ui_generate_docket = []
        self.ui_upload_attachment = []
        self.ui_change_bu_remove = []
        self.ui_change_bu_save = []

    def event_advance_search(self):
        # --------------------------------- event details ----------------------------------------------------------
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
        self.xpath.click()
        self.ui_event_tab = 'Pass'

        time.sleep(5)
        self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
        self.xpath.click()

        self.name_element_webdriver_wait(page_elements.event['event_names'])
        self.name.send_keys('Sprint_{}'.format(self.sprint_version))

        self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
        self.xpath.click()
        self.ui_event_advance_search = 'Pass'

        print "-------------------- Event Advance search ------------------------"

    def event_get_by_id(self):
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
        self.xpath.click()
        self.ui_event_get_by_id = 'Pass'

    def event_applicants(self, candidate_name):
        time.sleep(2)
        # --------------------------------- event floating actions -------------------------------------------------
        self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
        self.xpath.click()
        self.ui_event_floating_actions = 'Pass'

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.event['View_Applicants'])
        self.xpath.click()
        self.ui_event_applicants = 'Pass'
        print "-------------------- Floating action ------------------------"

        self.event_applicant_advance_search(candidate_name)

    def event_change_applicant_status(self):
        # --------------------------- Change Applicant Status to Schedule ------------------------------------------
        time.sleep(3)
        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.event['Change_applicant_status'])
        time.sleep(2)
        self.xpath.click()

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.event['change_stage'])
        self.xpath.send_keys('Group Discussion')

        self.x_path_element_webdriver_wait(page_elements.event['change_status'])
        self.xpath.send_keys('Shortlisted')

        self.x_path_element_webdriver_wait(page_elements.event['comment'])
        self.xpath.send_keys('Changed by UI Automation')

        self.x_path_element_webdriver_wait(page_elements.event['change_button'])
        self.xpath.click()
        time.sleep(3)

    def event_compose_mail(self):
        # --------------------------- Compose Mail to candidate ------------------------------------------
        time.sleep(3)
        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['Compose_Mail'])
        time.sleep(2)
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['mail_subject'])
        self.xpath.send_keys('UI Automation Mail')

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['mail_content'])
        self.xpath.send_keys('All Copy rights from Hirepro')

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['mail_send'])
        self.xpath.click()
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['Compose_Mail_notifier'])
        if self.xpath.text == 'Mail will be send asynchronously':
            self.ui_compose_mail = 'Pass'
            print "-------------------- Compose Mail to candidate ------------------------"

    def event_send_sms(self):
        # --------------------------- SMS to candidate ------------------------------------------
        time.sleep(3)
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['send_sms'])
        time.sleep(2)
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['sms_template'])
        self.xpath.send_keys('SMSNotify_Applicant_Interview_Slot')
        self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['send_sms_button'])
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['send_sms_ui_notifier'])
        if 'SMS sent successfully' in self.xpath.text:
            self.ui_send_sms = 'Pass'
            print "-------------------- Send SMS to candidate ------------------------"

    def tag_to_job(self, candidate_name):
        self.event_applicant_advance_search(candidate_name)
        time.sleep(2)
        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['Tag_to_job'])
        time.sleep(2)
        self.xpath.click()
        self.x_path_element_webdriver_wait(page_elements.candidate['Job_name'])
        time.sleep(1.3)
        self.xpath.send_keys('Sprint_{}'.format(self.sprint_version))
        self.xpath.send_keys(Keys.ARROW_DOWN)
        self.xpath.send_keys(Keys.ENTER)

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.candidate['Tag_to_event'])
        self.xpath.click()
        time.sleep(2)

    def event_applicant_advance_search(self, candidate_name):
        # ------------------------------- Applicant Advance search -------------------------------------------------
        time.sleep(3)
        self.x_path_element_webdriver_wait(page_elements.event['applicant_advance_search'])
        time.sleep(3)
        self.xpath.click()

        self.name_element_webdriver_wait(page_elements.event['applicant_name'])
        self.name.send_keys('Sprint_{}'.format(candidate_name))

        self.x_path_element_webdriver_wait(page_elements.event['applicant_search_button'])
        time.sleep(2)
        self.xpath.click()
        self.xpath.send_keys(Keys.END)

        print "-------------------- Applicant Advance search ------------------------"
        self.ui_applicant_advance_search = 'Pass'

    def reset_applicant_search(self):
        time.sleep(3)
        self.x_path_element_webdriver_wait(page_elements.event['reset_applicant_search'])
        self.xpath.click()

        # time.sleep(3)
        # self.x_path_element_webdriver_wait(page_elements.event['applicant_advance_search'])
        # self.xpath.click()

    def candidate_get_by_id(self, status):
        # --------------------------- Applicant Get By Id ----------------------------------------------------------

        time.sleep(5)
        if 'Sprint' in status:
            self.x_path_element_webdriver_wait(page_elements.event['applicant_getbyid'].format(status))
            self.xpath.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            self.x_path_element_webdriver_wait(
                page_elements.event['applicant_getbyid'].format('Sprint_{}'.format(self.sprint_version)))
            self.xpath.click()
            self.driver.switch_to.window(self.driver.window_handles[1])

        current_status = self.driver.find_element_by_xpath(
            page_elements.event['current_status'].format(status))

        job = self.driver.find_element_by_xpath(page_elements.candidate_get_by['job'])

        if current_status.text == status:
            print "-------------------- Candidate/Applicant status changed " \
                  "to {} successfully -----------------".format(status)
            self.ui_candidate_status_changed = 'Pass'
        elif self.sprint_version in job.text:
            print "-------------------- Candidate/Applicant tagged " \
                  "to {} successfully -----------------".format(status)
            self.ui_tag_to_job = 'Pass'
        self.ui_candidate_get_by_id = 'Pass'
        time.sleep(3)
        self.browser_close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def untag_applicants(self):
        self.reset_applicant_search()
        self.event_applicant_advance_search(self.sprint_version)
        time.sleep(2)
        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['Untag_applicant'])
        time.sleep(2)
        self.xpath.click()
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['untag_ok'])
        self.xpath.click()
        self.ui_untag_applicant = 'Pass'

    def more(self):
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['more'])
        self.xpath.click()
        self.ui_more_action = 'Pass'

    def registration_link(self):
        self.reset_applicant_search()
        self.event_applicant_advance_search(self.sprint_version)

        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.more()

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['send_rl'])
        self.xpath.click()
        time.sleep(1.2)
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['untag_ok'])
        self.xpath.click()
        self.ui_send_rl = 'Pass'
        print('----------------- Registration Link sent ----------------')

    def admit_card(self):
        self.reset_applicant_search()
        self.event_applicant_advance_search(self.sprint_version)

        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.more()

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['send_ac'])
        self.xpath.click()
        time.sleep(1.2)
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['untag_ok'])
        self.xpath.click()
        self.ui_send_ac = 'Pass'
        print('------------------- Admit Card sent -------------------')

    def single_pdf(self):
        self.reset_applicant_search()
        self.event_applicant_advance_search(self.sprint_version)

        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.more()
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['single_PDF'])
        self.xpath.click()
        self.ui_single_pdf = 'Pass'
        time.sleep(1.2)
        print('------------------- Single PDF -----------------')

    def generate_docket(self):
        self.more()
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['generate_docket'])
        self.xpath.click()
        self.ui_generate_docket = 'Pass'
        time.sleep(1.2)
        print('------------------- Generate Docket -----------------')

    def upload_attachment(self):
        self.more()
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['upload_attachment'])
        self.xpath.click()
        time.sleep(3)

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['upload_file'])
        time.sleep(2)
        self.xpath.send_keys(self.attachment)

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['save'])
        self.xpath.click()
        self.ui_upload_attachment = 'Pass'
        time.sleep(2)
        print('------------------- Upload Attachment -----------------')

    def change_bu_remove(self):

        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.more()
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['change_BU'])
        self.xpath.click()
        time.sleep(2)

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['remove'])
        self.xpath.click()
        print('------------------- BU Removed -----------------')
        self.ui_change_bu_remove = 'Pass'
        time.sleep(3)

    def change_bu_save(self):

        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.more()
        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['change_BU'])
        self.xpath.click()
        time.sleep(2)

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['bu_choose_text_box'])
        self.xpath.send_keys('Technology - Hyderabad (hmviod)')
        self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(1.2)

        self.x_path_element_webdriver_wait(page_elements.event_applicant_action['save'])
        self.xpath.click()
        print('------------------- BU Saved -----------------')
        self.ui_change_bu_save = 'Pass'
