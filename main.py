"""
Prediction de la survie d'un individu sur le Titanic
"""

import os
from dotenv import load_dotenv
import argparse
<<<<<<< HEAD
from loguru import logger

import pathlib
import pandas as pd
from sklearn.model_selection import train_test_split

from src.pipeline.build_pipeline import create_pipeline
from src.models.train_evaluate import evaluate_model


# ENVIRONMENT CONFIGURATION ---------------------------

logger.add("recording.log", rotation="500 MB")
=======
import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from pipeline.build_pipeline import create_pipeline
from models.train_evaluate import evaluate_model


logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("recording.log"),
        logging.StreamHandler()
    ]
)

# ENVIRONMENT CONFIGURATION ---------------------------

>>>>>>> ecce133e9506042f7e86ef081792939762d0ee44
load_dotenv()

parser = argparse.ArgumentParser(description="Paramètres du random forest")
parser.add_argument(
    "--n_trees", type=int, default=20, help="Nombre d'arbres"
)
args = parser.parse_args()

<<<<<<< HEAD
URL_RAW = "https://minio.lab.sspcloud.fr/lgaliana/ensae-reproductibilite/data/raw/data.csv"

n_trees = args.n_trees
jeton_api = os.environ.get("JETON_API", "")
data_path = os.environ.get("data_path", URL_RAW)
data_train_path = os.environ.get("train_path", "data/derived/train.parquet")
data_test_path = os.environ.get("test_path", "data/derived/test.parquet")
=======
n_trees = args.n_trees
jeton_api = os.environ.get("JETON_API", "")
data_path = os.environ.get("data_path", "data/raw/data.csv")
data_train_path = os.environ.get("train_path", "data/derived/train.csv")
data_test_path = os.environ.get("test_path", "data/derived/test.csv")
>>>>>>> ecce133e9506042f7e86ef081792939762d0ee44
MAX_DEPTH = None
MAX_FEATURES = "sqrt"

if jeton_api.startswith("$"):
<<<<<<< HEAD
    logger.info("API token has been configured properly")
else:
    logger.warning("API token has not been configured")
=======
    logging.info("API token has been configured properly")
else:
    logging.warning("API token has not been configured")
>>>>>>> ecce133e9506042f7e86ef081792939762d0ee44


# IMPORT ET STRUCTURATION DONNEES --------------------------------

<<<<<<< HEAD
p = pathlib.Path("data/derived/")
p.mkdir(parents=True, exist_ok=True)

TrainingData = pd.read_csv(data_path)
=======
TrainingData = pd.read_csv("data.csv")
>>>>>>> ecce133e9506042f7e86ef081792939762d0ee44

y = TrainingData["Survived"]
X = TrainingData.drop("Survived", axis="columns")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1
)
<<<<<<< HEAD
pd.concat([X_train, y_train], axis = 1).to_parquet(data_train_path)
pd.concat([X_test, y_test], axis = 1).to_parquet(data_test_path)

=======
pd.concat([X_train, y_train], axis = 1).to_csv("train.csv", index=False)
pd.concat([X_test, y_test], axis = 1).to_csv("test.csv", index=False)
>>>>>>> ecce133e9506042f7e86ef081792939762d0ee44


# PIPELINE ----------------------------

<<<<<<< HEAD

# Create the pipeline
=======
>>>>>>> ecce133e9506042f7e86ef081792939762d0ee44
pipe = create_pipeline(
    n_trees, max_depth=MAX_DEPTH, max_features=MAX_FEATURES
)


# ESTIMATION ET EVALUATION ----------------------

pipe.fit(X_train, y_train)
<<<<<<< HEAD


# Evaluate the model
score, matrix = evaluate_model(pipe, X_test, y_test)

logger.success(f"{score:.1%} de bonnes réponses sur les données de test pour validation")
logger.debug(20 * "-")
logger.info("Matrice de confusion")
logger.debug(matrix)
=======
score, matrix = evaluate_model(pipe, X_test, y_test)

logging.info(f"{score:.1%} de bonnes réponses sur les données de test pour validation")
logging.info(20 * "-")
logging.info("matrice de confusion")
logging.info(matrix)
>>>>>>> ecce133e9506042f7e86ef081792939762d0ee44
