def test(number):

    def test_in():
        print(number+100)

    print(number)
    return test_in

#test(100)()
print(test(100))
