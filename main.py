# from pumpernickel import Matrix
# Matrix()
# Matrix.hoge()

# from pumpernickel import p
# p('a')

# import numpy as np, pandas as pd
# y_pred = pd.Series(np.arange(4))
# from pumpernickel import print_confusion_matrix
# print_confusion_matrix(y_pred, y_pred)

# import numpy as np, pandas as pd
# y_pred  = pd.Series([0, 1, 0, 0, 0])
# y_valid = pd.Series([0, 1, 1, 0, 0])
# from pumpernickel import print_evaluation
# print_evaluation(y_pred, y_valid)

# import numpy as np, pandas as pd
# y_pred  = pd.Series([0, 1, 0, 0, 0])
# y_valid = pd.Series([0, 1, 1, 0, 0])
# from pumpernickel import print_auc_plot
# print_auc_plot(y_pred, y_valid)

# import warnings
# warnings.filterwarnings('ignore')
# import numpy as np, pandas as pd
# from sklearn import ensemble
# X = np.arange(80).reshape([-1, 2])
# y = np.random.choice(2, 40)
# model = ensemble.RandomForestClassifier()
# model.fit(X, y)
# from pumpernickel import print_feature_importance
# print_feature_importance(['a', 'b'], model)

# import warnings
# warnings.filterwarnings('ignore')
# import numpy as np, pandas as pd
# from sklearn import linear_model
# X = np.arange(80).reshape([-1, 2])
# y = np.random.choice(2, 40)
# model = linear_model.LogisticRegression()
# model.fit(X, y)
# from pumpernickel import print_coef
# print_coef(['a', 'b'], model)

# from pumpernickel import pn
# import numpy as np, pandas as pd
# y_pred  = pd.Series([0, 1, 0, 0, 0])
# y_valid = pd.Series([0, 1, 1, 0, 0])
# pn.print_evaluation(y_pred, y_valid)
