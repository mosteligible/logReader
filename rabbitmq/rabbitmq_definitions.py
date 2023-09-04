import json
import os


def get_definition():
    definition = {
        "exchanges": [
            {
                "name": "logreader",
                "vhost": "/",
                "type": "fanout",
                "durable": True,
                "auto_delete": False,
                "internal": False,
                "arguments": {},
            }
        ]
    }


def main():
    definition = get_definition()
    rabbitmq_user = os.getenv("RABBIT_USER")
    rabbit_password = os.getenv("RABBIT_PASSWORD")
    user_tag = os.getenv("RABBITMQ_USER_TAG")
    configure_setting = os.getenv("RABBIT_CONFIGURE_SETTING", ".*")
    write_setting = os.getenv("RABBIT_WRITE_SETTING", ".*")
    read_setting = os.getenv("RABBIT_READ_SETTING", ".*")
    user_characteristics = {
        "users": [
            {
                "name": rabbitmq_user,
                "password_hash": rabbit_password,
                "tags": user_tag,
            }
        ],
        "vhosts": [{"name": "/"}],
    }
    return definition


if __name__ == "__main__":
    main()
