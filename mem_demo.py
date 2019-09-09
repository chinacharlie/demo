import memory_profiler

@memory_profiler.profile
def read_random():
    with open('/dev/urandom', 'rb') as source:
        content = source.read(1024 * 1024 * 10)
        content_cpoy = content[1024:]    #复制，占用10m左右内存。
        
        content_view = memoryview(content)  #提供视图，不拷贝，也不占用内存
        content_view = content_view[1024:]

        print(len(content_cpoy) == len(content_view))

read_random()
