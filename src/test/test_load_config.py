import os
import pytest
import yaml
from utils.config_handler import ConfigHandler


@pytest.fixture()
def config_file(tmpdir):
    file_path = os.path.join(tmpdir, "config.yaml")
    config = {"key1": "value1", "key2": "value2"}
    with open(file_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False)
    return file_path

def test_load_config(config_file):
    config_handler = ConfigHandler(config_file)
    config = config_handler.load_config()
    assert isinstance(config, dict)
    assert config["key1"] == "value1"
    assert config["key2"] == "value2"

def test_update_config(config_file):
    config_handler = ConfigHandler(config_file)
    config_handler.update_config("key1", "new_value")
    with open(config_file, "r") as f:
        updated_config = yaml.safe_load(f)
    assert updated_config["key1"] == "new_value"

def test_create_config(tmpdir):
    file_path = os.path.join(tmpdir, "new_config.yaml")
    params = {"key1": "value1", "key2": "value2"}
    config_handler = ConfigHandler(file_path)
    config_handler.create_config(params)
    with open(file_path, "r") as f:
        new_config = yaml.safe_load(f)
    assert isinstance(new_config, dict)
    assert new_config["key1"] == "value1"
    assert new_config["key2"] == "value2"