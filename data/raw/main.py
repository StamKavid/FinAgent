from functions import main

if __name__ == "__main__":
    # Call the main function
    df = main()
    
    df.to_parquet('raw_data.parquet.gzip', compression='gzip')
    # df.to_csv('raw_data.csv', index=False)