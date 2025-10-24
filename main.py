#!/usr/bin/env python3
"""
WhatsApp Bot Professional
Autor: Tu Nombre
Fecha: Octubre 2024
Descripción: Bot avanzado para envío de mensajes de WhatsApp con múltiples funcionalidades
"""

import pywhatkit as kit
import pandas as pd
from datetime import datetime, timedelta
import re
import os
import sys
import time
from colorama import Fore, Style, init

# Inicializar colorama para colores en terminal
init(autoreset=True)

class WhatsAppBot:
    def __init__(self):
        self.logo = f"""
{Fore.GREEN}
██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗ 
██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝
██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝ 
╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║     
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     
                        {Fore.CYAN}BOT PROFESSIONAL v2.0{Style.RESET_ALL}
        """
        
    def verificar_configuracion(self):
        """Verifica que WhatsApp Web esté configurado correctamente"""
        print(f"{Fore.YELLOW}🔍 VERIFICANDO CONFIGURACIÓN...")
        print(f"{Fore.CYAN}")
        print("Para que el bot funcione correctamente:")
        print("1. ✅ Debes tener WhatsApp Web abierto en tu navegador")
        print("2. ✅ Debes estar logueado en WhatsApp Web")
        print("3. ✅ No debes tener otras pestañas de WhatsApp Web abiertas")
        print("4. ✅ Tu teléfono debe estar conectado a internet")
        print()
        
        respuesta = input(f"{Fore.GREEN}¿Tienes WhatsApp Web abierto y logueado? (s/n): ").lower()
        if respuesta != 's':
            print(f"{Fore.RED}❌ Por favor abre WhatsApp Web primero:")
            print(f"{Fore.CYAN}1. Ve a https://web.whatsapp.com")
            print(f"{Fore.CYAN}2. Escanea el código QR con tu teléfono")
            print(f"{Fore.CYAN}3. Vuelve a ejecutar este programa")
            return False
            
        print(f"{Fore.GREEN}✅ ¡Configuración lista!")
        return True
        
    def mostrar_menu(self):
        """Muestra el menú principal"""
        print(self.logo)
        print(f"{Fore.YELLOW}{'='*60}")
        print(f"{Fore.CYAN}          SELECCIONA UNA OPCIÓN:")
        print(f"{Fore.YELLOW}{'='*60}")
        print(f"{Fore.WHITE}[1] 📱 Enviar mensaje individual")
        print(f"{Fore.WHITE}[2] 📋 Enviar mensajes masivos (desde CSV)")
        print(f"{Fore.WHITE}[3] ⏰ Programar mensaje para después")
        print(f"{Fore.WHITE}[4] 🖼️  Enviar imagen con mensaje")
        print(f"{Fore.WHITE}[5] 📊 Ver estadísticas")
        print(f"{Fore.WHITE}[6] 🔧 Verificar configuración")
        print(f"{Fore.WHITE}[7] ❌ Salir")
        print(f"{Fore.YELLOW}{'='*60}")
        print(f"{Fore.GREEN}💡 TIP: Si es tu primera vez, usa opción [6] primero")
        
    def validar_numero(self, numero):
        """Valida formato del número de teléfono"""
        # Remover espacios y caracteres especiales excepto +
        numero_limpio = re.sub(r'[^\d+]', '', numero)
        
        # Verificar que empiece con + y tenga entre 10-15 dígitos
        patron = r'^\+\d{10,15}$'
        if re.match(patron, numero_limpio):
            return numero_limpio
        return None
        
    def obtener_numero(self):
        """Obtiene y valida el número de teléfono"""
        while True:
            print(f"{Fore.CYAN}Ingresa el número de teléfono:")
            print(f"{Fore.YELLOW}Formato: +[código país][número] (ej: +5215512345678)")
            numero = input(f"{Fore.WHITE}Número: ").strip()
            
            if numero.lower() == 'cancelar':
                return None
                
            numero_validado = self.validar_numero(numero)
            if numero_validado:
                return numero_validado
            else:
                print(f"{Fore.RED}❌ Número inválido. Intenta de nuevo o escribe 'cancelar'")
                
    def obtener_mensaje(self):
        """Obtiene el mensaje a enviar"""
        print(f"{Fore.CYAN}Escribe tu mensaje:")
        mensaje = input(f"{Fore.WHITE}Mensaje: ").strip()
        
        if not mensaje:
            return "Mensaje enviado desde WhatsApp Bot 🤖"
        return mensaje
        
    def enviar_mensaje_individual(self):
        """Envía un mensaje individual inmediatamente"""
        try:
            numero = self.obtener_numero()
            if not numero:
                return
                
            mensaje = self.obtener_mensaje()
            
            print(f"{Fore.YELLOW}⏳ Preparando envío...")
            print(f"{Fore.CYAN}📱 Número: {numero}")
            print(f"{Fore.CYAN}💬 Mensaje: {mensaje}")
            
            confirmacion = input(f"{Fore.GREEN}¿Confirmar envío? (s/n): ").lower()
            if confirmacion != 's':
                print(f"{Fore.YELLOW}❌ Envío cancelado")
                return
            
            # Instrucciones importantes antes del envío
            print(f"{Fore.YELLOW}🔥 IMPORTANTE:")
            print(f"{Fore.CYAN}1. WhatsApp Web se abrirá automáticamente")
            print(f"{Fore.CYAN}2. NO toques nada durante 20 segundos")
            print(f"{Fore.CYAN}3. Mantén WhatsApp Web abierto y logueado")
            
            input(f"{Fore.GREEN}Presiona ENTER cuando estés listo...")
                
            print(f"{Fore.GREEN}🚀 Enviando mensaje en 3... 2... 1...")
            
            # Configuración optimizada para envío real
            kit.sendwhatmsg_instantly(
                phone_no=numero,
                message=mensaje,
                wait_time=20,  # Tiempo de espera aumentado
                tab_close=True,  # Cerrar pestaña automáticamente
                close_time=10   # Tiempo antes de cerrar
            )
            
            print(f"{Fore.GREEN}✅ ¡Mensaje enviado exitosamente!")
            print(f"{Fore.CYAN}📋 Revisa WhatsApp para confirmar la entrega")
            self.guardar_estadistica("individual", numero, mensaje)
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error al enviar mensaje: {str(e)}")
            print(f"{Fore.YELLOW}💡 Tips:")
            print(f"{Fore.CYAN}- Asegúrate de tener WhatsApp Web abierto")
            print(f"{Fore.CYAN}- Verifica tu conexión a internet")
            print(f"{Fore.CYAN}- El número debe incluir código de país")
            
    def programar_mensaje(self):
        """Programa un mensaje para enviar más tarde"""
        try:
            numero = self.obtener_numero()
            if not numero:
                return
                
            mensaje = self.obtener_mensaje()
            
            print(f"{Fore.CYAN}¿Cuándo quieres enviar el mensaje?")
            print("[1] En X minutos")
            print("[2] A una hora específica (hoy)")
            print("[3] Mañana a una hora específica")
            
            opcion = input("Opción: ").strip()
            
            if opcion == "1":
                while True:
                    try:
                        minutos = int(input("¿En cuántos minutos? (mínimo 2): "))
                        if minutos < 2:
                            print(f"{Fore.RED}❌ Mínimo 2 minutos")
                            continue
                        tiempo_envio = datetime.now() + timedelta(minutes=minutos)
                        break
                    except ValueError:
                        print(f"{Fore.RED}❌ Ingresa un número válido")
                        
            elif opcion == "2":
                while True:
                    try:
                        hora = input("Hora (HH:MM en formato 24h): ")
                        hora_obj = datetime.strptime(hora, "%H:%M").time()
                        hoy = datetime.now().date()
                        tiempo_envio = datetime.combine(hoy, hora_obj)
                        
                        if tiempo_envio <= datetime.now():
                            print(f"{Fore.RED}❌ Esa hora ya pasó hoy")
                            continue
                        break
                    except ValueError:
                        print(f"{Fore.RED}❌ Formato inválido. Usa HH:MM")
                        
            elif opcion == "3":
                while True:
                    try:
                        hora = input("Hora (HH:MM en formato 24h): ")
                        hora_obj = datetime.strptime(hora, "%H:%M").time()
                        mañana = datetime.now().date() + timedelta(days=1)
                        tiempo_envio = datetime.combine(mañana, hora_obj)
                        break
                    except ValueError:
                        print(f"{Fore.RED}❌ Formato inválido. Usa HH:MM")
            else:
                print(f"{Fore.RED}❌ Opción inválida")
                return
            
            # Calcular tiempo de espera
            diferencia = tiempo_envio - datetime.now()
            total_segundos = int(diferencia.total_seconds())
            horas = total_segundos // 3600
            minutos = (total_segundos % 3600) // 60
            
            print(f"{Fore.YELLOW}📅 Programado para: {tiempo_envio.strftime('%d/%m/%Y %H:%M')}")
            print(f"{Fore.CYAN}⏰ Tiempo de espera: {horas}h {minutos}m")
            
            confirmacion = input(f"{Fore.GREEN}¿Confirmar programación? (s/n): ").lower()
            if confirmacion != 's':
                return
                
            print(f"{Fore.YELLOW}🔥 IMPORTANTE:")
            print(f"{Fore.CYAN}1. WhatsApp Web se abrirá automáticamente a la hora programada")
            print(f"{Fore.CYAN}2. Mantén la computadora encendida")
            print(f"{Fore.CYAN}3. No cierres este programa")
            
            # Envío programado con configuración optimizada
            kit.sendwhatmsg(
                phone_no=numero,
                message=mensaje,
                time_hour=tiempo_envio.hour,
                time_min=tiempo_envio.minute,
                wait_time=20,  # Tiempo de espera aumentado
                tab_close=True,
                close_time=10
            )
            
            print(f"{Fore.GREEN}✅ ¡Mensaje programado exitosamente!")
            self.guardar_estadistica("programado", numero, mensaje, tiempo_envio)
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error al programar mensaje: {str(e)}")
            print(f"{Fore.YELLOW}💡 Tips:")
            print(f"{Fore.CYAN}- Usa formato 24 horas (ej: 14:30)")
            print(f"{Fore.CYAN}- La hora debe ser futura")
            print(f"{Fore.CYAN}- Mantén WhatsApp Web activo")
            
    def crear_csv_ejemplo(self):
        """Crea un archivo CSV de ejemplo"""
        datos_ejemplo = {
            'numero': ['+5215512345678', '+5215587654321'],
            'nombre': ['Juan Pérez', 'María García'],
            'mensaje': ['¡Hola Juan! Este es un mensaje personalizado', '¡Hola María! Saludos desde el bot']
        }
        
        df = pd.DataFrame(datos_ejemplo)
        df.to_csv('contactos_ejemplo.csv', index=False)
        print(f"{Fore.GREEN}✅ Archivo 'contactos_ejemplo.csv' creado como ejemplo")
        
    def enviar_masivo(self):
        """Envía mensajes masivos desde CSV"""
        try:
            archivo_csv = input(f"{Fore.CYAN}Nombre del archivo CSV (o Enter para crear ejemplo): ").strip()
            
            if not archivo_csv:
                self.crear_csv_ejemplo()
                return
                
            if not os.path.exists(archivo_csv):
                print(f"{Fore.RED}❌ Archivo no encontrado: {archivo_csv}")
                return
                
            df = pd.read_csv(archivo_csv)
            
            print(f"{Fore.CYAN}📊 Contactos encontrados: {len(df)}")
            print(df.head())
            
            # Validar números antes del envío
            numeros_validos = []
            for index, fila in df.iterrows():
                numero = self.validar_numero(str(fila['numero']))
                if numero:
                    numeros_validos.append(index)
                else:
                    print(f"{Fore.RED}❌ Número inválido: {fila['numero']}")
            
            print(f"{Fore.CYAN}📊 Números válidos: {len(numeros_validos)}/{len(df)}")
            
            confirmacion = input(f"{Fore.YELLOW}¿Enviar a todos los contactos válidos? (s/n): ").lower()
            if confirmacion != 's':
                return
            
            print(f"{Fore.YELLOW}🔥 IMPORTANTE:")
            print(f"{Fore.CYAN}1. Habrá una pausa de 10 segundos entre cada mensaje")
            print(f"{Fore.CYAN}2. NO cierres WhatsApp Web durante el proceso")
            print(f"{Fore.CYAN}3. Mantén la computadora activa")
            
            input(f"{Fore.GREEN}Presiona ENTER para comenzar el envío masivo...")
            
            enviados = 0
            errores = 0
                
            for index in numeros_validos:
                try:
                    fila = df.iloc[index]
                    numero = self.validar_numero(str(fila['numero']))
                    mensaje = str(fila.get('mensaje', 'Mensaje desde WhatsApp Bot'))
                    nombre = fila.get('nombre', numero)
                    
                    print(f"{Fore.GREEN}📤 ({enviados+1}/{len(numeros_validos)}) Enviando a {nombre}...")
                    
                    # Envío con configuración optimizada
                    kit.sendwhatmsg_instantly(
                        phone_no=numero,
                        message=mensaje,
                        wait_time=15,
                        tab_close=True,
                        close_time=5
                    )
                    
                    self.guardar_estadistica("masivo", numero, mensaje)
                    enviados += 1
                    
                    print(f"{Fore.GREEN}✅ Enviado a {nombre}")
                    
                    # Pausa entre envíos para evitar spam
                    if index < numeros_validos[-1]:  # No pausar en el último
                        print(f"{Fore.YELLOW}⏳ Esperando 10 segundos...")
                        time.sleep(10)
                        
                except Exception as e:
                    print(f"{Fore.RED}❌ Error con {nombre}: {str(e)}")
                    errores += 1
                    continue
                    
            print(f"{Fore.GREEN}🎉 ¡Envío masivo completado!")
            print(f"{Fore.CYAN}📊 Resultados:")
            print(f"{Fore.GREEN}✅ Enviados: {enviados}")
            print(f"{Fore.RED}❌ Errores: {errores}")
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error en envío masivo: {str(e)}")
            print(f"{Fore.YELLOW}💡 Tips:")
            print(f"{Fore.CYAN}- Verifica el formato del CSV")
            print(f"{Fore.CYAN}- Asegúrate de tener columnas: numero, nombre, mensaje")
            print(f"{Fore.CYAN}- Usa números con código de país")
            
    def guardar_estadistica(self, tipo, numero, mensaje, tiempo=None):
        """Guarda estadísticas de envíos"""
        try:
            if tiempo is None:
                tiempo = datetime.now()
                
            estadistica = {
                'fecha': tiempo.strftime('%d/%m/%Y %H:%M'),
                'tipo': tipo,
                'numero': numero,
                'mensaje': mensaje[:50] + "..." if len(mensaje) > 50 else mensaje
            }
            
            archivo_stats = 'estadisticas.csv'
            
            if os.path.exists(archivo_stats):
                df = pd.read_csv(archivo_stats)
                df = pd.concat([df, pd.DataFrame([estadistica])], ignore_index=True)
            else:
                df = pd.DataFrame([estadistica])
                
            df.to_csv(archivo_stats, index=False)
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error al guardar estadística: {str(e)}")
            
    def ver_estadisticas(self):
        """Muestra estadísticas de envíos"""
        try:
            archivo_stats = 'estadisticas.csv'
            
            if not os.path.exists(archivo_stats):
                print(f"{Fore.YELLOW}📊 No hay estadísticas disponibles")
                return
                
            df = pd.read_csv(archivo_stats)
            
            print(f"{Fore.CYAN}📊 ESTADÍSTICAS DE ENVÍOS")
            print(f"{Fore.YELLOW}{'='*50}")
            print(f"Total de mensajes enviados: {len(df)}")
            print(f"\nPor tipo:")
            print(df['tipo'].value_counts().to_string())
            
            print(f"\n{Fore.CYAN}Últimos 10 envíos:")
            print(df.tail(10).to_string(index=False))
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error al mostrar estadísticas: {str(e)}")
            
    def ejecutar(self):
        """Método principal que ejecuta el bot"""
        while True:
            try:
                self.mostrar_menu()
                opcion = input(f"{Fore.GREEN}Selecciona una opción (1-7): ").strip()
                
                if opcion == "1":
                    if self.verificar_configuracion():
                        self.enviar_mensaje_individual()
                elif opcion == "2":
                    if self.verificar_configuracion():
                        self.enviar_masivo()
                elif opcion == "3":
                    if self.verificar_configuracion():
                        self.programar_mensaje()
                elif opcion == "4":
                    print(f"{Fore.YELLOW}🚧 Función en desarrollo...")
                elif opcion == "5":
                    self.ver_estadisticas()
                elif opcion == "6":
                    self.verificar_configuracion()
                elif opcion == "7":
                    print(f"{Fore.GREEN}👋 ¡Hasta luego!")
                    break
                else:
                    print(f"{Fore.RED}❌ Opción inválida")
                    
                input(f"\n{Fore.CYAN}Presiona Enter para continuar...")
                os.system('clear' if os.name == 'posix' else 'cls')
                
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}👋 Saliendo del programa...")
                break
            except Exception as e:
                print(f"{Fore.RED}❌ Error inesperado: {str(e)}")


if __name__ == "__main__":
    # Verificar dependencias
    try:
        import pandas as pd
        from colorama import Fore, Style, init
    except ImportError as e:
        print("❌ Falta instalar dependencias. Ejecuta:")
        print("pip install pandas colorama")
        sys.exit(1)
    
    bot = WhatsAppBot()
    bot.ejecutar()

