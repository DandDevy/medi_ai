from unittest import TestCase
import requests

REMOTE_ADDRESS = "https://2fc88f82.ngrok.io"


class TestRemote(TestCase):

    def test_tf(self):
        """
        Tests the local version of tensorflow. This verifies that tensorflow is working
        """
        request_result = requests.get(REMOTE_ADDRESS+"/tfversion").text
        expected_result = "2.0.0"
        print("TestRemote : test_tf : request_result ::",request_result)
        print("TestRemote : test_tf : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result, request_result)


    def test_heart(self):
        """
        Tests the heart model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/heart?val0=52&val1=1&val2=0&val3=125&val4=212&val5=0&val6=1&val7=168&val8=0&val9=1&val10=2&val11=2&val12=3").text
        expected_result = "0.040595107"
        print("TestRemote : test_heart : request_result ::",request_result)
        print("TestRemote : test_heart : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)

    def test_heart_rounded(self):
        """
        Tests the heart model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/heart?val0=52&val1=1&val2=0&val3=125&val4=212&val5=0&val6=1&val7=168&val8=0&val9=1&val10=2&val11=2&val12=3&round=1").text
        expected_result = "0"
        print("TestRemote : test_heart_rounded : request_result ::",request_result)
        print("TestRemote : test_heart_rounded : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)

    def test_breast_cancer(self):
        """
        Tests the breast model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/breast_cancer?val0=17.99&val1=10.38&val2=122.8&val3=1001&val4=0.1184").text
        expected_result = "0.0068584555"
        print("TestRemote : test_breast_cancer : request_result ::",request_result)
        print("TestRemote : test_breast_cancer : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)

    def test_breast_cancer_rounded(self):
        """
        Tests the breast model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/breast_cancer?val0=17.99&val1=10.38&val2=122.8&val3=1001&val4=0.1184&round=1").text
        expected_result = "0"
        print("TestRemote : test_breast_cancer_rounded : request_result ::",request_result)
        print("TestRemote : test_breast_cancer_rounded : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)

    def test_prostate_cancer(self):
        """
        Tests the prostate model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/prostate_cancer?val0=1&val1=23&val2=12&val3=151&val4=954&val5=0.143&val6=0.51&val7=0.2&val8=0.010").text
        expected_result = "0.7160286"
        print("TestLocal : test_prostate_cancer : request_result ::",request_result)
        print("TestLocal : test_prostate_cancer : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)

    def test_prostate_cancer_rounded(self):
        """
        Tests the prostate model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/prostate_cancer?val0=1&val1=23&val2=12&val3=151&val4=954&val5=0.143&val6=0.51&val7=0.2&val8=0.010&round=1").text
        expected_result = "1"
        print("TestRemote : test_prostate_cancer_rounded : request_result ::",request_result)
        print("TestRemote : test_prostate_cancer_rounded : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)

    def test_diabetes(self):
        """
        Tests the diabetes model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/diabetes?val0=1&val1=152&val2=43&val3=43&val4=0&val5=55.0&val6=0.51&val7=70").text
        expected_result = "0.30901816"
        print("TestRemote : test_diabetes : request_result ::",request_result)
        print("TestRemote : test_diabetes : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)

    def test_diabetes(self):
        """
        Tests the diabetes model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/diabetes?val0=1&val1=152&val2=43&val3=43&val4=0&val5=55.0&val6=0.51&val7=70").text
        expected_result = "0.30901816"
        print("TestRemote : test_diabetes : request_result ::",request_result)
        print("TestRemote : test_diabetes : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)

    def test_diabetes_rounded(self):
        """
        Tests the diabetes model with some random unseen data.
        """
        request_result = requests.get(REMOTE_ADDRESS+"/diabetes?val0=1&val1=152&val2=43&val3=43&val4=0&val5=55.0&val6=0.51&val7=70&round=1").text
        expected_result = "0"
        print("TestRemote : test_diabetes_rounded : request_result ::",request_result)
        print("TestRemote : test_diabetes_rounded : request_expected result ::",expected_result)
        print()
        self.assertEqual(expected_result,request_result)