import yaml

class ConfigHandler:
    """
    A class for handling configuration files.
    
    """
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load_config(self) -> dict:
        """
        Loads a YAML configuration file and returns its contents as a dictionary.

        """
        try:
            with open(self.file_path, "r") as f:
                config = yaml.safe_load(f)
                return config
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"Error loading config: {e}")

    def update_config(self, key: str, value: str) -> None:
        """
        Updates a key-value pair in a YAML configuration file.

        """
        try:
            with open(self.file_path, "r") as f:
                config = yaml.safe_load(f)
            config[key] = value
            with open(self.file_path, "w") as f:
                yaml.dump(config, f, default_flow_style=False)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"Error updating config: {e}")

    def create_config(self, params: dict) -> None:
        """
        Creates a new YAML configuration file.

        """
        try:
            with open(self.file_path, "w") as f:
                yaml.dump(params, f, default_flow_style=False)
        except Exception as e:
            print(f"Error creating config: {e}")
