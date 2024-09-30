import configparser

def demo_config():
    config = configparser.ConfigParser()
    config.read("demo_config.ini")

    print(config)
    print(config.sections())
    print(config["mysql"].get("host"))

    port = config["mysql"].getint("port")
    print(port)

    config["mysql"]["port"] = str(port)
    config["mysql"]["home"] = "/home/den"

    with open("demo_config.ini", "w") as f:
        config.write(f)

def main():
    demo_config()

if __name__ == "__main__":
    main()

