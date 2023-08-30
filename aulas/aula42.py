import json

pessoa = {
  "nome": "Guilherme",
  "sobrenome": "Lopes ",
  "enderecos": [
    {"rua": "R1","numero": 32},
    {"rua": "R2","numero": 55}
  ],
  "altura": 1.8,
  "numeros_preferidos": (2, 4, 6, 8, 10),
  "dev": True,
  "nada": None,
}

#with open('aula42.json', 'w', encoding='utf-8') as arquivo:
 #   json.dump(pessoa, arquivo, ensure_ascii=False, indent=2,)


with open('aula42.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)