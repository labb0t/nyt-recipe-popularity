from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression, Lasso, Ridge 
import numpy as np

def lr_cv_results(X, y, cv=5):
    '''
    Given a set of features X and target y, run linear regression with cross validation. 
    Return R2 and RMSE for train and test
    '''
    m = LinearRegression()
    m_cv = cross_validate(m, X, y, cv=cv, return_train_score=True, scoring=(
        'r2', 'neg_mean_squared_error'))
    m_mean_train_r2 = m_cv['train_r2'].mean()
    m_test_r2 = m_cv['test_r2'].mean()
    m_r2_ratio = m_mean_train_r2 / m_test_r2
    m_train_rmse = abs(m_cv['train_neg_mean_squared_error'].mean())
    m_test_rmse = abs(m_cv['test_neg_mean_squared_error'].mean())
    m_train_rmse_exp = np.exp(m_train_rmse)
    m_test_rmse_exp = np.exp(m_test_rmse)

    # print results
    print("LINEAR REGRESSION")
    print("Mean train r2:", m_mean_train_r2)
    print("Mean test r2:", m_test_r2)
    print("r2 ratio: ", m_r2_ratio)
    print("\nMean train MSE:", m_train_rmse)
    print("Mean test MSE:", m_test_rmse)
    print("Mean train MSE in number of ratings:", m_train_rmse_exp)
    print("Mean test MSE in number of ratings:", m_test_rmse_exp,"\n")

def lasso_cv_results(X, y, cv=5, alpha=0.02794918748827825):
    '''
    Given a set of features X and target y, run lasso with cross validation. 
    Return R2 and RMSE for train and test on all models.
    '''
    m = Lasso(alpha=alpha)
    m_cv = cross_validate(m,X,y,cv=cv ,return_train_score=True, scoring=('r2', 'neg_mean_squared_error'))
    m_mean_train_r2 = m_cv['train_r2'].mean()
    m_test_r2 = m_cv['test_r2'].mean()
    m_r2_ratio = m_mean_train_r2 / m_test_r2
    m_train_rmse = m_cv['train_neg_mean_squared_error'].mean()
    m_test_rmse = m_cv['test_neg_mean_squared_error'].mean()
    m_train_rmse_exp = np.exp(m_train_rmse)
    m_test_rmse_exp = np.exp(m_test_rmse)

    
    # print results
    print("LASSO")
    print("Mean train r2:",m_mean_train_r2)
    print("Mean test r2:",m_test_r2)
    print("r2 ratio: ", m_r2_ratio)
    print("\nMean train MSE:",m_train_rmse)
    print("Mean test MSE:",m_test_rmse)
    print("Mean train MSE in number of ratings:",m_train_rmse_exp)
    print("Mean test MSE in number of ratings:",m_test_rmse_exp,"\n")

def ridge_cv_results(X, y, cv=5, alpha=0.02794918748827825):
    '''
    Given a set of features X and target y, run ridge with cross validation. 
    Return R2 and RMSE for train and test on all models.
    '''
    m = Ridge(alpha=alpha)
    m_cv = cross_validate(m,X,y,cv=cv ,return_train_score=True, scoring=('r2', 'neg_mean_squared_error'))
    m_mean_train_r2 = m_cv['train_r2'].mean()
    m_test_r2 = m_cv['test_r2'].mean()
    m_r2_ratio = m_mean_train_r2 / m_test_r2
    m_train_rmse = m_cv['train_neg_mean_squared_error'].mean()
    m_test_rmse = m_cv['test_neg_mean_squared_error'].mean()
    m_train_rmse_exp = np.exp(m_train_rmse)
    m_test_rmse_exp = np.exp(m_test_rmse)

    
    # print results
    print("RIDGE")
    print("Mean train r2:",m_mean_train_r2)
    print("Mean test r2:",m_test_r2)
    print("r2 ratio: ", m_r2_ratio)
    print("\nMean train MSE:",m_train_rmse)
    print("Mean test MSE:",m_test_rmse)
    print("Mean train MSE in number of ratings:",m_train_rmse_exp)
    print("Mean test MSE in number of ratings:",m_test_rmse_exp,"\n")
    