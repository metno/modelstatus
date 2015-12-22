import json
from tastypie.test import ResourceTestCase


class ProductstatusResourceTest(ResourceTestCase):
    """
    Base test resource that setup attributes and methods common to all
    test classes. This class will be inherited by the BaseTestCases.* classes.
    """

    fixtures = ['core.json']

    def setUp(self):
        super(ProductstatusResourceTest, self).setUp()

        self.url_prefix = '/api/v1'
        self.username = 'admin'
        self.password = 'admin'

        # create_apikey generates Authorization http header. The key itself is already in the fixture.
        self.api_key_header = self.create_apikey(self.username, "5bcf851f09bc65043d987910e1448781fcf4ea12")

    def unserialize(self, response):

        return json.loads(response.content)


class BaseTestCases:
    """
    Nested base test classes so the unittest framework won't run the tests defined here.
    """

    class ProductstatusCollectionTest(ProductstatusResourceTest):
        """
        The tests defined here will be run for all the classes that inherit this baseclass.
        Please note that each subclass MUST set all the attributes in their own
        setUp method.
        """

        def setUp(self):
            super(BaseTestCases.ProductstatusCollectionTest, self).setUp()

            self.collection_size = 0
            self.base_url = self.url_prefix
            self.post_data = {}
            self.__model_class__ = None

        def test_post_collection_with_correct_size(self):
            """
            Test that you self.post_data can be posted to resource and that the collection size
            is correct.
            """
            self.assertEqual(self.__model_class__.objects.count(), self.collection_size)
            self.api_client.post(self.base_url, format='json', data=self.post_data,
                                 authentication=self.api_key_header)
            self.assertEqual(self.__model_class__.objects.count(), self.collection_size + 1)

        def test_get_collection(self):
            """
            Test that api returns a valid json response and with correct number of objects
            """
            response = self.api_client.get(self.base_url, format='json')
            self.assertValidJSONResponse(response)
            self.assertEqual(len(self.unserialize(response)['objects']), self.collection_size)

    class ProductstatusItemTest(ProductstatusResourceTest):

        def setUp(self):
            super(BaseTestCases.ProductstatusItemTest, self).setUp()

            self.base_url = self.url_prefix