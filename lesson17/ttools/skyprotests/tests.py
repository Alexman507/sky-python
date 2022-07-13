import unittest


class StatMixin:
    def send_stat(self, result):
        if result.wasSuccessful():
            print(f"Тест {result.testsRun} пройден успешно!")


class SkyproTestCase(StatMixin, unittest.TestCase):
    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)
        x = len(result.failures) - 1
        if len(result.failures) == 0:
            pass
        else:
            error_ind = result.failures[x][-1].find('%@')
            if error_ind != -1:
                error_text = result.failures[x][-1][error_ind + 2:]
                testcase = result.failures[x][0]
                new_error_output = (testcase, error_text)
                result.failures[x] = new_error_output
        self.send_stat(result)
