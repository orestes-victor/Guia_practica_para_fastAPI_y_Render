from fastapi import FastAPI, HTTPException
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# Función para obtener el top de gastadores por año
def top_consumidores_por_anio(df, year):

    # Filtrar el DataFrame por el año proporcionado
    df_usuarios_filtered = df[df['Año'] == year]

    # Obtener el top 3 de usuarios que más gastaron en ese año
    top_consumidores = df_usuarios_filtered.groupby('Usuario')['Gastos'].sum().nlargest(3)

    # Crear el resultado en formato JSON
    result = {
        'Para el año': year,
        'Estos son los top 3 usuarios consumidores': top_consumidores.reset_index().to_dict(orient='records')
    }
    return result

# Ruta para obtener el top de consumidores por año desde el archivo Parquet
@app.get("/top3_consumidores/{year}")
async def top_consumidores_by_year(year: int):
    try:
        # Cambia la ruta del archivo según la ubicación de tu archivo df_endpoint_1.parquet
        df = pd.read_parquet("C:/Users/Usuario/Desktop/Repositorios Github/Repositorio_guia_para_fastAPI_y_RENDER/Dataset/dataset_endpoint_1.parquet")
        # df = pd.read_parquet("df_endpoint_1.parquet")  # Esta línea está duplicada y se puede eliminar

        # Aplicar la función para obtener el top de gastadores por año
        result = top_consumidores_por_anio(df, year)

        return JSONResponse(content=jsonable_encoder(result), media_type="application/json")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo Parquet no encontrado, revisa si la ruta del archivo es correcta ;)")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer el archivo Parquet: {str(e)}")
