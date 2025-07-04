
def recode_features(X):
    """
    Convierte el problema en uno de clasificación, además de convertir a binarias algunas columnas
    Args:
        X: df inicial
    Returns:
        pd.DataFrame: Dataframe con las columnas recodificadas
    """
    X = X.copy()
    X["absent"] = X["Absenteeism time in hours"].apply(lambda x: 1 if x >= 3 else 0)
    X["Education"] = X["Education"].apply(lambda x: 2 if x > 1 else 1)
    X["Has_pet"] = X["Pet"].apply(lambda x: 1 if x > 0 else 0)
    X["Has_son"] = X["Son"].apply(lambda x: 1 if x > 0 else 0)
    return X


def func_exclude_columns(X, exclude_cols=None):
    """
    Excluye columnas especificadas de un DataFrame de forma segura.

    Args:
        X (pd.DataFrame): DataFrame de entrada.
        exclude_cols (list): Lista de columnas a excluir.

    Returns:
        pd.DataFrame: DataFrame con las columnas excluidas.
    """
    if exclude_cols == None:
        exclude_cols = ["ID", "Height", "Weight", "Disciplinary failure",
                      "Pet", "Son", "Absenteeism time in hours"]

    X_temp = X[[col for col in X.columns if col not in exclude_cols]].copy()
    return X_temp

def map_categoricals(X):
    """Permite hacer el One Hot Encoding"""
    X = X.copy()

    razones = {
    0:"UNK", 1:'Infectious', 2:'Neoplasms', 3:'Blood', 4:'Endocrine',
    5:'Mental', 6:'Nervous_system', 7:'Eye', 8:'Ear',
    9:'Circulatory', 10:'Respiratory', 11:'Digestive', 12:'Skin',
    13:'Musculoskeletal', 14:'Genitourinary', 15: 'Pregnancy', 16:'Perinatal', 
    17:'Congenital', 18:'Symptons', 19:'Injuries', 20:'External causes', 
    21:'healthstatus', 22:'Follow-up', 23:'Consultation', 24:'Blood-donation',
    25:'Lab', 26:'Unjustified', 27:'Physio', 28:'Dentist'}

    meses = {
    1: 'Jan', 2: 'Febr', 3: 'Mar', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec', 0: 'UNK'}
    
    dias = {
    2: 'Monday', 3: 'Tuesday', 4: 'Wednesday',
    5: 'Thursday', 6: 'Friday'}
    
    estaciones = {
    1: 'Summer', 2: 'Autumn', 3: 'Winter', 4: 'Spring'}

    X["Reason for absence"] = X["Reason for absence"].map(razones)
    X["Month of absence"] = X["Month of absence"].map(meses)
    X["Day of the week"] = X["Day of the week"].map(dias)
    X["Seasons"] = X["Seasons"].map(estaciones)
    return X

def evaluate_model(y_true, y_pred):
    """
    Evalúa un modelo de clasificación binaria mostrando sensibilidad, especificidad, precisión y accuracy.

    Parameters:
        y_true (array-like): Valores reales.
        y_pred (array-like): Valores predichos.

    Prints:
        Sensibilidad, especificidad, precisión y accuracy.
    """
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    sensibilidad = tp / (tp + fn) if (tp + fn) > 0 else 0
    especificidad = tn / (tn + fp) if (tn + fp) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    accuracy = accuracy_score(y_true, y_pred)

    print(f"✔️ Sensibilidad (Recall): {sensibilidad:.2f}")
    print(f"✔️ Especificidad: {especificidad:.2f}")
    print(f"✔️ Precisión (Precision): {precision:.2f}")
    print(f"✔️ Exactitud (Accuracy): {accuracy:.2f}")

