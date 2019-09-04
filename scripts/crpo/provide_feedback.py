import cancel_interview
import page_elements
import config
import time
from selenium.common import exceptions


class OldProvideFeedback(cancel_interview.CancelAndRequest):
    def __init__(self):
        super(OldProvideFeedback, self).__init__()
        self.ui_int1_login_PF_o = []
        self.ui_feedback_action_o = []
        self.ui_feedback_screen_o = []
        self.ui_saveasdraft_o = []
        self.ui_int1_decision_o = []

    def login(self):
        self.excel_read()
        self.crpo_login()

    def interviewer_login(self):
        try:
            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            time.sleep(3)
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['Change_applicant_status'])
            time.sleep(2)
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['change_stage'])
            self.xpath.send_keys(self.xl_change_applicant_stage_o)

            self.x_path_element_webdriver_wait(page_elements.event['change_status'])
            self.xpath.send_keys(self.xl_change_applicant_status_o)

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer_selection'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer_selection_done'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['comment'])
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.event['change_button'])
            self.xpath.click()
            time.sleep(3)
            print "-------------------- Applicant Schedule to Interview ------------------------"

            # --------------------------- New tab to login as interviewer ----------------------------------------------
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_username_int1_o)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_password_int1_o)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "-------------------- Interviewer1 Login successfully ------------------------"
            self.ui_int1_login_PF_o = 'Pass'

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event get by Details screen ------------------------"

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_interviews'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"

        except exceptions.NoSuchElementException as error:
            print error

    def provide_feedback(self):
        try:
            # --------------------------------- event interviews -------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['provide_feedback'])
            self.xpath.click()
            print "-------------------- provide feedback opened ------------------------"
            self.ui_feedback_action_o = 'Pass'

            # --------------------------------- Provide feedback -------------------------------------------------------
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(page_elements.feedback['maybe'])
            self.xpath.click()
            self.ui_int1_decision_o = 'Pass'

            self.x_path_element_webdriver_wait(page_elements.feedback['save_draft'])
            self.xpath.click()
            print "-------------------- Save as Draft ------------------------"
            self.ui_feedback_screen_o = 'Pass'
            self.ui_saveasdraft_o = 'Pass'

            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions.NoSuchElementException as error:
            print error


# Object = OldProvideFeedback()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.interviewer_login()
#     Object.provide_feedback()
