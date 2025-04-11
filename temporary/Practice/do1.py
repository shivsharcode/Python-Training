def func():
    try:
        try:
            raise ValueError("level 2")
        except ValueError as e:
            try:
                raise TypeError("level 3") from e
            finally:
                print("Finally Block")
    except Exception as ex:
        print(type(ex.__cause__).__name__)

func()
