import pandas as pd

# download_url : S3 url of a file. The file is a CSV table in our example but 
#               could also be a zipped folder, which can be extracted below.
def process(download_url):
    # Read the csv table into a pandas dataframe
    df = pd.read_csv(download_url)

    # Get tablename from the filename by removing .csv extension
    url_wo_sig = download_url[:download_url.find('?')]
    table_name = url_wo_sig[url_wo_sig.rfind('/') + 1 : url_wo_sig.rfind('.')]

    # Create output dataframe with columns table_name, column_name
    of = pd.DataFrame([table_name, i] for i in df.columns)
    of.columns = ['table_name', 'column_name']

    # Return dataframe
    return of


