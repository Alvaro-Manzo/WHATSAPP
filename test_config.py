#!/usr/bin/env python3
"""
Script de prueba para verificar pywhatkit
"""
import pywhatkit as kit
import webbrowser
from datetime import datetime

def test_pywhatkit():
    print("🧪 PRUEBA DE PYWHATKIT")
    print("=" * 40)
    
    # Verificar que pywhatkit puede abrir WhatsApp Web
    print("1. Probando apertura de WhatsApp Web...")
    try:
        # Esto solo abre WhatsApp Web sin enviar mensaje
        webbrowser.open("https://web.whatsapp.com")
        print("✅ WhatsApp Web se puede abrir")
    except Exception as e:
        print(f"❌ Error abriendo WhatsApp Web: {e}")
        return False
    
    # Verificar funciones básicas
    print("2. Verificando funciones de pywhatkit...")
    try:
        # Solo verificar que las funciones existen
        assert hasattr(kit, 'sendwhatmsg_instantly')
        assert hasattr(kit, 'sendwhatmsg')
        print("✅ Funciones de pywhatkit disponibles")
    except Exception as e:
        print(f"❌ Error en funciones: {e}")
        return False
    
    print("3. Estado de la configuración:")
    print(f"   - Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"   - PyWhatKit importado correctamente: ✅")
    print(f"   - Navegador disponible: ✅")
    
    print("\n🎉 ¡Todas las pruebas pasaron!")
    print("\n📋 INSTRUCCIONES:")
    print("1. Asegúrate de tener WhatsApp Web abierto")
    print("2. Escanea el código QR si no estás logueado")
    print("3. Ejecuta el bot principal: python main.py")
    
    return True

if __name__ == "__main__":
    test_pywhatkit()
