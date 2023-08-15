import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId
from utils.mongo_utils import get_collection

collection = get_collection(collection_name="people")

@csrf_exempt
def cadastrar_pessoa(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nome = data.get('nome')
            idade = data.get('idade')

            if nome is not None and idade is not None:
                pessoa = {"nome": nome, "idade": idade}
                collection.insert_one(pessoa)

                return JsonResponse({"sucesso": True, "mensagem": "Pessoa cadastrada com sucesso."})
            else:
                return JsonResponse({"sucesso": False, "mensagem": "Dados inválidos."})

        except json.JSONDecodeError:
            return JsonResponse({"sucesso": False, "mensagem": "JSON inválido."})

    return JsonResponse({"sucesso": False, "mensagem": "Método não permitido."})

@csrf_exempt
def atualizar_pessoa(request, pessoa_id):
    try:
        pessoa = collection.find_one({"_id": ObjectId(pessoa_id)})
    except:
        return JsonResponse({"sucesso": False, "mensagem": "Pessoa não encontrada."}, status=404)

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            nome = data.get('nome')
            idade = data.get('idade')

            if nome is not None or idade is not None:
                if nome:
                    collection.update_one({"_id": ObjectId(pessoa_id)}, {"$set": {"nome": nome}})
                if idade:
                    collection.update_one({"_id": ObjectId(pessoa_id)}, {"$set": {"idade": idade}})

                return JsonResponse({"sucesso": True, "mensagem": "Dados da pessoa atualizados com sucesso."})
            else:
                return JsonResponse({"sucesso": False, "mensagem": "Dados inválidos."})

        except json.JSONDecodeError:
            return JsonResponse({"sucesso": False, "mensagem": "JSON inválido."})

    return JsonResponse({"sucesso": False, "mensagem": "Método não permitido."})

@csrf_exempt
def excluir_pessoa(request, pessoa_id):
    try:
        pessoa = collection.find_one({"_id": ObjectId(pessoa_id)})
    except:
        return JsonResponse({"sucesso": False, "mensagem": "Pessoa não encontrada."}, status=404)

    if request.method == 'DELETE':
        collection.delete_one({"_id": ObjectId(pessoa_id)})
        return JsonResponse({"sucesso": True, "mensagem": "Pessoa excluída com sucesso."})

    return JsonResponse({"sucesso": False, "mensagem": "Método não permitido."})

def listar_pessoa(request, pessoa_id):

    if request.method == 'GET':
        try:
            pessoa = collection.find_one({"_id": ObjectId(pessoa_id)})
            pessoas_data = {"id": str(ObjectId(pessoa.get('_id'))),"nome": pessoa.get('nome'), "idade": pessoa.get('idade')}
            return JsonResponse({"sucesso": True, "mensagem": pessoas_data})
        except:
            return JsonResponse({"sucesso": False, "mensagem": "Pessoa não encontrada."}, status=404)

    
        collection.delete_one({"_id": ObjectId(pessoa_id)})

    return JsonResponse({"sucesso": False, "mensagem": "Método não permitido."})

def listar_pessoas(request):
    pessoas = collection.find()
    pessoas_data = [{"id": str(ObjectId(pessoa.get('_id'))),"nome": pessoa.get('nome'), "idade": pessoa.get('idade')} for pessoa in pessoas]
    return JsonResponse({"sucesso": True, "pessoas": pessoas_data})
