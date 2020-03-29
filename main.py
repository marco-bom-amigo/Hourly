import requests
import pygsheets
import pandas as pd
import time

def copia_dados_worksheet(
        url_workbook_origem_revenue,
        url_workbook_origem_receita, url_workbook_destino_1,url_workbook_destino_2,url_workbook_destino_3,
        nome_worksheet_origem_revenue='Revenue Responses',
        nome_worksheet_origem_receita='Resultados',
        indice_coluna_copia=0,
        celula_destino='A1',
        nome_worksheet_destino_revenue = 'Rev. Import',
        nome_worksheet_destino_receita = 'Receita Import',
        service_file='client_secret.json'):

    # Google API account info
    google_sheets_client = pygsheets.authorize(service_file=service_file)

    # abre as workbooks
    try:
        workbook_origem_revenue = google_sheets_client.open_by_url(url_workbook_origem_revenue)
        print('Read 1')
        workbook_origem_receita = google_sheets_client.open_by_url(url_workbook_origem_receita)
        print('Read 2')
        workbook_destino_1 = google_sheets_client.open_by_url(url_workbook_destino_1)
        print('Read 3')
        workbook_destino_2 = google_sheets_client.open_by_url(url_workbook_destino_2)
        print('Read 4')
        workbook_destino_3 = google_sheets_client.open_by_url(url_workbook_destino_3)
        print('Read 5')

    except pygsheets.SpreadsheetNotFound as err:
        raise('Url da worksheet não encontrada. Erro {}'.format(err))

    # acessa worksheet com dados de origem
    worksheet_origem_receita = workbook_origem_receita.worksheet('title', nome_worksheet_origem_receita)
    lista_dados_receita = worksheet_origem_receita.get_all_records(empty_value='', head=1)
    df_receita = pd.DataFrame(lista_dados_receita)
    print('Df 1')
    worksheet_origem_revenue = workbook_origem_revenue.worksheet('title', nome_worksheet_origem_revenue)
    lista_dados_revenue = worksheet_origem_revenue.get_all_records(empty_value='', head=1)
    df_revenue = pd.DataFrame(lista_dados_revenue)
    print('Df 2')

    # acessa worksheet com dados de destino

    worksheet_destino_1 = workbook_destino_1.worksheet('title', nome_worksheet_destino_revenue)
    worksheet_destino_2 = workbook_destino_2.worksheet('title', nome_worksheet_destino_revenue)
    worksheet_destino_3 = workbook_destino_3.worksheet('title', nome_worksheet_destino_revenue)
    worksheet_destino_4 = workbook_destino_1.worksheet('title', nome_worksheet_destino_receita)
    worksheet_destino_5 = workbook_destino_2.worksheet('title', nome_worksheet_destino_receita)
    worksheet_destino_6 = workbook_origem_receita.worksheet('title', nome_worksheet_destino_revenue)

    # cola valores na celula
    worksheet_destino_1.set_dataframe(df_revenue, celula_destino)
    print('1')
    worksheet_destino_2.set_dataframe(df_revenue, celula_destino)
    print('2')
    worksheet_destino_3.set_dataframe(df_revenue, celula_destino)
    print('3')
    worksheet_destino_4.set_dataframe(df_receita, celula_destino)
    print('4')
    worksheet_destino_5.set_dataframe(df_receita, celula_destino)
    print('5')
    worksheet_destino_6.set_dataframe(df_revenue, celula_destino)
    print('6')

if __name__ == '__main__':
    while True:
        time.sleep(2800)
        print('Done')
        copia_dados_worksheet(
            url_workbook_origem_revenue='https://docs.google.com/spreadsheets/d/1iPQups5lg5YyfBBSBPJR6bD4INLlSa3nOXpfuxyKvXU/edit#gid=729963051',#planilha de revenue
            url_workbook_origem_receita='https://docs.google.com/spreadsheets/d/1QzImtLN9s-XPLRYcWaOFDLhW7M_-xhlu7NnZ58y8U3g/edit#gid=1096880562',#consulta receita federal
            url_workbook_destino_1='https://docs.google.com/spreadsheets/d/1MvKoHhMw4frPWXCllHVC5-PG9S1k4eOj-S1th0DynrI/edit#gid=0',#planilha background check
            url_workbook_destino_2='https://docs.google.com/spreadsheets/d/1UOAWp2AA3h8RbNHh1UdciqdheF4VPg3D7D66k0iipbM/edit?ts=5e597378#gid=1928062177',# planilha view revenue
            url_workbook_destino_3='https://docs.google.com/spreadsheets/d/1-mA_bo8Nc3XDVPCUOv5n3g9i22YNj1G6YjMOdrMDF2A/edit#gid=305582219',#planilha ultimate
            )
