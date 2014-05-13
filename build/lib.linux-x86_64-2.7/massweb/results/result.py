import json
from urlparse import urlparse

class Result(object):

    def __str__(self):

        url_parsed = urlparse(str(self.fuzzy_target))
        to_ret = json.dumps({"url" : str(self.fuzzy_target), "results" : self.result_dic})

        return to_ret

    def __init__(self, fuzzy_target, result_dic = {}):

        self.fuzzy_target = fuzzy_target
        self.result_dic = result_dic