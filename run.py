from utils.getMsg import *



if __name__=="__main__":
  list = getDataList()
  for item in list:
    print('~~~', item.type, '&&&', item.content, '&&&', item.time)
