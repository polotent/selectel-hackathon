class TextProcessor:
    def validate_link(link):
        try:
            if "github.com" in link:
                return True
            else:
                return False
        except Exception:
            return False
