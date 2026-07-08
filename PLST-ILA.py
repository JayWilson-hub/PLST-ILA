import os
import pandas as pd
import numpy as np
import lightgbm as lgb
import gc

lgb_model1 = lgb.LGBMRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=-1,
    num_leaves=31,
    random_state=42,
    subsample=0.8,
    colsample_bytree=0.8
)
lgb_model1.fit(X, y)
y_pred_lgb1 = lgb_model1.predict(X)

### residual
residual = y - y_pred_lgb1

lgb_model2 = lgb.LGBMRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=-1,
    num_leaves=31,
    random_state=42,
    subsample=0.8,
    colsample_bytree=0.8
)
lgb_model2.fit(X, residual)

### Training
y_pred_final = y_pred_lgb1 + lgb_model2.predict(X)

