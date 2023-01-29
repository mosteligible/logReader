from time import sleep
from unittest import TestCase

from tests.conftest import TEST_DB, TEST_DB_TABLE_NAME


class TestDB(TestCase):
    def testDatabaseOperation(self):
        payloads = [
            {"id": "anid1", "name": "compname1", "plan": "small", "token": "tok00001"},
            {"id": "anid2", "name": "compname2", "plan": "medium", "token": "tok00002"},
            {"id": "anid3", "name": "compname3", "plan": "large", "token": "tok00003"},
            {"id": "anid4", "name": "compname4", "plan": "medium", "token": "tok00004"},
        ]
        for load in payloads:
            self.assertEqual(TEST_DB.AddEntry(load, tableName=TEST_DB_TABLE_NAME), True)

        clientIds = ["anid1", "anid2", "anid3", "anid4"]
        for index, id in enumerate(clientIds):
            clientInfo = TEST_DB.RetreiveClient(clientId=id, tableName=TEST_DB_TABLE_NAME)
            sleep(0.5)
            self.assertDictEqual(clientInfo, payloads[index])

        obtainedClients = TEST_DB.RetreiveAllClients(tableName=TEST_DB_TABLE_NAME)
        self.assertListEqual(obtainedClients, payloads)

        for id in clientIds:
            result = TEST_DB.DeleteClient(id, tableName=TEST_DB_TABLE_NAME)
            self.assertTrue(result)
