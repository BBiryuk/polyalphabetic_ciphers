import re


class Cryptographer:
    def __init__(self, message):
        self.RU_ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        self.FIRST_ALPHABET = 'БЮГЫЕЬЗШЙЦЛФНТПРСОУМХКЧИЩЖЪДЭВЯ АЁ'
        self.SECOND_ALPHABET = 'СОУМКХЧИЩЖЪДЭВЯАБЮГ ЕЬЗШЙЦЁФНТПРЫЛ'
        self.THIRD_ALPHABET = 'МНОПРСТУФЪЦЧЩЗЪЬЫЭЮЯ АБВГДЕЁЖЗИЙКЛ'
        self.message = self.message_formatter(message)

    def message_formatter(self, message):
        message = re.sub(r'[.,"\'-?:!;\n]', '', message.upper())
        if all([i in self.RU_ALPHABET for i in message]):
            return message
        else:
            raise ValueError('Invalid message')

    def encryption(self):
        result = ''
        count = 1
        for i in self.message:
            x = self.RU_ALPHABET.index(i)
            if count % 3 == 0:
                result += self.THIRD_ALPHABET[x]
            elif count % 2 == 0:
                result += self.SECOND_ALPHABET[x]
            else:
                result += self.FIRST_ALPHABET[x]
            count += 1
        print(result)
        return result

    def decryption(self, message):
        result = ''
        count = 1
        for i in message:
            if count % 3 == 0:
                result += self.RU_ALPHABET[self.THIRD_ALPHABET.index(i)]
            elif count % 2 == 0:
                result += self.RU_ALPHABET[self.SECOND_ALPHABET.index(i)]
            else:
                result += self.RU_ALPHABET[self.FIRST_ALPHABET.index(i)]
            count += 1
        print(result)
        return result


text = """
У лукоморья дуб зелёный; 
Златая цепь на дубе том: 
И днём и ночью кот учёный 
Всё ходит по цепи кругом; 
Идёт направо - песнь заводит, 
Налево - сказку говорит.
"""

e = Cryptographer(text)
a = e.encryption()
b = e.decryption(a)
