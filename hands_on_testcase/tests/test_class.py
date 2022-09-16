class TestClass:
    def test_one(self):
        x = "word"
        assert "r" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


class TestClassDemoInstances:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
