def es_palindromo(texto):
    texto_limpio = ""
    
    for caracter in texto.lower():
        if caracter.isalnum():
            texto_limpio += caracter
    
    return texto_limpio == texto_limpio[::-1]

def probar_palindromo():
    print("=== DETECTOR DE PALÍNDROMOS ===")
    print("Un palíndromo se lee igual al derecho y al revés")
    print("Ejemplos: 'Anita lava la tina', 'Reconocer'")
    
    texto = input("\nIngrese un texto para verificar: ").strip()
    
    if not texto:
        print("No ingresó ningún texto")
        return
    
    if es_palindromo(texto):
        print(f"✅ '{texto}' ES un palíndromo")
    else:
        print(f"❌ '{texto}' NO es un palíndromo")

probar_palindromo()