# 提供一个功能入口，在TUI中完成操作。
# 同时提供纯命令行方式。

if __name__ == '__main__':
    mode=input("您需要上传还是下载？")
    if mode=="上传":
        upload()
    else:
        download()