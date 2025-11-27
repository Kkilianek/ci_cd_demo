import joblib

model = joblib.load("zadanie/model_adresowo_lodz_lr.pkl")


def predict_price(area_m2: float, rooms: int, floor: str, year_built: int, longitude: float, latitude: float, locality: str) -> float:
    """
    Perform inference using the loaded model.

    Parameters:
    area (float): Area in square meters.
    locality (str): Locality of the property.
    rooms (int): Number of rooms.
    latitude (float): Latitude coordinate.
    longitude (float): Longitude coordinate.

    Returns:
    float: Predicted price_total_zl.
    """
    import pandas as pd

    X_new = pd.DataFrame(
        [[area_m2, rooms, floor, year_built, longitude, latitude, locality]],
        columns=['area', 'rooms', 'floor', 'year_built', 'longitude', 'latitude', 'locality']
    )
    prediction = model.predict(X_new)
    return prediction[0]