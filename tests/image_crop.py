class ImageMetadata:
    '''
    Para cada imagem:
    1 - Pegar imagem
    2 - Tratar imagem
    3 - Realizar tentativa de corte
    4 - Comparar com parâmetros já definidos
    '''
    plateCoordinates = {}
    caracteres ="ABC1234"

def getImage(id):
    # Recupera imagem da pasta resources
    return ""

def getParameters(id):
    # Recupera os parâmetros
    return "parameters"

def processImage(rawImage):
    
    # Trata a imagem
    modifiedImage = rawImage
    return modifiedImage

def checkResults(modifiedImage, plateCoordinates):
    
    # Verificar se está aproximado
    if (modifiedImage.coordinates == plateCoordinates):
        return True
    else:
        return False

def test(imageId):
    rawImage = getImage(imageId)
    modifiedImage = processImage(rawImage)
    parameters = getParameters(imageId)

    result = checkResults(modifiedImage, parameters.plateCoordinates)
    return result