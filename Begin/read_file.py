def file_ops(name):
    with open(name, mode='r') as f:
        print(f.read())
    with open(name, mode='a') as f:
        f.write('\nThis is new content')
    with open(name, mode='r') as f:
        print(f.read())


if __name__ == '__main__':
    file_ops('test.txt')
