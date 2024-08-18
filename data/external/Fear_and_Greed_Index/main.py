from functions import main
import os 

# Get the current working directory
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

if __name__ == "__main__":
    df = main()
    
    df.to_parquet(os.path.join(data_folder, 'btc_fear_and_greed.parquet.gzip'), compression='gzip')
    # df.to_csv('btc_fear_and_greed.csv', index=False)