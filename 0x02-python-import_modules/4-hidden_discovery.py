#!/usr/bin/python3
if __name__ == "__main__":
    """Print every name defined by hidden_4"""
    import hidden_4

    its_names = dir(hidden_4)
    for name in its_names:
        if name[:2] != "__":
            print(its_names)
