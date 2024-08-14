while True:
    h = input("enter the height of the wall: ")
    if h.lower() == 'exit':
        break
    w = input("enter the width of the wall: ")
    try:
        h, w = float(h), float(w)
        print(f"wall area: {h * w}")
    except ValueError:
        continue  
