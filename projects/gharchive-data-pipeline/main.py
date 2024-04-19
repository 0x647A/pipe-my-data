import gharchive_downloader
import process_data
import load_to_db

def main():
    filename = gharchive_downloader.download_gharchive_data()
    projects_agg, users_agg = process_data.process_data_with_pandas(filename)
    load_to_db.load_data_to_db(projects_agg, users_agg)

if __name__ == "__main__":
    main()
