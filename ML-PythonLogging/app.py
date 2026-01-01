import logging

##logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(name)s-%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()    
    ]
)

logger=logging.getLogger("ArithematicAPP")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b} ={result}")
    return result


def subract(a,b):
    result=a-b
    logger.debug(f"Adding {a} - {b} = {result}")
    return result


def multiply(a,b):
    result=a*b
    logger.debug(f"Adding {a} * {b} = {result}")
    return result


def divide(a,b):
    try:
      result=a/b
      logger.debug(f"Adding {a} + {b} = {result}")
      return result
    except ZeroDivisionError:
        logger.error("Division by Zero Error")
        return None
    
add(10,15)
subract(15,10)
multiply(5,3)
divide(20,0)
