import pytest

from tools.read_yaml import read_yaml


class TestData:
    @pytest.mark.parametrize('input_title,input_content,select_channel,expect', read_yaml('mp_article.yaml'))
    def test_data(self, input_title, input_content, select_channel, expect):
        print(input_title)
        print(input_content)
        # print(select_channel)
        # print(expect)


if __name__ == '__main__':
    TestData.test_data()
