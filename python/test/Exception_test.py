for s in range(5):
    try:
        for page in range(1, 31):
            print(page)
            # raise Exception('爬取店铺【%s】 第【%s】页评论出错了, 停止爬取' % ('111', str(page)))
    except Exception as e:
        print(e)
        break;
    else:
        print("没有抛出异常")