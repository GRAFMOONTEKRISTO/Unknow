import imghdr
from builtins import IOError, SyntaxError, print
from PIL import Image
import json


class ExtractorClient:
    def __init__(self):
        pass

    def format_check(self, file_path):
        pass

    def get_extract_passport(self):
        passport_data = {
            'Фамилия': '-',
            'Имя': '-',
            'Отчество': '-',
            'Пол': '-',
            'Дата рождения': '-',
            'Место рождения': '-',
            'Серия': '-',
            'Номер': '-',
            'Кем выдан': '-',
            'Код подразделения': '-',
            'Дата выдачи': '-',
        }

        json_data = json.dumps(passport_data)

        return json_data

    def get_extract_tax_accounting(self):
        tax_accounting_data = {
            'ИНН': '-',
        }

        json_data = json.dumps(tax_accounting_data)

        return json_data

    def get_extract_snils(self):
        snils_data = {
            'Номер СНИЛС': '-',
        }

        json_data = json.dumps(snils_data)

        return json_data

    def get_extract_diploma(self):
        diploma_data = {
            'Наименования образовательного учреждения': '-',
            'Специальность': '-',
            'Уровень образования': '-',
            'Квалификация/Направление подготовки': '-',
            'Серия': '-',
            'Номер': '-',
            'Даты выдачи': '-',
            'Кем выдан': '-',
        }

        json_data = json.dumps(diploma_data)

        return json_data

    def get_extract_certificate_of_no_criminal_record(self):
        certificate_data = {
            'Серия': '-',
            'Номер': '-',
            'Дата выдачи': '-',
            'Кем выдан': '-',
            'Имеется ли судимость': '-',
        }

        json_data = json.dumps(certificate_data)

        return json_data










# def get_extract_passport(self, file_path):
#     if imghdr.what(file_path) == 'jpeg':
#         return True
#     return False

# client = ExtractorClient()
# # Проверка файла на формат JPG
# result = client.get_extract_passport('./ewq.png')
# print(result)
