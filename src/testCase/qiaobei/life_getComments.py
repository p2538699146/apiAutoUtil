import unittest
import time
from apiAutoUtil.config.path import dirPath
from apiAutoUtil.src.utils.ParserMethod import parserMethod
from apiAutoUtil.src.utils.PostRequest import postMethod
from ddt import ddt,data

case1 = {
    "shopId" : "2568251",
    # "pageIndex":1,
    # "pageSize":15
}

@ddt
class getMyNearMerchant(unittest.TestCase):
    """根据经纬度获取附近5km商家信息"""
    #测试数据准备
    def setUp(self):
        global url,request
        #创建对象
        request = postMethod()
        inputStream = parserMethod(dirPath.dataPath() + "url.ini")
        #获取数据
        ip = inputStream.selectData("ip","test")
        port = inputStream.selectData("port","8771")
        addr = inputStream.selectData("life","get_my_near_shop")
        url = ip + port + addr
        print("url：" + url)

    """执行测试用例阶段"""
    @data(case1)
    def testMain(self,data):
        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        #断言
        code = result.get("code")
        message = result.get("message")
        self.assertEqual(code,200,msg="接口访问失败")
        self.assertEqual(message,"商户信息查询成功",msg="接口访问失败")
        print(result)

    """执行用例后需要执行的操作"""
    def tearDown(self):
        print("执行完该测试用例了")
        time.sleep(0.5)

if __name__ == '__main__':
    unittest.main()