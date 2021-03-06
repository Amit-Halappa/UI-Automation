import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.new_interview_flow import submit_feedback_int1


class SubmitFeedbackInt2(submit_feedback_int1.SubmitFeedbackInt1):
    def __init__(self):
        super(SubmitFeedbackInt2, self).__init__()

        self.no_interviews = ''

        self.ui_event_tab_n_int2 = []
        self.ui_advance_search_n_int2 = []
        self.ui_event_details_n_int2 = []
        self.ui_event_validation_n_int2 = []
        self.ui_floating_action_n_int2 = []
        self.ui_event_interviews_action_n_int2 = []
        self.ui_provide_feedback_action_n_int2 = []
        self.ui_submit_feedback_new_int2 = []

    def submit_feedback_int2(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(1)
            self.crpo_logout()
            self.login('InterviewerTWO', self.xl_int2, self.xl_int2)

            # -------------------------------- Save Draft Process ------------------------------------------------------
            time.sleep(2.5)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.job_sprint_version_n, 'Event')
            self.event_getby_details()
            self.event_validation('submit feedback process by int2')
            self.floating_action()
            time.sleep(1.5)

            self.x_path_element_webdriver_wait(page_elements.floating_actions['event_interviews'])
            self.xpath.click()

            time.sleep(1)
            # ------------- submit feedback
            self.check_box()
            self.provide_feedback_new(self.xl_comment_n)

            self.x_path_element_webdriver_wait(page_elements.buttons['new_submit_feedback'])
            self.xpath.click()
            time.sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.refresh()
            time.sleep(2)

            # -------------------- output report values ----------------
            self.ui_event_tab_n_int2 = 'Pass'
            self.ui_advance_search_n_int2 = 'Pass'
            self.ui_event_details_n_int2 = 'Pass'
            self.ui_event_validation_n_int2 = 'Pass'
            self.ui_floating_action_n_int2 = 'Pass'
            self.ui_event_interviews_action_n_int2 = 'Pass'
            self.ui_provide_feedback_action_n_int2 = 'Pass'

        except Exception as error:
            api_logger.error(error)

    def submit_feed_validation_int2(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.new_interview['no_interviews'])
            self.no_interviews = self.xpath.text
            if self.no_interviews == 'No Interviews':
                self.ui_submit_feedback_new_int2 = 'Pass'
                print('**-------->>> Feedback submitted successfully by interviewer2')
        except Exception as error:
            api_logger.error(error)
