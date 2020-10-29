import unittest
# import HTMLReport
import unittestreport
from test_suite import suite_test

"""统一运行入口"""

suite = unittest.TestSuite()
suite.addTests(suite_test.test_suite())

# HTMLReport.TestRunner(
#     report_file_name='test',
#     title='xxx接口测试报告',
#     description='test',
#     thread_count=1
# ).run(suite)
unittestreport.TestRunner(suite, filename="report.html",
                          report_dir=r"C:\Users\25359\PycharmProjects\llc\report",
                          title='测试报告',
                          tester='木森',
                          desc="XX项目测试生产的报告",
                          templates=1
                          ).run()
