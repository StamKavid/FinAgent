from functions import main
import os 

# Get the current working directory
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

if __name__ == "__main__":
    # Call the main function
    df = main()
    
    df.to_parquet(os.path.join(data_folder, 'raw_data.parquet.gzip'), compression='gzip')
    # df.to_csv(os.path.join(data_folder ,'raw_data.csv'), index=False)