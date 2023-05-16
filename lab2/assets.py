from dagster import asset, get_dagster_logger
import pandas as pd

# Get our logger
logger = get_dagster_logger()

# Generate our data
df = pd.DataFrame({'column1': [1,2,3], 'column2': [4,5,6]})

@asset(description="The purpose of this asset is to show off the logger capability by logging information.")
def print_with_info():
    logger.info('This is how you use the information logger')

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################
    logger.info('The dataframe has the following dimensions')
    logger.info(f'{df.shape[0]} rows')
    logger.info(f'{df.shape[1]} columns')
    

@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_warning():
    logger.warn('This is how you use the warning logger')

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################
    if df.shape[0] > 2:
        logger.warn('Dataframe has greater than 2 rows')


@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_error():
    logger.error('This is how you use the error logger')

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################
    if df.shape[1] > 2:
        logger.error('Dataframe has greater than 2 columns')


@asset(description="The purpose of this asset is to show off the logger capability with warnings")
def print_with_critical_error():
    logger.critical('This is how you use the critical error logger')

    ##########################################################
    ################# Insert Code Below ######################
    ##########################################################
    if df.shape[0] > 2 and df.shape[1] > 2:
        logger.critical('Dataframe has greater than 2 rows and two columns')
    
