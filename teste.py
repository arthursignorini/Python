import requests
import json

# Configurações da Z-API
ID_INSTANCIA = '3DD69364FCB690CE20B8C6F206A1FB62'  # Substitua pelo ID da sua instância
TOKEN = '9EDA43CA444614E626A15943'               # Substitua pelo token da instância
CLIENT_TOKEN = 'Fad01f099aa5d4d4096ed0053173d171fS'  # Substitua pelo Client-Token da conta

# URL da API para listar grupos
API_LIST_GROUPS = f"https://api.z-api.io/instances/{ID_INSTANCIA}/token/{TOKEN}/contacts"

# Cabeçalhos incluindo o Client-Token
headers = {
    "Content-Type": "application/json",
    "Client-Token": CLIENT_TOKEN  # Adicionando o Client-Token
}

# Parâmetros iniciais
page = 1
page_size = 100  # Quantidade de contatos por página
all_groups = []

# Função para buscar grupos
def fetch_groups(page, page_size):
    params = {
        "page": page,
        "pageSize": page_size
    }
    response = requests.get(API_LIST_GROUPS, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'❌ Falha ao listar grupos. Código {response.status_code}: {response.text}')
        return None

# Buscar todos os grupos
while True:
    print(f"Buscando página {page} com {page_size} contatos por página...")
    response_data = fetch_groups(page, page_size)
    
    if not response_data:
        break  # Sai do loop em caso de erro
    
    # Verifica se a resposta é um dicionário ou lista
    if isinstance(response_data, dict):
        groups = response_data.get('contacts', [])
    elif isinstance(response_data, list):
        groups = response_data  # Se já for uma lista, usa diretamente
    else:
        print("❌ Resposta inesperada da API:", response_data)
        break
    
    # Adiciona os grupos à lista completa
    all_groups.extend(groups)
    
    # Verifica se há mais grupos para buscar
    if len(groups) < page_size:
        break  # Sai do loop se a página retornada tiver menos registros que o pageSize
    
    # Incrementa a página para buscar a próxima
    page += 1

# Exibir todos os grupos retornados pela API
print(json.dumps(all_groups, indent=4, ensure_ascii=False))

# Filtrar apenas os grupos que contêm "Ford Peças" no nome, ignorando maiúsculas e espaços extras
ford_pecas_groups = [
    group for group in all_groups 
    if 'pai' in group.get('name', '').strip().lower()
]

if not ford_pecas_groups:
    print("❌ Nenhum grupo com 'Ford Peças' encontrado.")
else:
    for group in ford_pecas_groups:
        print(f'✅ Grupo encontrado: {group["name"]} (ID: {group["id"]})')