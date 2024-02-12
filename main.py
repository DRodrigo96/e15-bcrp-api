# main.py
# ==================================================
# settings
import warnings
warnings.filterwarnings('ignore')
# --------------------------------------------------
# standard
import pathlib
from typing import NoReturn
# requirements
import requests, typer
import pandas as pd
from loguru import logger
# --------------------------------------------------

def main(txt: str = typer.Option(..., help='Ruta hacia archivo con lista de series BCRP.')) -> NoReturn:
    _ = pathlib.Path('./downloads/').mkdir(parents=True, exist_ok=True)
    
    with open(txt) as f:
        series = [line.strip() for line in f]
    
    for s in series:
        try:
            url = f'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{s}/json/1940/2018/'
            
            res = requests.get(url)
            if res.status_code not in range(200, 300):
                raise Exception('API response not successful.')
            
            columns = {'name': 'DATE', 'values': s}
            df = pd.json_normalize(res.json(), record_path='periods').rename(columns=columns)
            df[s] = df[s].str[0].astype('float')
            df.to_csv(f := f'./downloads/{s}.csv', sep=',', encoding='iso-8859-1', index=False)
            logger.info(f'Downloaded serie at: {f}')
        
        except:
            logger.warning(f'Could not process serie: {s}')
            continue
    
    logger.info('Done')

if __name__ == '__main__':
    typer.run(main)
