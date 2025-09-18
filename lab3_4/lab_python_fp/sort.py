data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, reverse=True, key=abs)
    print(result)

    result_with_lambda = (lambda array: sorted(array, reverse=True, key=abs))(data)
    print(result_with_lambda)