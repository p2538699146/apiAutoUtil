# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp

class talkingskill_getMusicByCondition(unittest.TestCase):
    """按条件查询评论话术"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        # self.userId,self.token = login(self.userPhone,self.smsCode)
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyMDQxMTMsInVzZXJJZCI6NjE5OTg4OTI4MjU4MTEzNTM2LCJpc3MiOiJxaWFva3UifQ.81kxXZgRzGVmX6CKQ8lEp09zui_1sH2O4hIRERWyMAw"
        print(self.token)

    def tearDown(self):
        # 清理自动化的测试数据
        # deleteData(self.userPhone)
        pass

    def test(self):
        """按条件查询评论话术"""
        self.a()
        # self.b()

    def a(self):
        data = {
            "keyword":"4",
            # "startTime":"2019-09-11T16:00:00.000Z",
            # "endTime":"2019-09-11T16:00:00.000Z",
            "pageIndex":1,
            "pageSize":10,
        }
        backHttp.getCommentTalkingByCondition(data)

if __name__ == '__main__':
    unittest.main()