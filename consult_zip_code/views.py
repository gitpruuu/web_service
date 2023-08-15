import requests
from django.http import JsonResponse
from utils.mongo_utils import get_collection

collection = get_collection(collection_name="address")

def consulta_cep(request, cep):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        response.raise_for_status()  # Verifica se a resposta HTTP é bem-sucedida

        data = response.json()

        if "erro" in data:
            return JsonResponse({"sucesso": False, "mensagem": "CEP não encontrado."})

        existing_address = collection.find_one({"cep": data["cep"]})
        if existing_address:
            return JsonResponse({"sucesso": False, "mensagem": "CEP já cadastrado."})

        collection.insert_one(data)

        endereco = {
            "cep": data["cep"],
            "logr": data["logradouro"],
            "compl": data["complemento"],
            "bairro": data["bairro"],
            "cidade": data["localidade"],
            "uf": data["uf"],
        }

        return JsonResponse({"sucesso": True, "endereco": endereco})

    except requests.exceptions.RequestException as e:
        return JsonResponse({"sucesso": False, "mensagem": "Erro ao consultar o CEP."})
    except Exception as e:
        return JsonResponse({"sucesso": False, "mensagem": "Ocorreu um erro inesperado."})
