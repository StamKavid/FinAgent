from functions import main

if __name__ == "__main__":
    df = main()
    df.to_parquet('yahoo_finance.parquet.gzip', compression='gzip')
    # df.to_csv('yahoo_finance.csv', index=False)
