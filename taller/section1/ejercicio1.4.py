def validar_contraseña():
    print("=== VALIDADOR DE CONTRASEÑA SEGURA ===")
    print("La contraseña debe cumplir:")
    print("- Mínimo 8 caracteres")
    print("- Al menos una mayúscula")
    print("- Al menos un número")
    print("- Al menos un carácter especial (!@#$%^&*)")
    print("-" * 40)
    
    contraseña = input("Ingrese su contraseña: ")
    
    criterios = {
        'longitud': len(contraseña) >= 8,
        'mayuscula': any(c.isupper() for c in contraseña),
        'numero': any(c.isdigit() for c in contraseña),
        'especial': any(c in '!@#$%^&*' for c in contraseña)
    }
    
    if all(criterios.values()):
        print("\n✅ ¡CONTRASEÑA SEGURA! Cumple con todos los criterios.")
    else:
        print("\n❌ CONTRASEÑA DÉBIL. No cumple con:")
        if not criterios['longitud']:
            print("  • Debe tener al menos 8 caracteres")
        if not criterios['mayuscula']:
            print("  • Debe contener al menos una mayúscula")
        if not criterios['numero']:
            print("  • Debe contener al menos un número")
        if not criterios['especial']:
            print("  • Debe contener al menos un carácter especial (!@#$%^&*)")

# Ejecutar
validar_contraseña()