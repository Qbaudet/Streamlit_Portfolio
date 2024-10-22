import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
# import numpy as np
import geopandas as gpd
import folium


def load_dataset() -> DataFrame:
    data: DataFrame = pd.read_csv("fr-en-indicateurs-de-resultat-des-lycees-gt_v2.csv", delimiter=";")
    return data


def data_preprocessing(data: DataFrame) -> DataFrame:
    columns_to_keep = [
        'Annee', 'UAI', 'Etablissement', 'Secteur', 'Code commune', 'Commune',
        'Code departement', 'Departement', 'Academie', 'Code region', 'Region',
        'Presents - Toutes series', 'Taux de reussite - Toutes series',
        'Valeur ajoutee du taux de reussite - Toutes series',
        'Valeur ajoutee du taux d\'acces 2nde-bac', 'Taux de mentions - Toutes series',
        'Valeur ajoutee du taux de mentions - Toutes series',
        'Nombre de mentions TB avec felicitations - G', 'Nombre de mentions TB sans felicitations - G',
        'Nombre de mentions B - G', 'Nombre de mentions AB - G',
        'Nombre de mentions TB avec felicitations - T', 'Nombre de mentions TB sans felicitations - T',
        'Nombre de mentions B - T', 'Nombre de mentions AB - T'
    ]
    data_filtered = data[columns_to_keep]
    return data_filtered


def create_distribution_plot(data: DataFrame, column_names: list[str], year: int):
    data = data[column_names]

    filtered_data = data[data['Annee'] == year]

    plt.figure(figsize=(4, 3))
    sns.histplot(filtered_data[column_names[1]], kde=True, bins=20)
    plt.xlabel(column_names[1])
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {column_names[1]} in {year}')

    return plt


def create_trend_plot(data: DataFrame, column_name: str):
    average_data = data.groupby("Annee")[column_name].mean().reset_index()

    plt.figure(figsize=(10, 8))
    plt.plot(average_data["Annee"], average_data[column_name], marker='o')
    plt.xlabel("Année")
    plt.ylabel(column_name)
    plt.title(f'Average {column_name} over the years')

    return plt


def create_pie_chart_2023(data: DataFrame, column_names: list[str]):
    data_2023 = data[data['Annee'] == 2023]
    data_avg_2023 = data_2023[column_names].mean()

    plt.figure(figsize=(12, 10))
    colors = plt.cm.get_cmap('tab10', len(column_names))

    plt.pie(
        data_avg_2023,
        labels=column_names,
        autopct='%1.1f%%',
        startangle=90,
        colors=[colors(i) for i in range(len(column_names))]
    )

    plt.title('Proportion of each honours for the year 2023')
    plt.axis('equal')
    plt.show()

    return plt


def create_department_success_rate_map(data: pd.DataFrame, column_name: str):
    geojson_path = "https://france-geojson.gregoiredavid.fr/repo/departements.geojson"
    france_geo = gpd.read_file(geojson_path)

    data_2023 = data[data['Annee'] == 2023]
    data_avg = data_2023.groupby("Code departement")[column_name].mean().reset_index()

    france_geo = france_geo.merge(data_avg, how='left', left_on='code', right_on='Code departement')

    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

    choropleth = folium.Choropleth(
        geo_data=france_geo.to_json(),
        data=data_avg,
        columns=["Code departement", column_name],
        key_on="feature.properties.code",
        fill_color="YlOrRd",
        fill_opacity=0.6,
        line_opacity=0.5,
        legend_name=column_name,
    ).add_to(m)

    geojson_layer = folium.GeoJson(
        france_geo.to_json(),
        name="Departments",
        tooltip=folium.GeoJsonTooltip(
            fields=["nom", column_name],
            aliases=["Department", column_name],
            localize=True
        )
    ).add_to(m)

    return m


def create_box_plot_type(data: DataFrame, column_name: str):
    data_avg = data.groupby(['Annee', 'Secteur'])[column_name].mean().reset_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(data=data_avg, x='Annee', y=column_name, hue='Secteur', palette='Set2')

    plt.title(f'Average {column_name} by Year and Secteur')
    plt.xlabel('Année')
    plt.ylabel(f'Average {column_name}')
    plt.legend(title='Secteur')
    plt.grid(True)
    plt.tight_layout()

    return plt


def create_trends_rates_talma(data: DataFrame, column_names: list[str]):
    data = data[data["UAI"] == '0911021R']
    average_data = data.groupby("Annee")[column_names].mean().reset_index()

    plt.figure(figsize=(10, 8))
    for i, column in enumerate(column_names):
        plt.plot(average_data["Annee"], average_data[column], marker='o', label=column)

    plt.xlabel("Année", fontsize=12)
    plt.ylabel("Percentage", fontsize=12)
    plt.title(f'Trends on the percentages of success and honor rate for the Talma high school', fontsize=14, fontweight='bold')

    plt.legend(title='Metrics', fontsize=10, title_fontsize='12')
    plt.grid(True)
    plt.tight_layout()

    return plt


def create_trends_added_values_talma(data: DataFrame, column_names: list[str]):
    data = data[data["UAI"] == '0911021R']
    average_data = data.groupby("Annee")[column_names].mean().reset_index()

    plt.figure(figsize=(10, 8))
    for i, column in enumerate(column_names):
        plt.plot(average_data["Annee"], average_data[column], marker='o', label=column)

    plt.xlabel("Année", fontsize=12)
    plt.ylabel("Added value", fontsize=12)
    plt.title(f'Trends on the added values of the Talma high school', fontsize=14, fontweight='bold')

    plt.legend(title='Metrics', fontsize=10, title_fontsize='12')
    plt.grid(True)
    plt.tight_layout()

    return plt


def create_trend_number_students_talma(data: DataFrame, column_name: str):
    data = data[data["UAI"] == '0911021R']
    average_data = data.groupby("Annee")[column_name].mean().reset_index()

    plt.figure(figsize=(10, 8))
    plt.plot(average_data["Annee"], average_data[column_name], marker='o')
    plt.xlabel("Année", fontsize=12)
    plt.ylabel(column_name, fontsize=12)
    plt.title(f'Average {column_name} over the years', fontsize=14, fontweight='bold')
    plt.grid(True)
    plt.tight_layout()

    return plt

