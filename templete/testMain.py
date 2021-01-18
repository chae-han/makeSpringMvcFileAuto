import contentBuilder as cb
import contentDirector as cd
import json


#  with open('define.json', 'r+') as f:
# ...     data = json.load(f)
# ...     print(data)
if __name__ == "__main__":
    with open('testDefine.json', 'r+') as f:
        jsondata = json.load(f)
        builder = cb.ContentBuilder()
        director = cd.ContentDirector('controller', 'testname', builder, jsondata, '/Users/terry/terry/caremind/afoter/makeSpringMvcFileAuto/templete/controller/controllerTemplete.java', 
                '/Users/terry/terry/caremind/afoter/makeSpringMvcFileAuto/templete/result_dir/controller/')
        director.makeContent()