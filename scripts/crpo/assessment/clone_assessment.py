import time
import page_elements
from datetime import datetime
from logger_settings import api_logger
from scripts.crpo.assessment import assessment_excel


class CloneAssessment(assessment_excel.AssessmentExcelRead):
    def __init__(self):
        super(CloneAssessment, self).__init__()

        now = datetime.now()
        self.test_from_date = now.strftime("%d/%m/%Y")
        self.test_to_date = now.strftime("%d/%m/%Y")

        self.grid_test_name = ''
        self.assessment_name_breadcumb = ''

        self.ui_test_advance_search = []
        self.ui_old_test_grid_validation = []
        self.ui_old_test_getby_validation = []
        self.ui_clone_action = []
        self.ui_assessment_clone = []
        self.ui_new_test_grid_validation = []
        self.ui_new_test_getby_validation = []

    def assessment_search(self, test_name):
        try:

            self.advance_search(page_elements.tabs['assessment_tab'])

            self.assessment_name_search(test_name, 'assessment')

            if self.search == 'Pass':
                self.ui_test_advance_search = 'Pass'

        except Exception as search:
            api_logger.error(search)

    def clone_assessment(self):
        try:
            # ---------------------------- Search and validating with cloning assessment -------------------------------
            self.assessment_search(self.xl_old_test)
            self.assessment_grid_validation(self.xl_old_test)
            time.sleep(2)
            self.assessment_getby_validation(self.xl_old_test)

            # ------------------------------- Clone test ---------------------------------------------------------------
            time.sleep(2)
            self.floating_action()
            self.x_path_element_webdriver_wait(page_elements.floating_actions['clone_assessment'])
            self.xpath.click()
            self.ui_clone_action = 'Pass'

            time.sleep(1.3)
            self.name_element_webdriver_wait(page_elements.advance_search['assessment_name'])
            self.name.send_keys(self.assessment_sprint_version)

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('From'))
            self.xpath.send_keys(self.test_from_date)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('To'))
            self.xpath.send_keys(self.test_from_date)

            self.x_path_element_webdriver_wait(page_elements.buttons['clone/save'])
            self.xpath.click()

            time.sleep(2)
            # ---------------------------- Search and validating with cloned assessment --------------------------------
            self.assessment_search(self.assessment_sprint_version)
            self.assessment_grid_validation(self.assessment_sprint_version)
            time.sleep(2)
            self.assessment_getby_validation(self.assessment_sprint_version)

            if self.assessment_name_breadcumb == self.assessment_sprint_version:
                self.ui_assessment_clone = 'Pass'
                print('**-------->>> Assessment cloned successfully')
            else:
                print('Failed the assessment cloning <<<--------**')
                time.sleep(2)

        except Exception as error:
            api_logger.error(error)

    def assessment_grid_validation(self, test_name):
        try:
            time.sleep(2)
            self.x_path_element_webdriver_wait(
                page_elements.assessment['grid_assessment_name'].format(test_name))
            self.grid_test_name = self.xpath.text
            if self.grid_test_name == self.xl_old_test:
                self.ui_old_test_grid_validation = 'Pass'
                print('**-------->>> Cloning assessment Validated after search')
            elif self.grid_test_name == self.assessment_sprint_version:
                self.ui_new_test_grid_validation = 'Pass'
                print('**-------->>> Cloned assessment Validated after search')

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(
                page_elements.assessment['grid_assessment_name'].format(test_name))
            self.xpath.click()

        except Exception as e:
            api_logger.error(e)

    def assessment_getby_validation(self, test_name):
        try:
            self.x_path_element_webdriver_wait(page_elements.assessment_validation['assessment_name_breadcrumb'])
            self.assessment_name_breadcumb = self.xpath.text

            if self.assessment_name_breadcumb == self.assessment_sprint_version:
                self.ui_new_test_getby_validation = 'Pass'
                print('**-------->>> assessment Validated and continuing '
                      'with {} to cloned assessment :: {}'.format(test_name, self.assessment_name_breadcumb))

            elif self.assessment_name_breadcumb == self.xl_old_test:
                self.ui_old_test_getby_validation = 'Pass'
                print('**-------->>> assessment Validated and continuing '
                      'with {} to exist assessment :: {}'.format(test_name, self.assessment_name_breadcumb))
            else:
                print('Assessment validation/creation failed <<<--------**')

        except Exception as e:
            api_logger.error(e)


# ob = CloneAssessment()
# ob.clone_assessment()
