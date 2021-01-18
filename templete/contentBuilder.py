
class ContentBuilder:
    
    # def makeRequestUrlRemark():
    
    #     return remarkText

    '''
    {
        "requestParamObjects" : [
            {
                "typeInfo(int, myVo ...etc)" : "int"
                "variableName" : "name"
            },
            {}, {}, ...
        ], ...
    }
    '''    
    def makeRequestParamRemark(self, requestParamObjects):
        remarkText = ''
        return remarkText


    '''
    {
        "reponseFieldObjects" : [
            {
                "typeInfo(int, myVo ...etc)" : "int"
                "variableName" : "name"
            },
            {}, {}, ...
        ], ...
    }
    '''
    def makeResponseParamRemark(self, reponseFieldObjects):
        remarkText = ''
        return remarkText

    # def makeMappingAnnotation():

    #     return annotationText



    '''
    primitive type pre definition
        int : return 0;
        boollean : return true;
        String : return '';
    ex) primitive type ) return : return 0;
        collection type ) return : return null;
    {
        "reponseFieldObjects" : [
            {
                "typeInfo(int, myVo ...etc)" : "int"
            },
            {}, {}, ...
        ], ...
    }
    '''
    def makeFunctionReturn(self, reponseFieldObjects):
        definitionText = ''
        primitiveTypeDefault = {
            "int" : "0",
            "boolean" : "true"
        }

        if reponseFieldObjects[0]["typeInfo"] in list(primitiveTypeDefault.keys()):
            definitionText += primitiveTypeDefault["typeInfo"]
        else:
            definitionText += "new Object()"
            
        definitionText = "return " + definitionText + ";"
        return definitionText

    '''
    ex) return : public List<TextAndCountSearchHistoryAcademyVo> findAcademySearchKeyword()
    {
        "requestParamObjects" : [
            {
                "typeInfo(int, myVo ...etc)" : "int"
                "variableName" : "name"
            },
            {}, {}, ...
        ], ...
    }
    '''    

    def makeFunctionDefinition(self, functionName, requestParamObjects, reponseFieldObjects):
        definitionText = ''
        reqParamText = ''
        
        if requestParamObjects:
            lastIndex = len(requestParamObjects) - 1
            for idx, reqParam in enumerate(requestParamObjects):
                reqParamText = reqParamText + reqParam["typeInfo"] + ' ' + reqParam["variableName"]
                if idx != lastIndex:
                    reqParamText += ', '

        definitionText = reponseFieldObjects[0]["typeInfo"] + ' ' + functionName + '(' + reqParamText + ')'
        return definitionText


    def makeFunction(self, functionName, functionSpecObject):
        functionText = ''
        funcDef = self.makeFunctionDefinition(functionName, functionSpecObject['requestParamObjects'], functionSpecObject['reponseFieldObjects'])
        funcReturn = self.makeFunctionReturn(functionSpecObject['reponseFieldObjects'])
        functionText =  '\t' + funcDef + '{\n\n' + \
                        '\t\t' + funcReturn + '\n\n' + \
                        '\t' + '}\n\n'
        return functionText
