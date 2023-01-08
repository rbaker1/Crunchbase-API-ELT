import pytest

from app.src.crunchbase_extract import CrunchbaseExtractor
from py_crunchbase.entities import Entity


class SampleEntity(Entity):
    pass


class TestCrunchbaseExtractor:
    @pytest.fixture(name='api', scope='class')
    def api_instance(self):
        return CrunchbaseExtractor('key')

    def test_init(self):
        api = CrunchbaseExtractor('key')
        assert api.api_key == 'key'

        api = CrunchbaseExtractor()
        assert api.api_key is None

    def test_extractionOutput(self): #todo
        #page with no results
        #extraction type allowed/not-allowed
        #large results

        pass

    def test_objectNamer(self): #todo
        pass

    def test_callAPI(self): #todo
        pass

    def test_writeOutput(self): #todo
        #write to page that does not
        pass