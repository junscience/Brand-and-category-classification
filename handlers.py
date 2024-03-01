from fastapi import APIRouter
from model import embedding_data, semantic, model_hits
from fastapi.responses import JSONResponse
from forms import RequestParams, ResponsePredict
from loguru import logger
from DB_connect import dataset_embeddings, DB
from DB_write import write_embeddings

logger.add('debug.log', format="{time} {level} {message}", level="DEBUG", rotation="1 weeks", compression='zip')

router = APIRouter()


@router.get('/status')
def index():
    return {'status': 'OK'}


@router.post('/predict/Embeddings', response_model=ResponsePredict, name='prediction')
def predict_model(params: RequestParams):
    logger.info('Run /predict/Embeddings')
    try:
        embeddings = embedding_data(params.params)
        hits = semantic(dataset_embeddings, embeddings)
        predict = model_hits(hits)['predict']
        predict_quality = model_hits(hits)['predict_quality']
        embed_list = embeddings.tolist()
        write_embeddings(params.params, predict, predict_quality, DB, embed_list)
        return ResponsePredict(params=params.params, predict=predict,
                               predict_quality=predict_quality)
    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})



