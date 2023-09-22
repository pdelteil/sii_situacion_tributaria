# sii_situacion_tributaria
Script para consultar situación tributaria de terceros. Versión web https://zeus.sii.cl/cvc_cgi/stc/getstc

Traducción de Ruby a Python de [@sii](https://github.com/sagmor/sii_chile)

# Cómo usar

```
git clone https://github.com/pdelteil/sii_situacion_tributaria.git

cd sii_situacion_tributaria

pip install -r requirements.txt 

python main.py RUT

ex: python main.py 76632059-7

``` 

# Alternativa

`curl -sX GET 'https://siichile.herokuapp.com/consulta?rut=76632059-7' -H 'Content-Type: application/json' -H 'Accept: application/json'` 
