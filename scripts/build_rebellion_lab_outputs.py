from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


AUDIENCE_ORDER = {
    "Jedi fiel": 1,
    "Rebelde nostalgico": 2,
    "Explorador casual": 3,
    "Territorio neutral": 4,
}


def classify_audience(row: pd.Series) -> str:
    is_fan = row.get("is_star_wars_fan_binary") == 1
    movies_seen = row.get("total_movies_seen", 0)
    if is_fan and movies_seen >= 5:
        return "Jedi fiel"
    if is_fan and movies_seen < 5:
        return "Rebelde nostalgico"
    if not is_fan and movies_seen >= 2:
        return "Explorador casual"
    return "Territorio neutral"


def audience_role(segment: str) -> str:
    return {
        "Jedi fiel": "Profundidad, lore, inmersion y pertenencia.",
        "Rebelde nostalgico": "Nostalgia, personajes clasicos y memoria emocional.",
        "Explorador casual": "Reconocimiento visual, iconos simples y acceso rapido.",
        "Territorio neutral": "Entrada ligera, digital y sin dependencia del lore.",
    }[segment]


def audience_message(segment: str) -> str:
    return {
        "Jedi fiel": "Entra en la mision completa.",
        "Rebelde nostalgico": "Vuelve al momento que encendio la saga.",
        "Explorador casual": "Reconoce los iconos y elige tu lado.",
        "Territorio neutral": "Descubre Star Wars por sus simbolos universales.",
    }[segment]


def audience_goal(segment: str) -> str:
    return {
        "Jedi fiel": "Fidelizar y convertir en prescriptor.",
        "Rebelde nostalgico": "Reactivar recuerdo y compra emocional.",
        "Explorador casual": "Reducir friccion de entrada.",
        "Territorio neutral": "Crear primer contacto reconocible.",
    }[segment]


def build_audience_tables() -> pd.DataFrame:
    respondents = pd.read_csv(PROCESSED_DIR / "survey_respondents.csv")
    respondents["audience_type"] = respondents.apply(classify_audience, axis=1)
    respondents["audience_type_order"] = respondents["audience_type"].map(AUDIENCE_ORDER)

    total = len(respondents)
    segments = (
        respondents.groupby(["audience_type", "audience_type_order"], dropna=False)
        .agg(
            respondents=("respondent_id", "nunique"),
            avg_movies_seen=("total_movies_seen", "mean"),
            fan_rate_pct=("is_star_wars_fan_binary", "mean"),
            avg_character_affinity=("average_character_opinion_score", "mean"),
            with_demographic_info_pct=("has_demographic_info", "mean"),
        )
        .reset_index()
        .sort_values("audience_type_order")
    )
    segments["share_pct"] = segments["respondents"] / total * 100
    segments["fan_rate_pct"] = segments["fan_rate_pct"] * 100
    segments["with_demographic_info_pct"] = segments["with_demographic_info_pct"] * 100
    segments["strategic_role"] = segments["audience_type"].map(audience_role)
    segments["recommended_message"] = segments["audience_type"].map(audience_message)
    segments["activation_goal"] = segments["audience_type"].map(audience_goal)
    segments = segments[
        [
            "audience_type_order",
            "audience_type",
            "respondents",
            "share_pct",
            "avg_movies_seen",
            "fan_rate_pct",
            "avg_character_affinity",
            "with_demographic_info_pct",
            "strategic_role",
            "recommended_message",
            "activation_goal",
        ]
    ].round(2)
    segments.to_csv(PROCESSED_DIR / "strategy_audience_segments.csv", index=False)

    age_matrix = (
        respondents.groupby(["audience_type_order", "audience_type", "age"], dropna=False)
        .agg(
            respondents=("respondent_id", "nunique"),
            avg_movies_seen=("total_movies_seen", "mean"),
            fan_rate_pct=("is_star_wars_fan_binary", "mean"),
        )
        .reset_index()
        .sort_values(["audience_type_order", "age"])
    )
    age_matrix["fan_rate_pct"] = age_matrix["fan_rate_pct"] * 100
    age_matrix.to_csv(PROCESSED_DIR / "strategy_audience_age_matrix.csv", index=False)

    respondents.to_csv(PROCESSED_DIR / "strategy_survey_respondents.csv", index=False)
    return segments


