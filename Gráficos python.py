import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
file_path = r'C:\Users\anaca\Downloads\DadosIndic.xlsx'  # Reemplaza con la ruta de tu archivo
df = pd.read_excel(file_path)

# Convertir las columnas de fecha a tipo datetime
df['DTAbertura'] = pd.to_datetime(df['DTAbertura'])
df['DTFechamento'] = pd.to_datetime(df['DTFechamento'])

# Filtrar solo los datos con intervalo de 1 minuto (1m) para hacer un gráfico de líneas
df_1m = df[df['DSGrupo'] == '1m']

# Crear un solo gráfico con 4 subgráficos para los análisis anteriores
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico de líneas para "VlrFechamento" en intervalos de 1 minuto
axs[0, 0].plot(df_1m['DTAbertura'], df_1m['VlrFechamento'], label='VlrFechamento', color='orange')
axs[0, 0].set_xlabel('Fecha y Hora')
axs[0, 0].set_ylabel('Valor de Cierre')
axs[0, 0].set_title('Valor de Cierre (VlrFechamento) en Intervalos de 1 Minuto')
axs[0, 0].legend()
axs[0, 0].tick_params(axis='x', rotation=45)

# Gráfico de barras para mostrar el volumen (VlrVolume)
axs[0, 1].bar(df_1m['DTAbertura'], df_1m['VlrVolume'], color='skyblue', label='VlrVolume')
axs[0, 1].set_xlabel('Fecha y Hora')
axs[0, 1].set_ylabel('Volumen')
axs[0, 1].set_title('Volumen de Operaciones (VlrVolume) en Intervalos de 1 Minuto')
axs[0, 1].legend()
axs[0, 1].tick_params(axis='x', rotation=45)

# Gráfico de dispersión para la relación entre "VlrFechamento" y "VlrVolume"
axs[1, 0].scatter(df_1m['VlrFechamento'], df_1m['VlrVolume'], color='orange', label='Relación VlrFechamento vs VlrVolume')
axs[1, 0].set_xlabel('Valor de Cierre (VlrFechamento)')
axs[1, 0].set_ylabel('Volumen (VlrVolume)')
axs[1, 0].set_title('Relación entre Valor de Cierre y Volumen')
axs[1, 0].legend()

# Gráfico de líneas para el RSI (RSI_close5)
axs[1, 1].plot(df_1m['DTAbertura'], df_1m['RSI_close5'], color='purple', label='RSI (5)')
axs[1, 1].set_xlabel('Fecha y Hora')
axs[1, 1].set_ylabel('RSI (5)')
axs[1, 1].set_title('Índice de Fuerza Relativa (RSI) en Intervalos de 1 Minuto')
axs[1, 1].legend()
axs[1, 1].tick_params(axis='x', rotation=45)

# Ajustar el espacio entre los subgráficos
plt.tight_layout()
plt.show()

