import logging
import os

class HWLog:
    #コンストラクタ
    def __init__(self, current_path, log_level):
        self.current_path = current_path
        self.log_level = log_level

    #ログファイルオープン
    def open(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)
        logfile_handler = logging.FileHandler(self.current_path)
        logfile_handler.setLevel(self.log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logfile_handler.setFormatter(formatter)
        self.logger.addHandler(logfile_handler)

    #debugログ出力
    def log_debug(self, message):
        self.logger.debug(message)

    #infoログ出力
    def log_info(self, message):
        self.logger.info(message)

    #warningログ出力
    def log_warn(self, message):
        self.logger.warning(message)

    #errorログ出力
    def log_error(self, message):
        self.logger.warning(message)

    #criticalログ出力
    def log_critical(self, message):
        self.logger.critical(message)

#動作確認
if __name__ == '__main__':
    current_path = os.getcwd()
    hwlog = HWLog(current_path +'\\test.log', logging.WARNING)
    hwlog.open()
    hwlog.log_debug('test debug!!')
    hwlog.log_info('test info!!')
    hwlog.log_warn('test warning!!')
    hwlog.log_error('test error!!')
    hwlog.log_critical('test critical!!')

    hwlog2 = HWLog(current_path +'\\test2.log', logging.DEBUG)
    hwlog2.open()
    hwlog2.log_debug('test debug2!!')
    hwlog2.log_info('test info2!!')
    hwlog2.log_warn('test warning2!!')
    hwlog2.log_error('test error2!!')
    hwlog2.log_critical('test critical2!!')
