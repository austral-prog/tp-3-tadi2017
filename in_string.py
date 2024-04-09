def check_vowels():
    Name=input()
    a="a"in Name.lower()
    e="e"in Name.lower()
    i="i"in Name.lower()
    o="o"in Name.lower()
    u="u"in Name.lower()
    print(f"Contiene a: {a}")
    print(f"Contiene e: {e}")
    print(f"Contiene i: {i}")
    print(f"Contiene o: {o}")
    print(f"Contiene u: {u}") 
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
