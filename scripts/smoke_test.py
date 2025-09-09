# smoke_test.py - ejecuta un Enviar demo con payload de ejemplo (leer vars de entorno)
import os
from src.python.app.client import enviar

def main():
    # Cargar payload de tests/invoices-samples/sample1.json
    import json
    with open('docs/invoices-samples/sample_minimal.json') as f:
        doc = json.load(f)
    resp = enviar(doc)
    print(resp)

if __name__ == "__main__":
    main()
