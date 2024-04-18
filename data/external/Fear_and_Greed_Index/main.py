from functions import main

if __name__ == "__main__":
    df = main()
    df.to_parquet('btc_fear_and_greed.parquet.gzip', compression='gzip')
    # df.to_csv('btc_fear_and_greed.csv', index=False)