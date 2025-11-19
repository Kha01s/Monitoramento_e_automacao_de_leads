import pandas as pd
import random
from datetime import datetime, timedelta

print('Iniciando a coleta...')
dados=[]
for i in range(40):
    data = datetime.now() - timedelta(days=i)
    leads = random.randint(6, 80)
    dados.append({"Data": data.strftime("%d-%m-%Y"), "Leads": leads})

df = pd.DataFrame(dados)

df.to_csv("date/dados_vendas.csv", index=False)
print("Automação finalizada, arquivo gerado!")
