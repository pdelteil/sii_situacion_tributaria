import requests
from lxml import html
import base64

class Consulta:
    XPATH_RAZON_SOCIAL = '/html/body/div/div[4]'
    XPATH_ACTIVIDADES = '/html/body/div/table[1]/tr'

    def __init__(self, rut):
        self.rut = rut

    def resultado(self):
        captcha = self.fetch_captcha()
        data = {
            'RUT': self.rut.split('-')[0],
            'DV': self.rut.split('-')[1],
            'PRG': 'STC',
            'OPC': 'NOR',
            'txt_code': captcha['code'],
            'txt_captcha': captcha['captcha']
        }
        response = requests.post('https://zeus.sii.cl/cvc_cgi/stc/getstc', data=data)

        data = html.fromstring(response.text)

        actividades = [
            {
                'giro': node.xpath('./td[1]/font')[0].text.strip(),
                'codigo': int(node.xpath('./td[2]/font')[0].text.strip()),
                'categoria': node.xpath('./td[3]/font')[0].text.strip(),
                'afecta': node.xpath('./td[4]/font')[0].text.strip() == 'Si'
            }
            for node in data.xpath(self.XPATH_ACTIVIDADES)[1:]
        ]

        return {
            'rut': self.rut.format(),
            'razon_social': data.xpath(self.XPATH_RAZON_SOCIAL)[0].text.strip(),
            'actividades': actividades
        }

    def fetch_captcha(self):
        response = requests.post('https://zeus.sii.cl/cvc_cgi/stc/CViewCaptcha.cgi', data={'oper': 0})
        data = response.json()

        return {
            'code': base64.b64decode(data['txtCaptcha'])[36:40].decode(),
            'captcha': data['txtCaptcha']
        }

