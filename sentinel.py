mport psutil
import os
import time

def notificar(titulo, mensaje):
        # Envía una notificación real a tu Android
            os.system(f'termux-notification -t "{titulo}" -c "{mensaje}" --image-path logo.png')

            print("🚀 PACK⚡T Sentinel v1.27 activado...")

            while True:
                    # 1. Monitoreo de RAM
                        ram = psutil.virtual_memory().percent
                            if ram > 80:
                                        notificar("🔥 ALERTA DE RAM", f"Uso al {ram}%. ¡PACK⚡T recomienda limpiar!")
                                            
                                                # 2. Monitoreo de Batería
                                                    bateria = psutil.sensors_battery()
                                                        if bateria.percent < 15 and not bateria.power_plugged:
                                                                    notificar("🪫 BATERÍA BAJA", f"Te queda {bateria.percent}%. ¡Busca un cargador!")

                                                                        time.sleep(60) # Revisa cada minuto
                                                                        import psutil
                                                                        import os
                                                                        import time

                                                                        def notificar(titulo, mensaje):
                                                                                # Envía una notificación real a tu Android
                                                                                    os.system(f'termux-notification -t "{titulo}" -c "{mensaje}" --image-path logo.png')

                                                                                    print("🚀 PACK⚡T Sentinel v1.27 activado...")

                                                                                    while True:
                                                                                            # 1. Monitoreo de RAM
                                                                                                ram = psutil.virtual_memory().percent
                                                                                                    if ram > 80:
                                                                                                                notificar("🔥 ALERTA DE RAM", f"Uso al {ram}%. ¡PACK⚡T recomienda limpiar!")
                                                                                                                    
                                                                                                                        # 2. Monitoreo de Batería
                                                                                                                            bateria = psutil.sensors_battery()
                                                                                                                                if bateria.percent < 15 and not bateria.power_plugged:
                                                                                                                                            notificar("🪫 BATERÍA BAJA", f"Te queda {bateria.percent}%. ¡Busca un cargador!")

                                                                                                                                                time.sleep(60) # Revisa cada minuto
                                                                                                                                                import psutil
                                                                                                                                                import os
                                                                                                                                                import time

                                                                                                                                                def notificar(titulo, mensaje):
                                                                                                                                                        # Envía una notificación real a tu Android
                                                                                                                                                            os.system(f'termux-notification -t "{titulo}" -c "{mensaje}" --image-path logo.png')

                                                                                                                                                            print("🚀 PACK⚡T Sentinel v1.27 activado...")

                                                                                                                                                            while True:
                                                                                                                                                                    # 1. Monitoreo de RAM
                                                                                                                                                                        ram = psutil.virtual_memory().percent
                                                                                                                                                                            if ram > 80:
                                                                                                                                                                                        notificar("🔥 ALERTA DE RAM", f"Uso al {ram}%. ¡PACK⚡T recomienda limpiar!")
                                                                                                                                                                                            
                                                                                                                                                                                                # 2. Monitoreo de Batería
                                                                                                                                                                                                    bateria = psutil.sensors_battery()
                                                                                                                                                                                                        if bateria.percent < 15 and not bateria.power_plugged:
                                                                                                                                                                                                                    notificar("🪫 BATERÍA BAJA", f"Te queda {bateria.percent}%. ¡Busca un cargador!")

                                                                                                                                                                                                                        time.sleep(60) # Revisa cada minuto
                                                                                                                                                                                                                        
