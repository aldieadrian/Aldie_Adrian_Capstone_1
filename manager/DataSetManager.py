import json
import uuid

class DataSetManager:

    # Init to set the file path from argument
    def __init__(self, file_path):
        self.file_path = file_path

    # Read data set from function
    def read_data_set(self):
        try:
            # Initialize empty data dictionary
            data = {}

            with open(self.file_path, 'r') as file:
                # Read all line in file
                for line in file:
                    # Separate ID and data
                    data_id, content = line.strip().split(':', 1)
                    try:
                        # Compose the JSON data to dictionary
                        data[data_id.strip()] = json.loads(content.strip())
                    except json.JSONDecodeError as e:
                        print(f"Data tidak valid di baris {line.strip()}: {e}")

            return data
        except FileNotFoundError:
            print(f"File {self.file_path} tidak ditemukan.")
            return {}
        except Exception as e:
            print(f"Terjadi kesalahan saat membaca file: {str(e)}")
            return {}

    # Write data to file function
    def write_data_set(self, data):
        try:
            with open(self.file_path, 'w') as file:
                for data_id, json_data in data.items():
                    file.write(f"{data_id}: {json.dumps(json_data)}\n")
        except Exception as e:
            print(f"Terjadi kesalahan saat menulis ke file: {str(e)}")

    # Add new data function
    def add_new_data_set(self, new_data, prefix_unique_id):
        data = self.read_data_set()
        new_id = prefix_unique_id + str(uuid.uuid4().hex)[:5]
        data[new_id] = new_data
        self.write_data_set(data)
        return new_id

    # Update data function 
    def update_data_set(self, data_id, updated_data):
        data = self.read_data_set()
        if data_id in data:
            data[data_id].update(updated_data)
            self.write_data_set(data)
            return data_id
        else:
            print(f"Data dengan ID {data_id} tidak ditemukan.\n")
            return None

    # Delete data function
    def delete_data_set(self, data_id):
        data = self.read_data_set()
        if data_id in data:
            del data[data_id]
            self.write_data_set(data)
            return data_id
        else:
            print(f"Data dengan ID {data_id} tidak ditemukan.\n")
            return None
