from zeep import Client

'''

client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
result = client.service.ConvertSpeed(
    100, 'kilometersPerhour', 'milesPerhour')

assert result == 62.137

'''
client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method1(bstrParam1='oi', bstrParam2='tchau')
print(result)
