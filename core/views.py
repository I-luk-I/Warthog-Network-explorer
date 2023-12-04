from django.shortcuts import render
import requests
from core.forms import FindForm
from django.shortcuts import redirect

URL = "http://127.0.0.1:3000/account/richlist"
URL_HEIGHT = "http://127.0.0.1:3000/chain/signed_snapshot"
URL_HASHRATE = "http://127.0.0.1:3000/chain/hashrate"

def mainPage(request):
    global input_wallet
    
        
    response = requests.get(URL).json()
    response_list = response['data'][:77]
    req_he = requests.get(URL_HEIGHT).json()
    ret_he = req_he['data']['priority']['height']
    req_hash = requests.get(URL_HASHRATE).json()
    req_hash_get = round(req_hash['data']['last100BlocksEstimate'] / 1000000000, 3)
    form = FindForm()
    
    input_wallet = request.GET.get('wallet', '')
    try:
        if input_wallet:
            url = f'http://127.0.0.1:3000/account/{input_wallet}/balance'
            url_transaction = f"http://127.0.0.1:3000/account/{input_wallet}/history/{ret_he}"
            url_transaction_get = requests.get(url_transaction).json()
            transaction = url_transaction_get['data']['perBlock']
            balance = requests.get(url).json()
            balance_get = balance['data']['balance']
            print(balance_get, transaction)
        else:
            balance_get = ''
            transaction = ''
    except KeyError:
        balance_get = 'Empty'
        transaction = 'Invalid address'
            
    return render(request,'index.html',{'response_list':response_list,'form':form,'ret_he':ret_he,
                                            'req_hash_get':req_hash_get,'input_wallet':input_wallet,
                                            'balance_get': balance_get, 'transaction': transaction})




