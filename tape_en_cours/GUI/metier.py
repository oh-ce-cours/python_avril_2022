def traitement_donnees(val1: str, val2: str, update_ui=None) -> str:
    if update_ui:
        update_ui(40)
    try:
        return str(int(val1) + int(val2))
    except ValueError:
        return "Des nombres SVP"