def build_character_emotional_map() -> pd.DataFrame:
    characters = pd.read_csv(PROCESSED_DIR / "eda_character_merchandising_opportunities.csv")
    emotions = {
        "luke_skywalker": ("Esperanza", "Heroe aspiracional", "Activaciones heroicas y mensajes de superacion."),
        "leia_organa": ("Liderazgo", "Autoridad rebelde", "Campanas de liderazgo, comunidad y resistencia."),
        "han_solo": ("Rebeldia", "Carisma inconformista", "Tono aventurero, nostalgico y de alta afinidad."),
        "yoda": ("Sabiduria", "Mentor Jedi", "Experiencias de aprendizaje, misterio y entrenamiento."),
        "obi_wan_kenobi": ("Legado", "Puente generacional", "Narrativa clasica con autoridad y memoria."),
        "darth_vader": ("Poder", "Icono premium polarizante", "Linea visual adulta, intensa y de alto reconocimiento."),
        "anakin_skywalker": ("Conflicto", "Transformacion", "Relatos de dualidad y eleccion de bando."),
        "r2_d2": ("Compania", "Humor y ternura", "Entrada amable para publico familiar y casual."),
        "c_3po": ("Humor", "Compania reconocible", "Activaciones ligeras, familiares y nostalgicas."),
        "emperor_palpatine": ("Amenaza", "Riesgo dramatico", "Contrapunto del Lado Oscuro, uso secundario."),
        "jar_jar_binks": ("Riesgo de rechazo", "Personaje polarizante", "Usar solo como aprendizaje de sesgo y tono."),
        "boba_fett": ("Misterio", "Coleccionismo", "Linea nicho para fans de iconografia y armaduras."),
        "padme_amidala": ("Elegancia", "Politica y estilo", "Activaciones lifestyle y estetica Naboo."),
        "lando_calrissian": ("Estilo", "Carisma secundario", "Campanas de nostalgia, moda y diferenciacion."),
    }

    def emotional_field(key: str, idx: int, fallback: str) -> str:
        return emotions.get(key, (fallback, fallback, fallback))[idx]

    characters["brand_emotion"] = characters["character_key"].apply(
        lambda key: emotional_field(key, 0, "Afinidad")
    )
    characters["emotional_role"] = characters["character_key"].apply(
        lambda key: emotional_field(key, 1, "Activo de conexion")
    )
    characters["activation_use"] = characters["character_key"].apply(
        lambda key: emotional_field(key, 2, "Apoyo narrativo segun segmento.")
    )
    characters["polarization_risk"] = characters["unfavorable_pct"].apply(
        lambda value: "alto" if value >= 25 else "medio" if value >= 10 else "bajo"
    )
    output_columns = [
        "character_key",
        "character_name",
        "brand_emotion",
        "emotional_role",
        "activation_use",
        "familiarity_score",
        "audience_affinity_score",
        "quote_count",
        "favorable_pct",
        "unfavorable_pct",
        "opinion_responses",
        "opportunity_quadrant",
        "polarization_risk",
    ]
    emotional_map = characters[output_columns].sort_values(
        ["audience_affinity_score", "familiarity_score"], ascending=False
    )
    emotional_map.to_csv(PROCESSED_DIR / "strategy_character_emotional_map.csv", index=False)
    return emotional_map


def build_strategy_routes() -> pd.DataFrame:
    routes = pd.DataFrame(
        [
            {
                "audience_type_order": 1,
                "audience_type": "Jedi fiel",
                "entry_gate": "The Empire Strikes Back",
                "key_characters": "Yoda, Luke Skywalker, Darth Vader",
                "world": "Dagobah / Hoth",
                "experience_format": "Experiencia inmersiva y mision por niveles",
                "primary_emotion": "Profundidad y pertenencia",
                "recommended_action": "Activar lore, retos, coleccionismo y contenido desbloqueable.",
            },
            {
                "audience_type_order": 2,
                "audience_type": "Rebelde nostalgico",
                "entry_gate": "Trilogia original",
                "key_characters": "Han Solo, Leia Organa, Obi-Wan Kenobi",
                "world": "Tatooine",
                "experience_format": "Campana emocional retro",
                "primary_emotion": "Nostalgia y rebeldia",
                "recommended_action": "Usar escenas, frases y estetica clasica con baja complejidad.",
            },
            {
                "audience_type_order": 3,
                "audience_type": "Explorador casual",
                "entry_gate": "Iconos reconocibles",
                "key_characters": "Darth Vader, Yoda, R2-D2",
                "world": "Escenarios reconocibles",
                "experience_format": "Activacion visual sencilla",
                "primary_emotion": "Reconocimiento inmediato",
                "recommended_action": "Priorizar simbolos, videos cortos, piezas sociales y rutas simples.",
            },
            {
                "audience_type_order": 4,
                "audience_type": "Territorio neutral",
                "entry_gate": "Lightsaber y naves",
                "key_characters": "Simbolos antes que personajes",
                "world": "Universo simplificado",
                "experience_format": "Activacion digital de entrada",
                "primary_emotion": "Curiosidad",
                "recommended_action": "Evitar exceso de lore y crear una primera interaccion rapida.",
            },
        ]
    )
    routes.to_csv(PROCESSED_DIR / "strategy_experience_routes.csv", index=False)

    campaign_lines = routes.rename(
        columns={
            "audience_type": "campaign_line",
            "key_characters": "main_assets",
            "experience_format": "recommended_products",
            "recommended_action": "business_reading",
        }
    )
    campaign_lines["target"] = campaign_lines["campaign_line"]
    campaign_lines[
        [
            "campaign_line",
            "main_assets",
            "recommended_products",
            "target",
            "business_reading",
            "entry_gate",
            "world",
            "primary_emotion",
        ]
    ].to_csv(PROCESSED_DIR / "story_campaign_lines.csv", index=False)
    return routes


