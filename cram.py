import codecs, requests

class CramConnection(object):
    def __init__(self, client_id, secret_key=None):
        self.url = 'https://api.Cram.com/v2'
        self.client_id = client_id
        self.secret_key = secret_key
        self.search = self.url + '/search/sets'
        self.id = self.url + '/sets/'
        if secret_key:
            self._test_oauth()
        self._test_query()
        self.params =  {'client_id': self.client_id}

    def _test_oath(self):
        pass
    def _test_query(self):
        pass
    def _chk_rsp(self, response):
        pass

    def search_sets(self, term, keep_list=[], **kwargs):
        params = copy(self.params)
        params['qstr'] = str(term)

        if kwargs:
            params = dict(params.items() + kwargs.items())

        response = requests.get(self.search, params=params)

        if response.status_code != 200:
            return response.status_code, response.reason

        if not keep_list:
            keep_list = [u'title', u'set_id', u'subject']

        return [{keep: result[keep] for keep in keep_list}
                 for result in response.json()[u'results']]

    def get_set(self, set_id):
        url = self.id + str(set_id)
        response = requests.get(url, params=self.params)
        if response.status_code != 200:
            return response.status_code, response.reason

        result = response.json()[0]
        lets_keep = [u'title', u'cards']
        return {keep: result[keep] for keep in lets_keep}

    def get_sets(self, id_list):
        pass

    def cleave_cards(self, cards):
        lets_keep = [u'front', u'back', u'image_url', u'image_front', u'hint']
        return [{keep: card[keep] for keep in lets_keep if card[keep]} for card in cards]
