from unittest import TestCase

from task_one_buh import get_doc_owner_name, get_all_doc_owners_names, \
     show_document_info, delete_doc, add_new_doc

from task_two_yadisk_api_add_dir import get_upload_link, get_dir_info

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

# Задача №1 unit-tests
class Testbuhfunctions(TestCase):
    def test_all_doc_owners_names(self):
        self.assertEqual(len(get_all_doc_owners_names()) - 1, len(documents))

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('10006'), 'Аристарх Павлов')

    def test_show_doc_info(self):
        doc_info = show_document_info(documents[0])
        self.assertEqual(doc_info, 'passport "2207 876234" "Василий Гупкин"')

    def test_add_new_doc(self):
        add_new_doc('99-12 01', 'certificate', 'Александр Павлович', 3)
        self.assertEqual(documents[-1], {'name': 'Аристарх Павлов', 'number': '10006', 'type': 'insurance'})

    def test_delete_doc(self):
        self.assertEqual(delete_doc('11-2'), '11-2')


# Задача №2 Автотест API Яндекса
class Testdiryadisk(TestCase):
    def test__get_upload_link(self):
        self.assertEqual(get_upload_link('2021'), int(201))

    def test_get_dir_info(self):
        self.assertEqual(get_dir_info('2021'), 'disk:/2021')

    def test_in_not_dir(self):
        self.assertRaises(KeyError, lambda: get_dir_info('2021'))