def build_world_assets() -> None:
    planet_rows = [
        ("Tatooine", "planet", "aventura, origen, desierto y nostalgia", "Pop-up retro o ruta de inicio"),
        ("Hoth", "planet", "batalla, supervivencia y accion", "Experiencia inmersiva de mision"),
        ("Dagobah", "planet", "entrenamiento Jedi, misterio y sabiduria", "Escape room o entrenamiento"),
        ("Coruscant", "planet", "ciudad futurista, tecnologia y escala", "Instalacion tecnologica"),
        ("Naboo", "planet", "estetica visual, elegancia y lifestyle", "Colaboracion lifestyle"),
        ("Endor", "planet", "naturaleza, comunidad y aventura familiar", "Evento familiar y exterior"),
        ("Millennium Falcon", "starship", "aventura, libertad y silueta reconocible", "Pieza central fotografiable"),
        ("X-wing", "starship", "Alianza Rebelde, velocidad y coleccionismo", "Gaming, maquetas y accion"),
        ("Lightsaber", "weapon", "simbolo transversal de eleccion y poder", "Activacion Choose Your Side"),
    ]
    assets = pd.DataFrame(
        planet_rows,
        columns=["asset_name", "asset_type", "story_role", "experience_concept"],
    )
    assets.insert(0, "story_line", assets["asset_type"].map({
        "planet": "Planetas como experiencias",
        "starship": "Tecnologia, poder y velocidad",
        "weapon": "Tecnologia, poder y velocidad",
    }))
    assets.to_csv(PROCESSED_DIR / "story_featured_assets.csv", index=False)

    planet_experiences = assets[assets["asset_type"] == "planet"].copy()
    planet_experiences.rename(
        columns={
            "asset_name": "planet_name",
            "story_role": "brand_atmosphere",
        },
        inplace=True,
    )
    planet_experiences[
        ["planet_name", "brand_atmosphere", "experience_concept"]
    ].to_csv(PROCESSED_DIR / "strategy_planet_experiences.csv", index=False)


def build_story_pages() -> None:
    pages = pd.DataFrame(
        [
            (
                1,
                "La senal perdida",
                "Donde sigue viva la conexion con Star Wars?",
                "eda_survey_kpis, eda_fan_by_age, eda_fan_by_gender, survey_respondents",
                "KPIs, barras por edad/genero, segmentador fan_segment",
            ),
            (
                2,
                "Los clanes de la galaxia",
                "Que tipos de audiencia necesita reactivar la marca?",
                "strategy_audience_segments, strategy_audience_age_matrix, strategy_survey_respondents",
                "donut o barras de segmentos, matriz segmento x edad, promedio peliculas vistas",
            ),
            (
                3,
                "El mapa emocional de Star Wars",
                "Que emocion de marca activa cada personaje?",
                "strategy_character_emotional_map, eda_character_merchandising_opportunities, eda_quote_character_summary",
                "dispersion afinidad/familiaridad, amor vs rechazo, frases por personaje",
            ),
            (
                4,
                "Las puertas de entrada al universo",
                "Que pelicula abre mejor la conversacion con cada publico?",
                "eda_movie_opportunities, eda_movie_commercial_audience_summary, films_business_clean",
                "score pelicula, popularidad vs preferencia, impacto comercial vs conexion",
            ),
            (
                5,
                "Planetas como experiencias",
                "Que atmosfera debe vivir cada publico?",
                "strategy_planet_experiences, eda_planet_business_summary, universe_planets_clean",
                "tarjetas de experiencia, film_count, resident_count, mapa de mundos",
            ),
            (
                6,
                "Tecnologia, poder y velocidad",
                "Que activos generan impacto visual y accion?",
                "eda_starship_business_summary, eda_weapon_business_summary, universe_starships_clean, universe_weapons_clean",
                "naves por presencia, clase de nave, coste vs presencia, armas iconicas",
            ),
            (
                7,
                "La estrategia de reactivacion",
                "Como convertir los datos en rutas de experiencia?",
                "strategy_experience_routes, story_campaign_lines, eda_conclusions, eda_survey_bias_visual",
                "matriz final por audiencia, tarjetas de ruta, sesgos clave",
            ),
        ],
        columns=["page_order", "page_name", "business_question", "main_tables", "main_visuals"],
    )
    pages.to_csv(PROCESSED_DIR / "storytelling_powerbi_pages.csv", index=False)


