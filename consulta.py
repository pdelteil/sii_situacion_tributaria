import requests
import base64
from lxml import html
from rut_chile import rut_chile
import json

class Consulta:
    XPATH_RAZON_SOCIAL = '/html/body/div/div[4]'
    XPATH_INICIO_ACTIVIDADES = '/html/body/div/div[7]'
    XPATH_ACTIVIDADES = '/html/body/div/table[1]/tr'

    def __init__(self, rut):
        self.rut = rut

    def validate(self):
        return rut_chile.is_valid_rut(self.rut)

    def resultado(self):
        captcha = self.fetch_captcha()
        rut_formatted = rut_chile.format_capitalized_rut_without_dots(self.rut)
        rut = rut_formatted.split('-')[0]
        dv  = rut_formatted.split('-')[1]


        data = {
            'RUT': rut,
            'DV':  dv,
            'PRG': 'STC',
            'OPC': 'NOR',
            'txt_code': captcha['code'],
            'txt_captcha': captcha['captcha']
        }
        response = requests.post('https://zeus.sii.cl/cvc_cgi/stc/getstc', data=data)
        print(response.text)
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
        inicio_actividades = data.xpath("//span[contains(text(),'Contribuyente presenta Inicio de Actividades:')]/text()")[0].split(":", 1)[-1].strip()

        data_dict = {
            'rut': self.rut,
            'razon_social': data.xpath(self.XPATH_RAZON_SOCIAL)[0].text.strip(),
            'inicio_actividades': inicio_actividades,
            'actividades': actividades}
        # Serialize the dictionary as JSON
        json_data = json.dumps(data_dict, ensure_ascii=False, indent=4)

        return json_data

    def fetch_captcha(self):
        response = requests.post('https://zeus.sii.cl/cvc_cgi/stc/CViewCaptcha.cgi', data={'oper': 0})
        data = response.json()

        return {
            'code': base64.b64decode(data['txtCaptcha'])[36:40].decode(),
            'captcha': data['txtCaptcha']
        }
