
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
    ex) return : \tpublic List<TextAndCountSearchHistoryAcademyVo> findAcademySearchKeyword()
    '''
    def makeFunctionDefinition(self, requestParamObjects, reponseFieldObjects):
        definitionText = ''
        return definitionText


    '''
    primitive type pre definition
        int : return 0;
        boollean : return true;
        String : return '';
    ex) primitive type ) return : \treturn 0;
        collection type ) return : \treturn null;
    '''
    def makeFunctionReturn(self, reponseFieldObjects):
        definitionText = ''
        return definitionText



    def makeFunction(self, functionSpecObject):
        functionText = ''
        funcDef = self.makeFunctionDefinition(functionSpecObject['reponseFieldObjects'], functionSpecObject['reponseFieldObjects'])
        funcReturn = self.makeFunctionReturn(functionSpecObject['reponseFieldObjects'])
        functionText =  '\t' + funcDef + '{\n\n' + \
                        '\t' + funcReturn + '\n\n' + \
                        '\t' + '}\n\n'
        return functionText
