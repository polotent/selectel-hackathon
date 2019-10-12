class TextProcessor:
    def __init__(self):
        pass

    def validate_link(self, link):
        try:
            if "github.com" in link:
                return True
            else:
                return False
            # if re.match(r'((git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?', link):
            #     return True
            # else:
            #     return False
        except Exception:
            return False
