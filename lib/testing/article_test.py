import pytest
from classes.many_to_many import Author, Magazine, Article

class TestArticle:
    """Article in many_to_many.py"""

    def test_valid_title(self):
        """Article is initialized with a valid title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")

        assert article.title == "How to wear a tutu with style"

    def test_title_length(self):
        """Article title length must be between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")

        # Title too short
        with pytest.raises(ValueError, match="Title length must be between 5 and 50 characters inclusive"):
            Article(author, magazine, "Shrt")

        # Title too long
        with pytest.raises(ValueError, match="Title length must be between 5 and 50 characters inclusive"):
            Article(author, magazine, "A" * 51)

    def test_title_is_immutable(self):
        """Article title cannot be changed"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")

        with pytest.raises(AttributeError):
            article.title = "New title"

    def test_title_cannot_be_deleted(self):
        """Article title cannot be deleted"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")

        with pytest.raises(AttributeError):
            del article.title

if __name__ == "__main__":
    pytest.main([__file__])