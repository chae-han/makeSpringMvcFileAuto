
import shutil
import os

class ContentDirector:

    def __init__(self, mvcOption, classNameLower, contentBuilder, jsonFunctionSpecification, templetePathFile, newDirPath):
        self.classNameLower = classNameLower
        self.classNameFirstUpper = classNameLower.capitalize()

        self.contentBuilder = contentBuilder;
        self.jsonFuncSpec = jsonFunctionSpecification

        self.mvcOption = mvcOption

        self.templetePathFile = templetePathFile
        self.newDirPath = newDirPath
        self.newFilPathFile = newDirPath + self.classNameFirstUpper + mvcOption.capitalize() + '.java'


    def makeMvcDir(self):
        # mkdir [mvc] (controller, service, repository)
        if not os.path.exists(self.newDirPath):
            os.makedirs(self.newDirPath)

    def copyTempleteFile(self):
        shutil.copyfile(self.templetePathFile, self.newFilPathFile)

    def makeFunctionTemplete(self, functionSpecObject):
        functionText = self.contentBuilder.makeFunction(functionSpecObject)
        return functionText

    def makeContent(self):
        try:
            # mkdir [mvc] (controller, service, repository)
            self.makeMvcDir()
            # copy [mvc]Templete.java as dir/[self.classNameFirstUpper][Mvc].java
            # self.copyTempleteFile()
            # read [self.classNameFirstUpper][Mvc].java file as text

            with open(self.newFilPathFile, 'w') as f:
                with open(self.templetePathFile, 'r') as r:
                    fileData = r.read()

                    # replace [classNameFirstUpper] to self.classNameFirstUpper
                    fileData = fileData.replace('[classNameFirstUpper]', self.classNameFirstUpper)

                    # replace [classNameLower] to self.classNameLower
                    fileData = fileData.replace('[classNameLower]', self.classNameLower)

                    # replace [Content] to real content
                    functionsList = list(self.jsonFuncSpec.keys())
                    contentText = ''
                    
                    for functionName in functionsList:
                        contentText += self.makeFunctionTemplete(self.jsonFuncSpec[functionName][self.mvcOption])

                    fileData = fileData.replace('[content]', contentText)

                    # write
                    f.write(fileData)
                    '''
                    with open(self.newFilPathFile, 'r+') as f:
                        while True:
                            line = f.readline()
                            if not line:
                                break
                            print(line)
                            # replace [classNameFirstUpper] to self.classNameFirstUpper
                            if '[classNameFirstUpper]' in line:
                                line = line.replace('[classNameFirstUpper]', self.classNameFirstUpper)
                                #f.write(line.replace('[classNameFirstUpper]', self.classNameFirstUpper))

                            # replace [classNameLower] to self.classNameLower
                            if '[classNameLower]' in line:
                                line = line.replace('[classNameLower]', self.classNameLower)
                                # f.write(line.replace('[classNameLower]', self.classNameLower))


                            # replace [Content] to real content
                            if '[content]' in line:
                                print("content")
                                functionsList = list(self.jsonFuncSpec.keys())
                                contentText = ''

                                for functionName in functionsList:
                                    contentText += self.makeFunctionTemplete(self.jsonFuncSpec[functionName][self.mvcOption])

                                line = line.replace('[content]', contentText)

                            print(line)
                            f.writelines(line)
                    return content
                    '''

        except:
            return []
                
        
