class PersonService:
    _cache = str
    scientist_list = ["Aryabhatta India", "Newton UK", "Albert Eienstein"]

    def __init__(self):
        self._cache = {}

    def __call__(self, personParam):
        if personParam not in self._cache:
            self._cache[personParam] = {personParam: 'test'}
        return self._cache[personParam]

    def is_test(self, name):
        if name in self._cache:
            return True
        else:
            return False

    ## Demoing Lambda Expressions Used.
    def sort_scientist(self):
        print(self.scientist_list)
        return sorted(self.scientist_list, key=lambda name: name.split()[-1])
