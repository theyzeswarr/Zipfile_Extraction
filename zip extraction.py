import zipfile

def extract_zip_file(zip_file_path, destination_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)
    print("Extraction complete.")

# Specify the path of the zip file and the destination folder where the contents will be extracted
zip_file_path = 'C:\\Users\\ibmtr\\Downloads\\GSOC2017-master.zip'
destination_path = 'C:\\Users\\ibmtr\\Desktop\\20projects'

# Call the function to extract the zip file
extract_zip_file(zip_file_path, destination_path)