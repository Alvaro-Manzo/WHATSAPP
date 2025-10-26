# WhatsApp Bot Professional

Un bot avanzado para WhatsApp con múltiples funcionalidades.

## 🚀 Características

- ✅ Envío de mensajes individuales
- ✅ Envío masivo desde CSV
- ✅ Programación de mensajes
- ✅ Validación de números telefónicos
- ✅ Interfaz colorida y profesional
- ✅ Sistema de estadísticas
- ✅ Manejo robusto de errores

## 📋 Requisitos

- Python 3.7+
- Conexión a internet
- WhatsApp Web configurado en el navegador

## 🛠️ Instalación

1. Clona o descarga el proyecto
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 🎯 Uso

Ejecuta el programa:
```bash
python main.py
```

### Opciones disponibles:

1. **Mensaje Individual**: Envía un mensaje inmediato a un número
2. **Mensajes Masivos**: Carga contactos desde CSV y envía mensajes
3. **Programar Mensaje**: Programa mensajes para enviar más tarde
4. **Estadísticas**: Ve el historial de mensajes enviados

### Formato CSV para mensajes masivos:

```csv
numero,nombre,mensaje
+5215512345678,Juan Pérez,¡Hola Juan! Mensaje personalizado
+5215587654321,María García,¡Hola María! Saludos
```

## ⚙️ Configuración

- El bot valida automáticamente los números telefónicos
- Guarda estadísticas en `estadisticas.csv`
- Crea archivos de ejemplo automáticamente

## 🔧 Solución de Problemas

1. **Error de dependencias**: Ejecuta `pip install -r requirements.txt`
2. **WhatsApp no abre**: Asegúrate de tener WhatsApp Web configurado
3. **Números inválidos**: Usa formato internacional (+código_país + número)

## 📊 Características Técnicas

- Validación regex para números telefónicos
- Manejo de excepciones robusto
- Interfaz colorida con colorama
- Sistema de logging con pandas
- Programación temporal avanzada

¡Disfruta usando el bot! :)
