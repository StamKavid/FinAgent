from functions import main

if __name__ == "__main__":
    df = main()
    
    df.to_parquet('btc_technical_indicators.parquet.gzip', compression='gzip')
    # df.to_csv('btc_technical_indicators.csv', index=False)