import config
from logger_settings import api_logger
from scripts.crpo.common import validations_check


class Image(validations_check.ValidationCheck):
    def __init__(self):
        super(Image, self).__init__()

    def image_capture(self, image_name):
        try:
            self.driver.save_screenshot(config.image_config['screen_shot'].format(image_name))
        except Exception as image_error:
            api_logger.error(image_error)