def build_conclusions(segments: pd.DataFrame) -> None:
    movie_summary = pd.read_csv(PROCESSED_DIR / "eda_movie_commercial_audience_summary.csv")
    character_map = pd.read_csv(PROCESSED_DIR / "strategy_character_emotional_map.csv")
    kpis = pd.read_csv(PROCESSED_DIR / "eda_survey_kpis.csv").iloc[0]
    bias_visual = pd.read_csv(PROCESSED_DIR / "eda_survey_bias_visual.csv")

    top_segment = segments.sort_values("respondents", ascending=False).iloc[0]
    top_movie = movie_summary.sort_values("preference_score", ascending=False).iloc[0]
    top_character = character_map.sort_values("audience_affinity_score", ascending=False).iloc[0]
    expanded_universe_null_pct = bias_visual.loc[
        bias_visual["bias_dimension"] == "Fan universo expandido no medido",
        "bias_metric_pct",
    ].iloc[0]

    conclusions = pd.DataFrame(
        [
            {
                "area": "Audiencia",
                "finding": f"{kpis['seen_any_star_wars_pct']:.2f}% ha visto alguna pelicula y {kpis['star_wars_fan_pct']:.2f}% se declara fan.",
                "business_reading": "La marca tiene reconocimiento, pero la estrategia debe diferenciar niveles de vinculo.",
            },
            {
                "area": "Segmentacion",
                "finding": f"El segmento mas grande es {top_segment['audience_type']} con {int(top_segment['respondents'])} respuestas.",
                "business_reading": "El dashboard debe hablar de clanes de audiencia, no de una masa unica.",
            },
            {
                "area": "Peliculas",
                "finding": f"{top_movie['movie_title']} lidera la conexion de audiencia con preference_score {top_movie['preference_score']:.2f}.",
                "business_reading": "La pelicula ganadora funciona como puerta emocional, no solo como dato comercial.",
            },
            {
                "area": "Personajes",
                "finding": f"{top_character['character_name']} destaca por afinidad y activa la emocion {top_character['brand_emotion']}.",
                "business_reading": "Los personajes deben leerse como emociones de marca, no solo como productos.",
            },
            {
                "area": "Experiencias",
                "finding": "Tatooine, Hoth, Dagobah, Coruscant, Naboo y Endor representan atmosferas de campana distintas.",
                "business_reading": "Elegir un planeta equivale a elegir la sensacion que vivira el publico.",
            },
            {
                "area": "Activos visuales",
                "finding": "Millennium Falcon, X-wing y Lightsaber concentran reconocimiento visual y accion.",
                "business_reading": "Los simbolos convierten la estrategia en una experiencia memorable y facil de comunicar.",
            },
            {
                "area": "Recomendacion",
                "finding": "La propuesta final es Choose Your Side: una estrategia modular por tipo de audiencia.",
                "business_reading": "Star Wars no necesita una unica campana; necesita varias rutas de conexion bajo una misma marca.",
            },
            {
                "area": "Sesgos",
                "finding": f"{kpis['seen_any_star_wars_pct']:.2f}% ha visto alguna pelicula, {kpis['star_wars_fan_pct']:.2f}% se declara fan y {expanded_universe_null_pct:.2f}% no responde universo expandido.",
                "business_reading": "La lectura es direccional: sirve para reactivar publico fan o familiarizado, no para predecir el mercado general.",
            },
        ]
    )
    conclusions.to_csv(PROCESSED_DIR / "eda_conclusions.csv", index=False)


def main() -> None:
    segments = build_audience_tables()
    build_character_emotional_map()
    build_strategy_routes()
    build_world_assets()
    build_story_pages()
    build_conclusions(segments)
    print("Rebellion Lab outputs generated in data/processed")


if __name__ == "__main__":
    main()
