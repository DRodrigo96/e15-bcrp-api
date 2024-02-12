# BCRP API Series Download

## Descripción
Python script para descargar automáticamente series del Banco Central de Reserva del Perú a través de su API.

## Uso
1. Generar una archivo TXT con la lista de series que desea descargar.
2. Instalar las dependencias del repositorio. Se recomienda usar un ambiente virtual.
```bash
pip3 install -r requirements.txt
```
3. Ejecutar la línea de comando especificando la ruta del archivo, por ejemplo, usando una muestra del repositorio:
```bash
python main.py --txt="./sample/series.txt"
```
4. Las series serán descargadas en la carpeta `downloads`.
