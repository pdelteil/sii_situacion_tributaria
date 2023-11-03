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
Salida: 

```
{
    "rut": "76632059-7",
    "razon_social": "INFOSEC SERVICIOS DE SEGURIDAD INFORMATICA SPA",
    "empresa_menor_tamano": "SI",
    "aut_moneda_extranjera": "NO",
    "inicio_actividades": "SI",
    "fecha_inicio_actividades": "08-07-2016",
    "actividades": [
        {
            "giro": "FABRICACION DE COMPUTADORES Y EQUIPO PERIFERICO",
            "codigo": 262000,
            "categoria": "Primera",
            "afecta": true
        },
        {
            "giro": "ACTIVIDADES DE CONSULTORIA DE INFORMATICA Y DE GESTION DE INSTALACIONE",
            "codigo": 620200,
            "categoria": "Primera",
            "afecta": true
        },
        {
            "giro": "PROCESAMIENTO DE DATOS, HOSPEDAJE Y ACTIVIDADES CONEXAS",
            "codigo": 631100,
            "categoria": "Primera",
            "afecta": true
        }
    ],
    "documentos_timbrados": [
        {
            "Documento": "01-02-2017",
            "Año último timbraje": "28-02-2017"
        },
        {
            "Documento": "Factura No Afecta O Exenta Electronica",
            "Año último timbraje": "2023"
        },
        {
            "Documento": "Nota Debito Electronica",
            "Año último timbraje": "2021"
        },
        {
            "Documento": "Nota Credito Electronica",
            "Año último timbraje": "2022"
        }
    ]
}

```
# Alternativa

`curl -sX GET 'https://siichile.herokuapp.com/consulta?rut=76632059-7' -H 'Content-Type: application/json' -H 'Accept: application/json'` 
